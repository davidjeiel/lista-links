import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obter_links_diretorios(url):
    # Faz a requisição GET para a página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra todos os elementos <a> na página
        links = soup.find_all('a')

        # Lista para armazenar os links de diretórios
        diretorios = []

        # Verifica cada link encontrado
        for link in links:
            href = link.get('href')
            if href:
                # Ignora links que começam com uma barra ("/")
                if not href.startswith('/'):
                    # Trata links que começam com '/'
                    if href.startswith('/'):
                        href = urljoin(url, href)

                    # Verifica se o link é um diretório
                    if href.endswith('/'):
                        diretorios.append(href)

        # Retorna a lista de diretórios
        return diretorios

    else:
        # Caso a requisição não tenha sido bem-sucedida, retorna uma lista vazia
        return []


# Exemplo de uso
url = input()  # Insira a URL desejada aqui
diretorios = obter_links_diretorios(url)

# Executa a função verificar_links para cada diretório encontrado
for diretorio in diretorios:
    diretorio_url = urljoin(url, diretorio)
    resultados = verificar_links(diretorio_url)

    # Imprime todos os links, seus status e a página onde estão vinculados
    for pagina, link, status in resultados:
        print(f'Página: {pagina}, Link: {link}, Status: {status}')
