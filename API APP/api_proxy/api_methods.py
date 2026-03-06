import requests

BASE_URL = 'https://newsapi.org/v2'
def _make_request(endpoint: str, api_key: str, params: dict[str, str] = None) -> dict[str, str]:
    url = f"{BASE_URL}/{endpoint}"
    default_params = {'apiKey': api_key}

    if params:
        default_params.update(params)
    try:
        response = requests.get(url, params=default_params, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Ошибка в запросе к NewsAPI ({endpoint}): {e}')
    except ValueError as e:
        raise Exception(f"Ошибка типа JSON: {e} ")


def get_top_headlines(api_key: str, q: str, country, category: str, sources: str, page_size: int) -> dict:
    allowed_params = {'apiKey': api_key, 'q': q, 'country': country, 'category': category, 'sources': sources, 'pageSize': page_size}
    params = {key: value for key, value in allowed_params.items() if value is not None}
    return _make_request(endpoint='top_headlines', api_key=api_key, params=params)



def get_everything(api_key:str, q:str=None, qintitle:str=None, sources:str=None, domains:str=None,
                   from_param:str=None, to:str=None, language:str=None, sort_by:str=None, page_size:int=None, page:int=None) -> dict:


    allowed_params = {
        'apikey': api_key,
        'q': q,
        'qInTitle': qintitle,
        'sources': sources,
        'domains': domains,
        'from': from_param,
        'to': to,
        'language': language,
        'sortBy': sort_by,
        'pageSize': page_size,
        'page': page
    }
    params = {key: value for key, value in allowed_params.items() if value is not None}
    return _make_request(endpoint='everything', api_key=api_key, params=params)



def sources(api_key:str, country:str=None, category:str=None, language:str=None) -> dict:

    allowed_params = {
        'apikey': api_key,
        'country': country,
        'category': category,
        'language': language
    }
    params = {key: value for key, value in allowed_params.items() if value is not None}
    return _make_request(endpoint='sources', api_key=api_key, params=params)



