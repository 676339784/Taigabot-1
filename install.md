# taigabot dependencies
taigabot is ancient software that now runs on python 3 (only 3.9 or 3.10). it depends mostly on requests, beautifulsoup4 and lxml.

## instructions
see below for copypaste-friendly ubuntu/alpine instructions.

1. install python 3.9 or 3.10, pip and a compiler
2. clone this repo
3. make and activate a virtual environment
4. install and compile the requirements

    pip install -r requirements.txt
    pip install -r requirements_extra.txt

last step is to configure the bot:

    cp config.default config
    vi config

you can now run taigabot!

    python3 bot.py


### ubuntu
these instructions work for ubuntu 22.04. see older commits in this repo for ubuntu 21 and 18.

    # protip: update ur system
    sudo apt update
    sudo apt upgrade

    # lxml requirements
    sudo apt install build-essential libxml2-dev libxslt1-dev
    # system requirements
    sudo apt install git python3 python3-pip python3-venv

    # OPTIONAL: spellcheck plugin requirements (defaults to aspell english)
    sudo apt install libenchant-2-2 --no-install-suggests

    # download taigabot
    git clone https://github.com/inexist3nce/Taigabot.git Taigabot
    cd Taigabot

    # create and use a virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # install dependencies
    python3 -m pip install -r requirements.txt
    # OPTIONAL: install extra dependencies (means more plugins will work)
    python3 -m pip install -r requirements_extra.txt

    # edit the config file
    cp config.default config
    vi config

    # run the bot
    python3 bot.py


### alpine
TODO update this!!! its for python 2

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

- lxml
- requests
- beautifulsoup4

## details
these plugins are available after installing the main dependencies (`lxml`, `bs4` and `requests`):
- amazon
- bash
- booru
- choose
- coin
- coins
- debt
- dice
- dictionary
- distance
- distro
- fmylife
- geoip
- kernel
- lyrics
- radio
- religion
- translate
- twitch
- urbandict
- validate
- vimeo
- wordoftheday

## specific dependencies
some plugins need extra dependencies, you can read `requirements_extra.txt` for more info. theyre optional, without these the plugins simply wont load.

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

TODO document the other 30+ api keys
