import json
from jose import jwt
from urllib.request import urlopen
from starlette.requests import Request

from app.util import logger

# FIXME: 開発時以外は必ずTrueにすること
DISABLE_AUTH = False
AUTH0_DOMAIN = 'dev-uql6wxih.jp.auth0.com'
API_AUDIENCE = 'https://api-staging.cohabi.runemosuky.com'
ALGORITHMS = ["RS256"]


class AuthResult:
    def __init__(self, error_code: str = "", error_detail: str = "", usersub: str = None) -> None:
        self.error_code = error_code
        self.error_detail = error_detail
        self.user = usersub

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)


def create_auth_error(code: str = "", detail: str = ""):
    logger.error(
        "AUTH ERROR [CODE]: {0} [DETAIL]: {1}".format(code, detail))
    return AuthResult(error_code=code, error_detail=detail)


def get_jwk_from_auth0API():
    # Auth0APIからJWK(公開鍵)を取得
    jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    return jwks


def authorized_user(request: Request) -> AuthResult:
    if DISABLE_AUTH:
        return AuthResult(usersub="testuser01")

    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        return create_auth_error(code="authorization_header_missing", detail="Authorization header is expected")
    parts = auth.split()
    if parts[0].lower() != "bearer":
        return create_auth_error(code="invalid_header", detail="Authorization header must start with Bearer")
    elif len(parts) == 1:
        return create_auth_error(code="invalid_header", detail="Token not found")
    elif len(parts) > 2:
        return create_auth_error(code="invalid_header", detail="Authorization header must be Bearer token")
    token = parts[1]

    """Get Public Key from Auth0
    """
    jwks = get_jwk_from_auth0API()

    try:
        unverified_header = jwt.get_unverified_header(token)
    except Exception:
        return create_auth_error(code="unable_decode_token", detail="Token must include unverified header")

    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://"+AUTH0_DOMAIN+"/"
            )
        except jwt.ExpiredSignatureError:
            return create_auth_error(code="token_expired", detail="token is expired")
        except jwt.JWTClaimsError:
            return create_auth_error(code="invalid_claims", detail="incorrect claims, please check the audience and issuer")
        except Exception:
            return create_auth_error(code="invalid_header", detail="Unable to parse authentication, token.")
        return AuthResult(usersub=payload['sub'])
    return create_auth_error(code="invalid_header", detail="Unable to find appropriate key")
