import requests

def buscar_jogo(nome_jogo, api_key):
    url = "https://api.rawg.io/api/games"
    params = {
        'key': api_key,
        'page_size': 1,
        'search': nome_jogo
    }
    
    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()  
        dados = resposta.json()

        if dados['results']:
            jogo = dados['results'][0]
            nome = jogo.get('name', 'N/A')
            ano_lancamento = jogo.get('released', 'N/A')
            categorias = [genero.get('name', 'N/A') for genero in jogo.get('genres', [])]
            plataformas = [plataforma['platform']['name'] for plataforma in jogo.get('platforms', [])]
            desenvolvedores = [dev['name'] for dev in jogo.get('developers', [])]
            classificacao = jogo.get('esrb_rating', {}).get('name', 'N/A')
            descricao = jogo.get('description_raw', 'N/A')
            imagem = jogo.get('background_image', 'N/A')

            gerar_html(nome, ano_lancamento, categorias, plataformas, desenvolvedores, classificacao, descricao, imagem)
        else:
            print("Jogo não encontrado.")
    except requests.RequestException as e:
        print(f"Erro ao buscar jogo: {e}")

def gerar_html(nome, ano_lancamento, categorias, plataformas, desenvolvedores, classificacao, descricao, imagem):
    html_conteudo = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Detalhes do Jogo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
            }}
            h1 {{
                color: #333;
            }}
            .imagem {{
                width: 100%;
                max-width: 500px;
                height: auto;
                margin-bottom: 20px;
            }}
            .info {{
                margin-bottom: 20px;
            }}
            .info label {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{nome}</h1>
            <img src="{imagem}" alt="Imagem do {nome}" class="imagem">
            <div class="info">
                <label>Ano de Lançamento:</label> {ano_lancamento}<br>
                <label>Categoria(s):</label> {', '.join(categorias)}<br>
                <label>Plataforma(s):</label> {', '.join(plataformas)}<br>
                <label>Desenvolvedor(es):</label> {', '.join(desenvolvedores)}<br>
                <label>Classificação ESRB:</label> {classificacao}<br>
           
             
            </div>
        </div>
    </body>
    </html>
    """

    with open('detalhes_jogo.html', 'w', encoding='utf-8') as arquivo:
        arquivo.write(html_conteudo)
    print("Arquivo HTML gerado com sucesso.")

def main():
    api_key = "6c69bfae5674443a9790d706e84c0a69"  
    nome_jogo = input("Digite o nome do jogo: ")
    buscar_jogo(nome_jogo, api_key)

if __name__ == "__main__":
    main()
