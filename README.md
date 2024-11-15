# 文字起こし・翻訳API

## 環境構築
### 必要環境
- Docker
- VSCode
- Dev Containers (VSCode拡張機能)

### 構築手順
1. VSCodeで `Ctrl(Cmd) + Shift + P` を押し、`DevContainers: Reopen in Container` を選択。
2. ウィンドウが再読み込みされ、必要な設定が適用されます
3. 以下のコマンドで環境確認
    ```bash
    $ python -V  # Python 3.12.7
    $ which flake8  # /usr/local/py-utils/bin/flake8
    $ which black  # /usr/local/py-utils/bin/black
    ```

## 実行方法
### Debug 実行起動 (VSCode)
1. `.env` ファイルに必要な設定を記載（`.env.sample`を参照）。

### ターミナルから起動
```bash
python app/main.py
```

### Docker コンテナから起動
```bash
docker compose up
```

## 動作確認
- `/sample/http.rest` ファイルでリクエスト内容とレスポンスを確認可能。

## 単体テスト
### VSCodeで実行
1. サイドバーの `フラスコ` アイコンからテスト一覧を表示。
2. テストを選択して実行。Debug 実行も可能。

### ターミナルで実行
```bash
pytest          # 全体実行
pytest test_example.py  # 特定のテストを実行
pytest -v       # 詳細出力付きで実行
```
