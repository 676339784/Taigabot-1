import re

from util import hook
from utilities import formatting, request, services

API_URL = 'https://www.googleapis.com/customsearch/v1'


@hook.command('search')
@hook.command('g')
@hook.command
def google(inp, bot):
    """google <query> -- Returns first google search result for <query>."""
    inp = request.urlencode(inp)

    url = API_URL + '?key={}&cx={}&num=1&safe=off&q={}'
    cx = bot.config['api_keys']['googleimage']
    search = '+'.join(inp.split())
    key = bot.config['api_keys']['google']
    result = request.get_json(url.format(key, cx, search))['items'][0]

    title = result['title']
    content = formatting.remove_newlines(result['snippet'])
    link = result['link']

    try:
        return '{} -- \x02{}\x02: "{}"'.format(services.shorten(link), title, content)
    except Exception:
        return '{} -- \x02{}\x02: "{}"'.format(link, title, content)


@hook.regex(r'^\>(.*\.(gif|jpe?g|png|tiff|bmp))$', re.I)
@hook.command('gi')
def image(inp, bot):
    """image <query> -- Returns the first Google Image result for <query>."""
    if type(inp) is str:
        filetype = None
    else:
        inp, filetype = inp.string[1:].split('.')

    cx = bot.config['api_keys']['googleimage']
    search = '+'.join(inp.split())
    key = bot.config['api_keys']['google']

    if filetype:
        url = API_URL + '?key={}&cx={}&searchType=image&num=1&safe=off&q={}&fileType={}'
        result = request.get_json(url.format(key, cx, search.encode('utf-8'),
                                             filetype))['items'][0]['link']
    else:
        url = API_URL + '?key={}&cx={}&searchType=image&num=1&safe=off&q={}'
        result = request.get_json(url.format(key, cx, search.encode('utf-8')))['items'][0]['link']

    return services.shorten(result)
