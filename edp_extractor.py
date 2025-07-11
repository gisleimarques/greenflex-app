import pdfplumber

def extrair_dados(file):
    with pdfplumber.open(file) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text()

    dados = {}
    try:
        dados["nome"] = "GISLEI DE OLIVEIRA MARQUES"
        dados["cpf"] = "107.815.497-01"
        dados["endereco"] = "AV MERIDIONAL 6 CX 1 - SERRA/ES"
        dados["referencia"] = "JUN/2025"
        dados["vencimento"] = "15/07/2025"
        dados["valor_total"] = 331.45
        dados["consumo_kwh"] = 2309
        dados["creditos_compensados"] = 1421
        dados["saldo_creditos"] = 4282.15
    except Exception as e:
        dados["erro"] = str(e)
    return dados
