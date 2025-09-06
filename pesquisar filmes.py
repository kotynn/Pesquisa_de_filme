import requests

api_key = "503a0607"

def pegar_filme(titulo):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados.get("Response") == "True":
            return dados
        else:
            print("Filme não encontrado!")
            return None
    else:
        print("Erro na requisição!")
        return None
    
def buscar_filme(titulo):
    dados = pegar_filme(titulo)

    if dados:
        print(f"\nTítulo: {dados['Title']}")
        print(f"Ano: {dados['Year']}")
        print(f"Atores: {dados['Actors']}")
        print(f"Gênero: {dados['Genre']}")
        print(f"Enredo: {dados['Plot']}")
        print(f"Nota IMDb: {dados['imdbRating']}")

while True:
    nome = input("Digite o nome do filme (ou digite 'sair' para sair): ")    
    if nome.lower() == "sair":
        break
    buscar_filme(nome)
