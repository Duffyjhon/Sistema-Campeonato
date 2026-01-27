def calcular_tabela(dados):
    config = dados["config"]
    times = dados["times"]

    for time in times:
        pontos = (
            time["vitorias"] * config["pontos_vitoria"]
            + time["empates"] * config["pontos_empate"]
            + time["derrotas"] * config["pontos_derrota"]
        )

        saldo_gols = time["gols_pro"] - time["gols_contra"]

        time["pontos"] = pontos
        time["saldo_gols"] = saldo_gols

    # Ordenação:
    # 1º pontos
    # 2º saldo de gols
    # 3º gols pró
    tabela_ordenada = sorted(
        times,
        key=lambda t: (t["pontos"], t["saldo_gols"], t["gols_pro"]),
        reverse=True
    )

    return tabela_ordenada
