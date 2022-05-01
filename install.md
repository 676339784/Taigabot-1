# taigabot dependencies
taigabot is ancient software that runs only on python 2.7. it depends mostly on requests, beautifulsoup4 and lxml.

the main piece of software, the irc bot, is more than 12 years old and some dependencies can't be found on repositories (ubuntu, pip or even github), so they've been bundled with the bot in this repository.

## instructions
see below for copypaste-friendly ubuntu/alpine instructions.

1. install python 2.7, pip and a compiler
2. clone (or download) this repo
3. make and activate a virtual environment
4. install and compile the dependencies

    pip2 install -r requirements.txt
    pip2 install -r requirements_extra.txt

last step is to configure the bot:

    cp config.default config
    vi config

you can now run taigabot!

    python2 bot.py


### ubuntu 18.04(?)
- python2.7 python-pip git
- build-essential python2.7-dev libxml2-dev libxslt1-dev

tldr:

    sudo apt-get install python2.7 python-pip git
    sudo apt-get install python2.7-dev build-essential libxml2-dev libxslt1-dev
    git clone https://github.com/inexist3nce/Taigabot.git
    cd Taigabot
    pip2 install virtualenv
    python2 -m virtualenv venv
    source venv/bin/activate
    pip2 install -r requirements.txt
    pip2 install -r requirements_extra.txt

### ubuntu 21.10
    # system essentials
    sudo apt install python2.7 wget git --no-install-suggests
    
    # build essentials
    sudo apt install build-essential python2.7-dev libxml2-dev libxslt1-dev zlib1g-dev
    
    # pip for py2
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
    python2.7 get-pip.py
    export PATH=~/.local/bin:$PATH
    python2.7 -m pip install virtualenv
    
    # get taigabot
    git clone https://github.com/inexist3nce/Taigabot.git
    cd Taigabot/
    
    # install pip dependencies in a virtualenv
    python2.7 -m virtualenv venv
    source venv/bin/activate
    python2.7 -m pip install -r requirements.txt
    # enchant is fucked in py2/ubuntu22
    sed -i 's/pyenchant.*$/#pyenchant/' requirements_extra.txt
    python2.7 -m pip install -r requirements_extra.txt
    
    # run the bot
    python2.7 bot.py

### alpine
- python2 py2-pip git
- gcc g++ libxml2 libxml2-dev libxslt-dev

tldr:

    apk add python2 py2-pip git gcc g++ python2-dev libxml2 libxml2-dev libxslt-dev
    python2 -m pip install virtualenv
    git clone https://github.com/inexist3nce/Taigabot.git
    cd Taigabot
    python2 -m virtualenv venv
    source venv/bin/activate
    export CFLAGS='-I/usr/include/python2.7/'
    python2 -m pip install -r requirements.txt


## python dependencies
you __need__ these to run plugins.

    pip install -r requirements.txt

- virtualenv
  - helps keep the trash contained. please use this.
- lxml
  - uses **3.3.6**
  - fastest way to parse html and xml
- requests
  - 2.23.0 works fine
- beautifulsoup4
  - 4.9.0 works fine

## details
these plugins need only the main dependencies (`lxml`, `bs4` and `requests`):
- amazon
- bash
- choose †
- coin †
- countdown †
- debt
- dice †
- dictionary
- distance
- distro
- drama
- fmylife
- furry
- geoip
- heartbleed †
- kernel
- potato †
- religion
- smileys †
- translate
- urbandict
- validate
- vimeo
- wordoftheday

†: no external dependencies

## specific dependencies
these specific plugins need a huge disgusting mess of dependencies:
- weather
  - urllib
  - requests
  - pytz
  - geopy
- google
  - requests
  - depends on `plugins/util/web.py` which depends on `http`, `urlnorm`, `json`, `urllib`
    - `http` depends on `cookielib`, `json`, `urllib`, `urllib2`, `urlparse`, `re`, `lxml`, `bs4`
  - i'm sorry
- wolframalpha
  - depends on `plugins/util/http.py` which depends on `cookielib`, `json`, `urllib`, `urllib2`, `urlparse`, `re`, `lxml`, `bs4`
- urls
  - re, urllib2, urlparse, requests, lxml, bs4, util.http
    - `util.http` = `cookielib`, `json`, `urllib`, `urllib2`, `urlparse`, `re`, `lxml`, `bs4`

## api keys
these plugins need an api key on the `config` file
| plugin       | key name           | where to find |
|--------------|--------------------|---------------|
| religion     | `"english_bible"`  | [link](https://api.esv.org/docs/) |
| weather      | `"darksky"`        | not possible to get anymore |
| wolframalpha | `"wolframalpha"`   | [link](https://products.wolframalpha.com/api/) |
| google       | `"google"`         | - |
| google       | `"google2"`        | - |
| google       | `"googleimage"`    | - |
| twitch       | `"twitch_client_id"` | [link](https://dev.twitch.tv/docs/api#step-1-register-an-application) |
| twitch       | `"twitch_client_secret"` | [link](https://dev.twitch.tv/docs/api#step-1-register-an-application) |
