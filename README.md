# Sistema de Ranking Automatizado em Python

Este projeto consiste em um **sistema de automação desenvolvido em Python** que realiza a leitura de dados estruturados em JSON, aplica **regras configuráveis de pontuação** e gera automaticamente um **ranking ordenado** como resultado.

Inicialmente criado para controle de campeonatos, o sistema foi estruturado de forma modular para permitir fácil adaptação a outros cenários de **processamento e organização de dados**.

## 🚀 Funcionalidades

- Leitura de dados a partir de arquivo JSON
- Regras de pontuação configuráveis sem necessidade de alterar o código
- Cálculo automático de:
  - Pontos
  - Saldo de gols
- Ordenação do ranking por critérios definidos
- Geração automática de arquivo final com os resultados processados

## 📁 Estrutura do projeto

backend/
├── data/
│ └── campeonato.json
├── src/
│ ├── data_manager.py
│ ├── tabela.py
│ └── main.py
├── output/
│ └── tabela_final.json

## ⚙️ Como executar o projeto

1. Acesse a pasta do backend:

```bash
cd backend/src


Execute o sistema:

python main.py


O resultado será gerado automaticamente em:

backend/output/tabela_final.json

📥 Estrutura de entrada (JSON)

Exemplo de arquivo campeonato.json:

{
  "config": {
    "pontos_vitoria": 3,
    "pontos_empate": 1,
    "pontos_derrota": 0
  },
  "times": [
    {
      "nome": "Time A",
      "vitorias": 2,
      "empates": 1,
      "derrotas": 0,
      "gols_pro": 6,
      "gols_contra": 2
    },
    {
      "nome": "Time B",
      "vitorias": 1,
      "empates": 1,
      "derrotas": 1,
      "gols_pro": 3,
      "gols_contra": 3
    }
  ]
}

📤 Estrutura de saída

O sistema gera automaticamente um ranking processado e ordenado:

{
  "tabela": [
    {
      "nome": "Time A",
      "pontos": 7,
      "saldo_gols": 4,
      "gols_pro": 6
    },
    {
      "nome": "Time B",
      "pontos": 4,
      "saldo_gols": 0,
      "gols_pro": 3
    }
  ]
}

🧠 Possíveis aplicações

Automação de rankings e classificações

Processamento de dados estruturados

Geração automática de relatórios

Organização e análise de métricas

Substituição de controles manuais em planilhas

🛠 Tecnologias utilizadas

Python

JSON

Estrutura modular e organizada

Boas práticas de separação de responsabilidades

👨‍💻 Autor

João Vitor Mendonça




```
