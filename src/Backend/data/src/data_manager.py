import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "campeonato.json"
OUTPUT_PATH = BASE_DIR / "output" / "tabela_final.json"


def carregar_dados():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def salvar_resultado(dados):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

