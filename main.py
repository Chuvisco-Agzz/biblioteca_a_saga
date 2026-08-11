import csv
livros = []

# Função para salvar os livros no arquivo CSV
def salvar_livros():
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["isbn", "titulo", "autor", "ano", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for livro in livros:
            escritor.writerow(livro)

# Função para carregar os livros do arquivo CSV
def carregar_livros():
    with open("livros.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for livro in leitor:
            livro["isbn"] = int(livro["isbn"])
            livros.append(livro)