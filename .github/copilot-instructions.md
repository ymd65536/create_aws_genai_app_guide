# AWS GenAI アプリケーションガイド用 Copilot 指示書

## プロジェクト概要
これは AWS CLI のセットアップと Amazon Bedrock 統合のための **日本語教育ガイド** です。AWS GenAI 開発のための実践的な Python サンプルを含む段階的チュートリアルで構成されています。

## 主要なアーキテクチャと構造
- **ルート README.md**: Linux 環境での AWS CLI インストールと SSO 認証ガイド
- **ch03/**: 仮想環境設定を含む Amazon Bedrock Python 統合サンプル
- **言語**: すべてのドキュメントとコメントは日本語

## 重要な開発パターン

### AWS CLI インストールコマンド
常にアーキテクチャに依存しないコマンドを使用してください：
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-$(uname -m).zip" -o "awscliv2.zip"
```
`x86_64` をハードコードしないでください - クロスプラットフォーム対応のため `$(uname -m)` を使用してください。

### Python 環境セットアップパターン
各章では分離された仮想環境を使用します：
```bash
python -m venv prompt
source ./prompt/bin/activate
pip install -r ./prompt/requirements.txt
```
仮想環境名は常に `prompt` を使用してください（`venv` や他の名前ではありません）。

### Amazon Bedrock 統合
- **クライアントのインスタンス化**: boto3 クライアントで明示的に `region_name` を指定してください
- **モデル ARN 形式**: `arn:aws:bedrock:<region>::foundation-model/<model-name>`
- **型ヒント**: ランタイム依存関係を避けるため、mypy_boto3 型ヒントには TYPE_CHECKING インポートを使用してください
- **エラーハンドリング**: Bedrock API 呼び出しを try/except ブロックで囲み、わかりやすいエラーメッセージを含めてください

### コードスタイル規約
- 前方互換性のため `from __future__ import annotations` を使用してください
- 重要な注記や参考資料からの逸脱については `# memo:` コメントを含めてください
- API レスポンスのデバッグには `pprint` を使用してください
- AWS SDK 型には TYPE_CHECKING パターンを使った明示的型指定に従ってください

## 必須ワークフロー

### Bedrock 統合のテスト
```bash
cd ch03
source ./prompt/bin/activate
python sample_script.py
```

### 新しい章の追加
- 日本語ドキュメントで `ch[XX]/README.md` を作成してください
- 仮想環境セットアップ手順を含めてください
- 適切なエラーハンドリングを含むサンプル Python スクリプトを追加してください
- 新しい前提条件がある場合はルート README.md を更新してください

## AWS 固有のパターン
- **SSO プロファイル**: デフォルトプロファイル名は `default` を使用してください
- **リージョン**: サンプルは Bedrock に `us-west-2`、一般的な AWS サービスに `us-east-1` を使用します
- **認証**: すべてのサンプルは IAM キーではなく AWS SSO を前提としています
- **モデル ID**: 安定したモデルバージョンを使用してください（例：`anthropic.claude-3-sonnet-20240229-v1:0`）

## ドキュメント標準
- すべての技術ドキュメントは日本語で記述してください
- インストール例の後にクリーンアップコマンドを含めてください
- トラブルシューティングセクションで具体的なエラーシナリオと解決策を提供してください
- 可能な場合は公式 AWS ドキュメントの日本語リンクを参照してください

## ファイル構成
- 仮想環境は各章固有のディレクトリに保持してください
- 目的に合った説明的な Python スクリプト名を使用してください
- 再現性のためバージョンを固定した requirements.txt を含めてください
- すべてのPythonコードは PEP 8 に準拠してください
