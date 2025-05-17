# backend-evolve

AIスケジューラーの開発を目的とした、Poetry + FastAPI ベースのモダンなバックエンドプロジェクトです。  
まずは開発環境の基礎構築から開始しています。

## 📦 開発環境

- Python 3.10.4（pyenv管理）
- Poetry（依存管理、仮想環境）
- FastAPI + Uvicorn（APIフレームワーク）

## 🚀 起動方法

```bash
# 依存インストール
poetry install

# サーバ起動（ローカル）
poetry run uvicorn main:app --reload
