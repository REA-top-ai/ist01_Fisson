# import pprint
# from api_proxy.api_methods import get_everything
# from analytics.article_analytic import top_50_filtered_news
from api_proxy.api_mistral import past_day_digest


if __name__ == '__main__':
    # News API analitics report
    # result = get_everything(q="apple",
    # api_key="eb06bb24ef204dee8e6463bd4e5d6a78", language="ru")

    # Задание на аналитику статей
    # result1 = top_50_filtered_news(q="apple",
    #                                api_key="eb06bb24ef204dee8e6463bd4e5d6a78")
    # pprint.pprint(result1)

    # Задание на AI Client(краткая выжимка из статей за вчерашний день)
    news_api_key = "2fcb77a9f625451295d1d6552f524dd6"
    mistral_api_key = "YK2FdsUsm3qgCa8YLFoEODhT6TTjCHKp"
    news_topic = 'Apple'
    report = past_day_digest(news_api_key, mistral_api_key, news_topic)

    with open("report_from_news_titles.txt", "w", encoding="utf-8") as f:
        f.write(report)