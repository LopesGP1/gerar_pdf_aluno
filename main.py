from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gerar_pdf(dados_aluno):
    pdf = SimpleDocTemplate("registro_aluno.pdf", pagesize=A4)
    elementos = []

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    titulo = styles["Title"]

    # LOGO DA EMPRESA
    try:
        logo = Image("logo.png", width=100, height=100)
        elementos.append(logo)
    except:
        elementos.append(Paragraph("LOGO NÃO ENCONTRADA", titulo))

    elementos.append(Spacer(1, 20))

    elementos.append(Paragraph("LIVRO DE REGISTRO DE DIPLOMA – CURSOS TÉCNICOS", titulo))
    elementos.append(Spacer(1, 10))

    tabela_dados = [
        [f"Livro: {dados_aluno['livro']}",
         f"Registro nº {dados_aluno['registro']}",
         f"Data de Registro: {dados_aluno['data_registro']}"],

        [f"Turma/Curso: {dados_aluno['curso']}",
         f"Conclusão: {dados_aluno['conclusao']}", ""],

        [f"Aluno: {dados_aluno['nome']}",
         f"Data de Nascimento: {dados_aluno['nascimento']}", ""],

        [f"Nacionalidade: {dados_aluno['nacionalidade']}",
         f"Naturalidade: {dados_aluno['naturalidade']}",
         f"UF: {dados_aluno['uf']}"],

        [f"Identidade: {dados_aluno['rg']}",
         f"Expedidor: {dados_aluno['orgao']}",
         f"Data Expedição: {dados_aluno['data_rg']}"],

        [f"CPF: {dados_aluno['cpf']}", "", ""]
    ]

    tabela = Table(tabela_dados, colWidths=[180, 180, 150])
    tabela.setStyle(TableStyle([
        ('FONT', (0,0), (-1,-1), 'Helvetica', 10),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))

    elementos.append(tabela)
    elementos.append(Spacer(1, 20))

    elementos.append(Paragraph("Observações:", normal))
    elementos.append(Spacer(1, 10))
    elementos.append(Paragraph("Recebi originais em ___/___/_____  Assinatura do Aluno (a) ________________________________", normal))

    elementos.append(Spacer(1, 30))

    elementos.append(Paragraph(dados_aluno["secretaria"], normal))
    elementos.append(Paragraph("Secretaria Escolar", normal))
    elementos.append(Paragraph("Colégio Integrado Polivalente", normal))
    elementos.append(Paragraph("Brasília - DF", normal))

    pdf.build(elementos)
    print("PDF criado com sucesso!")

# EXEMPLO DE DADOS
dados = {
    "livro": "03",
    "registro": "1203 / 65E3E883",
    "data_registro": "27/08/2025",
    "curso": "2022.11.14 - TÉCNICO EM ADMINISTRAÇÃO",
    "conclusao": "28/11/2024",
    "nome": "Maria Alves Silva",
    "nascimento": "01/01/2000",
    "nacionalidade": "Brasileira",
    "naturalidade": "SOBRADINHO",
    "uf": "DF",
    "rg": "11111-00",
    "orgao": "SESP/DF",
    "data_rg": "01/01/2010",
    "cpf": "000.000.000-00",
    "secretaria": "Bruna de Oliveira Macedo Pires (Reg nº 2213)"
}

gerar_pdf(dados)
