# Lista Links - Documentação

Este repositório contém um código em Python que permite verificar links quebrados em um site. Ele analisa todas as páginas de um site e verifica a validade dos links, informando quais links estão quebrados e em quais páginas eles estão alocados.

## Como usar

Para utilizar o código fornecido neste repositório, siga as etapas abaixo:

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/davidjeiel/lista-links.git
```

2. Certifique-se de ter o Python 3 instalado em seu sistema.

3. Instale as dependências necessárias, como o módulo `beautifulsoup4`, usando o gerenciador de pacotes `pip`:

```bash
pip install beautifulsoup4
```

4. Navegue até o diretório do projeto e execute o script `lista_links.py` informando a URL que deseja verificar:

```bash
cd lista-links
python lista_links.py https://www.example.com
```

Substitua `https://www.example.com` pela URL do site que deseja verificar.

## Funcionamento

O código irá iniciar a verificação da URL informada, analisando todas as páginas do site e os links presentes em cada página. Para cada link encontrado, será feita uma requisição HTTP para verificar o status do link. Os links com status diferente de 200 serão considerados quebrados e serão listados no resultado.

## Exemplo de saída

A saída do código irá apresentar os links quebrados encontrados, juntamente com as páginas em que estão alocados e o status de cada link. Por exemplo:

```
Página: https://www.example.com/pagina1, Link: https://www.example.com/link-quebrado, Status: 404
Página: https://www.example.com/pagina2, Link: https://www.example.com/outro-link-quebrado, Status: 404
Página: https://www.example.com/pagina3, Link: https://www.example.com/mais-um-link-quebrado, Status: 404
```

## Observações

- Certifique-se de ter uma conexão estável com a internet, pois o código fará várias requisições HTTP para verificar os links.
- O código verificará todos os links encontrados, incluindo links externos. Se você quiser limitar a verificação apenas aos links internos do site, você pode fazer uma modificação no código para verificar a URL base e ignorar os links externos.

## Contribuição

Se você encontrar problemas, bugs ou quiser contribuir para este projeto, sinta-se à vontade para abrir um "issue" ou enviar um "pull request" para o repositório.

## Licença

Este projeto está sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
