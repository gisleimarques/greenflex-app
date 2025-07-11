from fpdf import FPDF
import io

def gerar_pdf(dados, economia):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "GreenFlex - Relatório Personalizado", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)

    pdf.cell(200, 10, f"Nome: {dados.get('nome', '')}", ln=True)
    pdf.cell(200, 10, f"Endereço: {dados.get('endereco', '')}", ln=True)
    pdf.cell(200, 10, f"Mês Referência: {dados.get('referencia', '')}", ln=True)
    pdf.cell(200, 10, f"Vencimento: {dados.get('vencimento', '')}", ln=True)
    pdf.cell(200, 10, f"Consumo: {dados.get('consumo_kwh', 0)} kWh", ln=True)
    pdf.cell(200, 10, f"Créditos Compensados: {dados.get('creditos_compensados', 0)} kWh", ln=True)
    pdf.cell(200, 10, f"Saldo de Créditos: {dados.get('saldo_creditos', 0)} kWh", ln=True)
    pdf.cell(200, 10, f"Valor Original: R$ {dados.get('valor_total', 0)}", ln=True)
    pdf.cell(200, 10, f"Economia Estimada: R$ {economia.get('economia_reais', 0)}", ln=True)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()
