# Poetry 2.x の使い方

## 基本的な使い方

### 1. 依存関係のインストール
```bash
poetry install
```
これで依存関係がインストールされます。`package-mode = false`を設定しているので、プロジェクト自体をパッケージとしてインストールしようとしません。

### 2. Pythonスクリプトの実行

Poetry 2.xでは`poetry shell`が廃止されました。以下の2つの方法があります：

#### 方法1: `poetry run`を使う（推奨）
```bash
poetry run python test_claude.py
poetry run pytest
```

#### 方法2: 仮想環境を直接アクティベート
```bash
# 仮想環境のパスを確認
poetry env info --path

# zshの場合
source $(poetry env info --path)/bin/activate

# その後、通常通りPythonコマンドが使える
python test_claude.py
pytest
```

### 3. 環境変数の読み込み

`.env`ファイルがある場合、`python-dotenv`を使って読み込むことができます：

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
```

### 4. 新しいパッケージの追加
```bash
poetry add <パッケージ名>
```

### 5. 開発用依存関係の追加
```bash
poetry add --group dev <パッケージ名>
```

## 便利なコマンド

- `poetry env info`: 仮想環境の情報を表示
- `poetry env info --path`: 仮想環境のパスを表示
- `poetry show`: インストール済みパッケージを表示
- `poetry update`: 依存関係を更新



