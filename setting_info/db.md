# DB の設定

## DB のマイグレーション

### とは

- 開発中に DB のテーブル定義が変わった時のバージョニングをしたい
- 人間が管理するのは大変なので、ツールを使う
- python で有名なツール[alembic](https://github.com/sqlalchemy/alembic)を使用
  - sqlalchemy という ORM と互換性が良いらしいが、使っていないので無視
  - マイグレーションする機能だけ使用する

### インストール

```shell
$ > pip install alembic
```

### 設定

- 接続設定は、`key/secret.json`を使用します。**間違って本番環境に migration 投げないように注意**。なんかいい方法ないかな...
- 一応、`db/env.py`の中で接続設定ファイルの場所を指定しているので、そこを変えれば本番とファイル名共用しなくて済みはする。

### マイグレーションの実行

```shell
# secret.json の内容を確認してから
cohabi-api > alembic upgrade head
```

### DB に変更を加える場合

```shell
cohabi-api > alembic revision -m "some operation name"
# db/versions/xxxxxxxxxxxx_some_operation_name.pyが作成される
```

- 作成されたファイルに加える変更内容をスクラッチで書いて、マイグレーションの実行を行う
  - sqlalchemy と連携することで auto generate できるらしいけど、ORM 使わないので無視
- 基本的に一度マイグレーション投げたら変更しない
  - 変更する場合は、一度ダウングレードしてからファイルを変更し、再度マイグレーションを行う
