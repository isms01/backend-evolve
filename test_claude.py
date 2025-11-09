# test_claude.py
import os

from anthropic import Anthropic
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hello, world!"}],
)

# レスポンス内容を表示
print("=== レスポンス ===")
print(message.content[0].text)
print()

# 使用量と料金を表示
print("=== 使用量 ===")
print(f"入力トークン: {message.usage.input_tokens}")
print(f"出力トークン: {message.usage.output_tokens}")
print(f"合計トークン: {message.usage.input_tokens + message.usage.output_tokens}")
print()

# 料金計算（Claude Sonnet 4.5 = Claude 3.5 Sonnetと同じ料金）
INPUT_COST_PER_MT = 3.0  # ドル/百万トークン（入力）
OUTPUT_COST_PER_MT = 15.0  # ドル/百万トークン（出力）

input_cost = (message.usage.input_tokens / 1_000_000) * INPUT_COST_PER_MT
output_cost = (message.usage.output_tokens / 1_000_000) * OUTPUT_COST_PER_MT
total_cost_usd = input_cost + output_cost

print("=== 料金（概算）===")
print(f"入力: ${input_cost:.10f} USD")
print(f"出力: ${output_cost:.10f} USD")
print(f"合計: ${total_cost_usd:.10f} USD")
print(f"約: {total_cost_usd * 150:.6f} 円 (@ 1USD=150円)")
