import re

from util import database


def format_hostmask(inp):
    """format_hostmask -- Returns a nicks userhost"""
    return re.sub(r'(@[^@\.]+\d{2,}([^\.]?)+\.)', '*', inp.replace('@', '@@')).replace('~', '').replace('@@', '@').strip()


def get_hostmask(inp, db):
    """userhost -- Returns a nicks userhost"""
    if '@' in inp or '.' in inp:
        return inp
    nick = inp.strip().replace('~', '').lower()
    db_host = database.get(db, 'users', 'mask', 'nick', nick)
    if db_host is False:
        db_host = database.get(db, 'seen', 'host', 'name', nick)
    if db_host is False:
        db_host = nick

    # return format_hostmask(db_host)
    return db_host


def compare_hostmasks(hostmask, matchmasks):
    for mask in re.findall(r'(\b\S+\b)', matchmasks):
        mask = '^*{}$'.format(mask).replace('.', r'\.').replace('*', '.*')
        if bool(re.match(mask.lower(), hostmask.lower())):
            return True
    return False


def is_globaladmin(hostmask, chan, bot):
    globaladmins = ' '.join(bot.config.get('admins', []))
    if globaladmins:
        return compare_hostmasks(format_hostmask(hostmask), globaladmins)
    return False


def is_channeladmin(hostmask, chan, db):
    channeladmins = database.get(db, 'channels', 'admins', 'chan', chan)
    if channeladmins:
        return compare_hostmasks(format_hostmask(hostmask), channeladmins)
    return False


def is_admin(inp, chan, db, bot):
    if is_globaladmin(inp, chan, bot) or is_channeladmin(inp, chan, db):
        return True
    return False
