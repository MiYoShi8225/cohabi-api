# anacondaを使用したflask環境作成コマンド

## ベース
``` sh
アナコンダを使用した場合のpython環境の作成
# conda create -n pythonenv python=3.8

上で作成したpythonenvを適用する。
# source activate pythonenv

anacondaに入っている環境をリストで表示できる
# conda env list

"""
# conda environments:
#
base                     /Users/miyoshishun/opt/anaconda3
pythonenv             *  /Users/miyoshishun/opt/anaconda3/envs/pythonenv
"""

環境をベース(mac標準)に戻す
# conda deactivate
"""
(pythonenv) miyoshishun@miyoshishunnoMacBook-Air python-flask-dev % conda deactivate
(base) miyoshishun@miyoshishunnoMacBook-Air python-flask-dev % 
"""

作成した環境を削除する
# conda remove -n pythonenv --all

```


## 作成環境
```sh
# conda create -n flaskenv python=3.8

# conda activate flaskenv

flaskが入っていないことを確認する
# conda list

flaskをインストールする
# pip install flask

flaskが入ったことを確認する
# conda list


```

