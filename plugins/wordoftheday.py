# word of the day plugin by ine (2020)
# checked 04/2022
from util import hook
from utilities import request, iterable
from bs4 import BeautifulSoup


@hook.command()
def wordoftheday(inp):
    html = request.get('https://www.merriam-webster.com/word-of-the-day')
    soup = BeautifulSoup(html)

    word = soup.find('div', attrs={'class': 'word-and-pronunciation'}).find('h1').text
    paragraphs = soup.find('div', attrs={'class': 'wod-definition-container'}).find_all('p')

    definitions = []

    for paragraph in iterable.limit(4, paragraphs):
        definitions.append(paragraph.text.strip())

    definitions = '; '.join(definitions)
    output = f'The word of the day is \x02{word}\x02: {definitions}'

    if len(output) > 300:
        output = output[:300] + '... More at https://www.merriam-webster.com/word-of-the-day'

    return output
