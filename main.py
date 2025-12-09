from fpdf import FPDF
import sqlite3

# -------------------- BUSCAR DADOS DO BANCO --------------------
def buscar_todos():
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    linhas = cur.fetchall()
    con.close()

    colunas = [
        "id", "livro", "registro", "data_registro", "curso", "conclusao", "nome", "nascimento",
        "nacionalidade", "naturalidade", "uf", "rg", "orgao", "data_rg",
        "cpf", "secretaria"
    ]

    return [dict(zip(colunas, linha)) for linha in linhas]


# -------------------- CLASSE PDF PERSONALIZADA --------------------
class PDF(FPDF):

    def header(self):

        # Título SENAC
        self.set_font("Noto", "B", 14)
        self.cell(
            0, 10,
            "LIVRO DE REGISTRO DE DIPLOMA – CURSOS TÉCNICOS SENAC SOBRADINHO",
            new_x="LMARGIN", new_y="NEXT", align="C"
        )

        # Página
        self.set_font("Noto", "", 11)
        self.cell(0, 8, "Página 210", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def bloco_registro(self, dados, y):

        ALTURA_BLOCO = 72
        LARGURA_BLOCO = 175
        X_INICIO = 17

        self.set_line_width(0.5)
        self.rect(X_INICIO, y, LARGURA_BLOCO, ALTURA_BLOCO)

        self.set_xy(X_INICIO + 3, y + 3)
        self.set_font("Noto", "", 10)

        linhas = [
            f"Livro: {dados['livro']}     Registro nº {dados['registro']}     Data de Registro: {dados['data_registro']}",
            f"Turma/Curso: {dados['curso']}     Conclusão: {dados['conclusao']}",
            f"Aluno: {dados['nome']}     Data de Nascimento: {dados['nascimento']}",
            f"Nacionalidade: {dados['nacionalidade']}     Naturalidade: {dados['naturalidade']}     UF: {dados['uf']}",
            f"Identidade: {dados['rg']}     Expedidor: {dados['orgao']}     Data Expedição: {dados['data_rg']}",
            f"CPF: {dados['cpf']}",
            "",
            f"{dados['secretaria']}",
            "Secretaria Escolar Reg nº 2213",
            "Colégio Integrado Polivalente",
            "Brasília - DF",
            "",
            "Observações:",
            "Recebi originais em ___/___/_____     Assinatura do Aluno(a) ____________________________",
        ]

        for linha in linhas:
            self.cell(0, 5, linha, new_x="LMARGIN", new_y="NEXT")

        return y + ALTURA_BLOCO + 10


# -------------------- GERAR PDF FINAL --------------------
def gerar_pdf():

    alunos = buscar_todos()

    pdf = PDF("P", "mm", "A4")

    # Registrar fontes Unicode
    pdf.add_font("Noto", "", "fonts/NotoSans-Regular.ttf")
    pdf.add_font("Noto", "B", "fonts/NotoSans-Bold.ttf")

    pdf.alias_nb_pages()
    pdf.add_page()

    y = 40
    contador = 0

    for a in alunos:
        y = pdf.bloco_registro(a, y)
        contador += 1

        if contador % 3 == 0:
            pdf.add_page()
            y = 40

    pdf.output("registro_fpdf2.pdf")
    print("PDF gerado com sucesso usando FPDF2!")


gerar_pdf()
