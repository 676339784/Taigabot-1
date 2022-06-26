import requests
from json import loads as json_load

from urllib.parse import quote

# update this like once every few months
fake_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'


def urlencode(inp):
    return quote(inp)


def get_json(url: str, **kwargs):
    return json_load(get_text(url, **kwargs))


def get_html(url: str, **kwargs):
    return get(url, **kwargs)


def get_text(url: str, **kwargs):
    return get(url, **kwargs)


# HTTP GET
# this is probably the function that's used the most in internet-enabled plugins
# it sends an http GET via the "requests" library.
#
# future plugin writers: please use this method so you can easily swap the "backend"
# without replacing hundreds of lines of code all over the codebase
#
# it supports passing an object as the query string
# - example:  get('https://google.com/search', params={'q': 'hello world'})
# - result:   https://google.com/search?q=hello%20world
#
# u can also pass custom headers:
#    get('http://example.org', headers={'X-secret-key': 'hunter2'})
# a fake user-agent of a popular browser will be used if none is provided
#
def get(url: str, **kwargs):
    # accept custom headers
    if 'headers' in kwargs:
        headers = kwargs.pop('headers')
        # set a default user-agent if none was set
        if 'User-Agent' not in headers:
            headers['User-Agent'] = fake_ua
    else:
        headers = {'User-Agent': fake_ua}

    print(f"Running request: {url}")

    r = requests.get(url, headers=headers, timeout=8, **kwargs)
    return r.text


def post(url: str, **kwargs):
    if 'data' not in kwargs:
        return None

    # accept custom headers
    if 'headers' in kwargs:
        headers = kwargs.pop('headers')
        # set a default user-agent if none was set
        if 'User-Agent' not in headers:
            headers['User-Agent'] = fake_ua
    else:
        headers = {'User-Agent': fake_ua}

    r = requests.post(url, headers=headers, timeout=8, **kwargs)
    return r.text


# upload any text to pastebin
# please use this function so you don't have to modify 40 plugins when the api changes
def upload_paste(text: str, title: str = 'Paste', config={}):
    # sadly we need to pass bot.config because of the api keys
    api_key = config.get('api_keys', {}).get('pastebin', False)

    if api_key is False:
        return "no api key found, pls fix config"

    data = {
        'api_dev_key': api_key,
        'api_option': 'paste',
        'api_paste_code': text,
        'api_paste_name': title,
        'api_paste_private': 1,
        'api_paste_expire_date': '1D',
    }

    response = requests.post('https://pastebin.com/api/api_post.php', headers={'User-Agent': fake_ua}, data=data, timeout=12, allow_redirects=True)
    return response.text
