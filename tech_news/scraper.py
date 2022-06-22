from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        HEADER = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=HEADER, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    lista_links = []
    for card in selector.css(".cs-overlay-link"):
        links = card.css("a::attr(href)").get()
        lista_links.append(links)
    return lista_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    if not next_page_url:
        None
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
