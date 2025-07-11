from fpdf import FPDF
import io

def gerar_pdf(dados, economia):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "GreenFlex - Relatório Personalizado", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)

    def safe(value):
        return str(value) if value is not None else "-"

    pdf.cell(200, 10, f"Nome: {safe(dados.get('nome'))}", ln=True)
    pdf.cell(200, 10, f"Endereço: {safe(dados.get('endereco'))}", ln=True)
    pdf.cell(200, 10, f"Mês Referência: {safe(dados.get('referencia'))}", ln=True)
    pdf.cell(200, 10, f"Vencimento: {safe(dados.get('vencimento'))}", ln=True)
    pdf.cell(200, 10, f"Consumo: {safe(dados.get('consumo_kwh'))} kWh", ln=True)
    pdf.cell(200, 10, f"Créditos Compensados: {safe(dados.get('creditos_compensados'))} kWh", ln=True)
    pdf.cell(200, 10, f"Saldo de Créditos: {safe(dados.get('saldo_creditos'))} kWh", ln=True)
    pdf.cell(200, 10, f"Valor Original: R$ {safe(dados.get('valor_total'))}", ln=True)
    pdf.cell(200, 10, f"Economia Estimada: R$ {safe(economia.get('economia_reais'))}", ln=True)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return pdf_bytes
