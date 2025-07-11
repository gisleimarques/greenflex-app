def calcular_economia(dados):
    tarifa_media = 0.30
    creditos_kwh = dados.get("creditos_compensados", 0)
    economia = round(creditos_kwh * tarifa_media, 2)
    return {"economia_reais": economia}
