import sys

from app.util import switcher

if __name__ == "__main__" and len(sys.argv) == 2:
    switcher.app_switch()
else:
    print("Please input args of enviroment name")
