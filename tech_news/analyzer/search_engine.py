from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    search_list = []
    for news in search:
        search_list.append((news["title"], news["url"]))
    return search_list


months = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}


# Requisito 7
def search_by_date(date):
    try:
        answer = []
        datetime.strptime(date, "%Y-%m-%d")
        month = date[5:7]
        day = date[8:10] if int(date[8:10]) >= 10 else date[9]
        extensive_date = f"{day} de {months[month]} de {date[0:4]}"
        search = search_news(
            {"timestamp": {"$regex": str(extensive_date), "$options": "i"}}
        )
        for index in search:
            answer.append(
                (index["title"], index["url"]),
            )
        return answer
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search = search_news(
        {"tags": {"$elemMatch": {"$regex": f"{tag}", "$options": "i"}}}
    )
    search_list = []
    for news in search:
        search_list.append((news["title"], news["url"]))
    return search_list


# Requisito 9
def search_by_category(category):
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    search_list = []
    for news in search:
        search_list.append((news["title"], news["url"]))
    return search_list
