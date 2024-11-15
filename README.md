# 文字起こし・翻訳API

## 環境変数

## 起動手順
1. 前提条件 (以下が使用できる環境であること)  
    - docker
    - VSCode
    - Dev Containers(VSCode拡張機能)
1. VSCode を開いたら, Ctrl + Shift + P で出てくる検索窓で、 `DevContainers: Reopen in Container` を選択
1. ウィンドウが再読み込みされ、python や 必要な拡張機能、 format 設定がされたウィンドウが開かれる
1. コマンドの確認
    ```bash
    $ python -V
    Python 3.12.7
    $ which flake8
    /usr/local/py-utils/bin/flake8
    $ which black
    /usr/local/py-utils/bin/black
    ```

### VSCode の Debug 実行
1. .env に必要な設定を記載(.env.sampleを参照)
1. 
### ターミナルから実行
```
python app/main.py
```
### Docker コンテナから実行
```
docker compose up
```

## 動作確認
`/sample/http.rest` ファイルから、リクエスト内容とレスポンスの内容を確認できる

## 単体テスト実行手順
- vscode Testing により実行  
VSCode サイドバーにある `フラスコ`のマークから、テスト一覧を表示でき, 実行できます.  
debug 実行も可能です.

- ターミナルで実行
    ```bash
    pytest  # 全体実行
    pytest test_example.py  # 単体実行
    pytest -v  # 詳細出力
    ```