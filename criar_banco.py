import sqlite3

con = sqlite3.connect("alunos.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro TEXT,
    registro TEXT,
    data_registro TEXT,
    curso TEXT,
    conclusao TEXT,
    nome TEXT,
    nascimento TEXT,
    nacionalidade TEXT,
    naturalidade TEXT,
    uf TEXT,
    rg TEXT,
    orgao TEXT,
    data_rg TEXT,
    cpf TEXT,
    secretaria TEXT
)
""")

# ------- INSERIR 3 ALUNOS PARA TESTE -------

alunos = [
    (
        '03', '1203 / 65E3E883', '27/08/2025',
        'Técnico em Administração', '28/11/2024',
        'Maria Alves Silva', '01/01/2000',
        'Brasileira', 'Sobradinho', 'DF',
        '11111-00', 'SESP/DF', '01/01/2010',
        '000.000.000-00', 'Bruna de Oliveira Macedo Pires (Reg nº 2213)'
    ),
    (
        '03', '1204 / 77X9G122', '27/08/2025',
        'Técnico em Informática', '30/11/2024',
        'João Pereira Santos', '12/05/1999',
        'Brasileiro', 'Planaltina', 'DF',
        '22222-00', 'SESP/DF', '12/02/2012',
        '111.111.111-11', 'Bruna de Oliveira Macedo Pires (Reg nº 2213)'
    ),
    (
        '03', '1205 / 88P2K441', '27/08/2025',
        'Técnico em Logística', '30/11/2024',
        'Ana Clara Rodrigues', '20/09/2001',
        'Brasileira', 'Brasília', 'DF',
        '33333-00', 'SSP/DF', '22/07/2014',
        '222.222.222-22', 'Bruna de Oliveira Macedo Pires (Reg nº 2213)'
    )
]

cur.executemany("""
INSERT INTO alunos (
    livro, registro, data_registro, curso, conclusao, nome, nascimento,
    nacionalidade, naturalidade, uf, rg, orgao, data_rg, cpf, secretaria
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", alunos)

con.commit()
con.close()

print("Banco criado com 3 alunos!")
