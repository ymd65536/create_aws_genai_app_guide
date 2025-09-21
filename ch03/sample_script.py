# memo: 書籍ではjsonがインポートされていますが、使用していないため削除しました

from __future__ import annotations
from typing import TYPE_CHECKING

from pprint import pprint
import boto3


if TYPE_CHECKING:
    from mypy_boto3_bedrock_runtime.client import BedrockRuntimeClient # pyright: ignore[reportMissingImports]

# memo: リージョンは適宜変更してください
bedrock_runtime_client: "BedrockRuntimeClient" = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2",
)


if __name__ == "__main__":
    try:
        response = bedrock_runtime_client.converse(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            system=[
                {
                    "text": "あなたは愉快なチャットbotです。<response></response>タグで返答をします。"
                }
            ],
            messages=[{"role": "user", "content": [{"text": "こんにちは!"}]}],
            inferenceConfig={
                "temperature": 0.1,
                "maxTokens": 512,
                "stopSequences": ["</response>"],
            },
        )
        pprint(response)
    except Exception as e:
        print(f"Error: {e}")
