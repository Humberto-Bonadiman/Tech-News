from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news_sorted = sorted(news, key=lambda x: x['comments_count'], reverse=True)
    return [
        (news['title'], news['url']) for news in news_sorted[:5]
    ]


# Requisito 11
def top_5_categories():
    news = find_news()

    news_categories = []
    for news in news:
        news_categories.append(news["category"])
    news_categories_counter = Counter(news_categories).most_common(5)

    categories_list = []
    for category in news_categories_counter:
        categories_list.append(category[0])
    return categories_list
