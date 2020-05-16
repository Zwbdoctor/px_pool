import requests


def get_page(url, headers=None, **kwargs):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    if headers:
        header.update(headers)
    try:
        resp = requests.get(url, headers=header, **kwargs)
    except:
        return None
    return resp.text
