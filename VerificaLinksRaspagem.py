from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def get_link_info(url):
    driver = webdriver.Chrome('/lib/chromedriver.exe')
    driver.get(url)

    link_infos = []
    elements = driver.find_elements(By.TAG_NAME, 'a')

    for element in elements:
        href = element.get_attribute('href')
        if href:
            link_info = {
                'page_url': driver.current_url,
                'link_url': href,
                'status_code': get_status_code(href)
            }
            link_infos.append(link_info)

    driver.quit()
    return link_infos

def get_status_code(url):
    response = requests.head(url)
    return response.status_code

# Exemplo de uso
url = 'https://www.example.com'
link_infos = get_link_info(url)

for link_info in link_infos:
    print('Página: ', link_info['page_url'])
    print('Link: ', link_info['link_url'])
    print('Status HTTP: ', link_info['status_code'])
    print()
