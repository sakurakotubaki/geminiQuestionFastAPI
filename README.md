# Gemini Question API

Google の Gemini API を使用した質問応答 API サービスです。FastAPI フレームワークを使用して実装されています。

## アーキテクチャ

このプロジェクトはクリーンアーキテクチャの原則に従って、以下の3層で構成されています：

### 1. Presentation Layer (API Layer)
- `app/presentation/api.py`
- FastAPI のルーティングとリクエスト/レスポンスの処理を担当
- エンドポイントの定義と入力バリデーションを実装

### 2. Use Case Layer (Service Layer)
- `app/usecase/question_service.py`
- ビジネスロジックを実装
- Gemini API とのやり取りを抽象化

### 3. Infrastructure Layer
- `app/infrastructure/gemini_client.py`
- 外部サービス（Gemini API）とのインテグレーション
- 環境変数の管理

## 環境構築

### 前提条件
- Python 3.8以上
- Gemini API キー

### セットアップ手順

1. リポジトリのクローン
```bash
git clone [your-repository-url]
cd geminiQuestionFastAPI
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
# または
.\venv\Scripts\activate  # Windows
```

3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
`.env.example` をコピーして `.env` を作成し、Gemini API キーを設定します：
```bash
cp .env.example .env
```
`.env` ファイルを編集し、`GEMINI_API_KEY` に実際の API キーを設定してください。

5. アプリケーションの起動
```bash
uvicorn main:app --reload
```

## API の使用方法

### 質問エンドポイント

- URL: `http://localhost:8000/question`
- Method: POST
- Headers: 
  - `Content-Type: application/json`
- Request Body:
```json
{
    "prompt": "あなたの質問をここに入力してください"
}
```
- Response:
```json
{
    "response": "Gemini API からの応答テキスト"
}
```

### サンプルリクエスト（curl）

```bash
curl -X POST http://localhost:8000/question \
     -H "Content-Type: application/json" \
     -d '{"prompt": "こんにちは、今日の天気を教えてください"}'
```

### サンプルリクエスト（Python）

```python
import requests

response = requests.post(
    "http://localhost:8000/question",
    json={"prompt": "こんにちは、今日の天気を教えてください"}
)
print(response.json())
```

## エラーハンドリング

- API キーが設定されていない場合: 500 エラー
- Gemini API からのエラーレスポンス: 500 エラー
- 不正なリクエストボディ: 422 エラー
