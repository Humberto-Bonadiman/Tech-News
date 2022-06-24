from parsel import Selector
import requests
import time
from .database import create_news


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
    selector = Selector(html_content)
    url = selector.css("[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".post-meta .meta-date::text").get()
    writer = selector.css(".meta-author a::text").get()
    comments_count = selector.css(".comment-content::text").getall()
    list_summary = selector.css(
        "div.entry-content p:nth-child(2) *::text"
    ).getall()
    summary = ""
    for text in list_summary:
        summary += text
    tags = selector.css('[rel="tag"]::text').getall()
    category = selector.css(".meta-category .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": summary,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    request_fetch = fetch("https://blog.betrybe.com/")
    selector_scrape = scrape_novidades(request_fetch)
    all_news = []
    while len(selector_scrape) < amount:
        link_next_page = scrape_next_page_link(request_fetch)
        request_fetch = fetch(link_next_page)
        selector_scrape.extend(scrape_novidades(request_fetch))

    for link in selector_scrape[:amount]:
        new_request_fetch = fetch(link)
        get_data = scrape_noticia(new_request_fetch)
        all_news.append(get_data)

    create_news(all_news)
    return all_news
