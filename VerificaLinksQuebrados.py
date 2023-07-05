import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin


def verificar_links(url):
    # Faz a requisição GET para a página
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontra todos os elementos <a> na página
        links = soup.find_all('a')
        
        # Lista para armazenar os links, status e páginas
        resultados = []
        
        # Verifica cada link encontrado
        for link in links:
            href = link.get('href')
            if href:
                # Trata links que começam com '/'
                if href.startswith('/'):
                    href = urljoin(url, href)
                
                # Trata links que terminam com '#'
                if href.endswith('#'):
                    href = href[:-1]
                
                # Ignora links com esquemas não suportados
                if href.startswith('http://') or href.startswith('https://'):
                    # Codifica corretamente os caracteres especiais no link
                    href_encoded = quote(href, safe='/:?#=&')
                    
                    # Combina o link com o URL base para lidar com URLs relativas
                    link_url = urljoin(url, href_encoded)
                    
                    # Faz uma nova requisição GET para o link
                    link_response = requests.get(link_url)
                    
                    # Adiciona o link, status e página à lista de resultados
                    resultados.append((url, href, link_response.status_code))
                    
                    # Verifica se o link é um subdiretório e chama a função recursivamente
                    if href.startswith(url):
                        verificar_links(href)
        
        # Retorna a lista de resultados
        return resultados
    
    else:
        # Caso a requisição não tenha sido bem-sucedida, retorna uma lista vazia
        return []


# Exemplo de uso
url = 'https://fgts.gov.br'  # Insira a URL desejada aqui
resultados = verificar_links(url)

# Imprime todos os links, seus status e a página onde estão vinculados
for pagina, link, status in resultados:
    print(f'Página: {pagina}, Link: {link}, Status: {status}')
