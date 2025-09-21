
# Python仮想環境の有効化

## Linuxの場合

仮想環境を作成します。

```bash
python -m venv prompt
```

仮想環境を有効化します。

```bash
source ./prompt/bin/activate
```

パッケージをインストールします。

```bash
pip install -r ./prompt/requirements.txt
```

サンプルスクリプトを実行します。

```bash
python sample_script.py 
```

## Amazon Bedrockに関すること


### model ARNについて

モデルのARNは、以下の形式で指定します。

```
arn:aws:bedrock:<region>::foundation-model/<model-name>
```

具体例としては以下のとおりです。

モデルID： anthropic.claude-3-5-sonnet-20240620-v1:0
モデルARN： arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0

モデルIDは以下のドキュメントで確認できます

[Amazon Bedrock でサポートされている基盤モデル - Amazon Bedrock](https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/models-supported.html)
