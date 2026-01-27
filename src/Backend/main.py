from data_manager import carregar_dados, salvar_resultado
from tabela import calcular_tabela


def main():
    dados = carregar_dados()
    tabela_final = calcular_tabela(dados)

    salvar_resultado({
        "tabela": tabela_final
    })

    print("✅ Tabela gerada com sucesso!")


if __name__ == "__main__":
    main()

