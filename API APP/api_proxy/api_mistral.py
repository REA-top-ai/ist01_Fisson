import requests
from .api_methods import get_everything
from datetime import datetime, timedelta


def past_day_digest(news_api_key: str,
                    mistral_api_key: str,
                    q: str):

    # Получаем вчерашний день
    yesterday = str(datetime.now() - timedelta(days=1))[:10]

    # Получаем статьи за вчерашний день с помощью get_everything
    articles = get_everything(api_key=news_api_key,
                              q=q,
                              from_param=yesterday,
                              to=yesterday).get('articles')

    # Делаем строку для промта из заголовков
    all_news = ''
    for article in articles:
        title = article.get('title')
        # disc = article.get('discription')
        all_news += f'{title}' + ', '

    # Создаем промт
    promt = (
        "Ты аналитик новостей. "
        f"Составь отчет за последние 24 часа по заголовкам новостей: {all_news}. "
        "Отчёт должен состоять из от 250 до 300 слов на русском языке.")

    # Авторизация + отправляем запрос
    mistral_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {mistral_api_key}"}
    params = {"messages": [{"role": "user", "content": promt}],
              "model": "mistral-small-latest"}

    response = requests.post(url=mistral_url,
                             headers=headers,
                             json=params)
    # преобразовываем response в json
    result = response.json()
    # возвращаем ответ Mistral
    return result['choices'][0]['message']['content']