import json


def get_db_dsn(path: str) -> str:
    with open(path) as f:
        acskey = json.load(f)

    db_acs = acskey['database']

    return 'mysql://{user}:{passwd}@{host}/{dbname}'.format(
        user=db_acs["user"],
        passwd=db_acs["passwd"],
        host=db_acs["host"],
        dbname=db_acs["db"],
    )
