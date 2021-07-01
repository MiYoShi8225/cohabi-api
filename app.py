# 標準ライブラリー
import sys

# 自作ライブラリー
from app.util import logger, switcher, common
switcher.logger(common.FileName(__file__))

# mainで実行された時と引数(環境名)を渡した状態で実行される
if __name__ == "__main__" and len(sys.argv) == 2:
    logger.info('start app.py')

    # switcherを呼び出して環境に合わせたuvicornの実行を行う
    switcher.app_switch()

    logger.info('end app.py')
