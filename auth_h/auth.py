import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth


base_url = 'https://httpbin.org'


# 1
def basic_auth(user, passwd):
    url = f"{base_url}/basic-auth/{user}/{passwd}"

    res_basic = requests.get(url=url,
                             auth=HTTPBasicAuth(user, passwd),
                             timeout=2)

    return res_basic.status_code


# 2
def bearer_auth(token):
    url = f"{base_url}/bearer"
    headers = {"Authorization": f"Bearer {token}"}

    res_bearer = requests.get(url=url, headers=headers, timeout=2)

    return res_bearer.status_code


def digest_auth(qop, user, passwd):
    url = f"{base_url}/digest-auth/{qop}/{user}/{passwd}"

    res_digest = requests.get(url=url,
                              auth=HTTPDigestAuth(user, passwd),
                              timeout=2)

    return res_digest.status_code


print(basic_auth('Veronika', 'parolll'))
print(bearer_auth('my_top_secret'))
print(digest_auth('auth', 'Veronika', 'parolll1'))