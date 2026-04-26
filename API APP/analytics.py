from api_proxy.api_methods import get_everything
def top_50_filtered_news(q: str,
                         api_key: str) -> list:

    data = get_everything(q=q,
                          api_key=api_key,
                          sort_by="publishedAt",
                          page_size=100)

    articles = data.get('articles')
    valid_articles = []

    for art in articles:
        title = art.get('title')
        url = art.get('url')
        description = art.get('description')

        if title and url and len(description) >= 50:
            valid_articles.append({"title": art.get('title'),
                                   "source": art.get('source'),
                                   "published": art.get('publishedAt'),
                                   "author": art.get('author')})

        if len(valid_articles) == 50:
            break
    return valid_articles