import datetime
import re
import unicodedata


def normalize_string(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = s.encode('ascii', 'replace').replace('?', '')
    s = re.sub('[- \t\n\r]+', '-', s)
    allowed = frozenset('abcdefghijklmnopqrstuvwxyz0123456789-')
    return ''.join(x for x in s if x in allowed)


def blog_entries(registry):
    a = registry['entities'].aspects
    entities = registry['entities'].query(u'date', u'title', u'body', a.walker.name==u'posts')
    entries = {}
    for entity in entities:
        date = entity.date.value.date()
        key = frozenset(dict(
            year=unicode(date.year),
            month=u"%02i" % date.month,
            day=u"%02i" % date.day,
            name=normalize_string(entity.title.value)).items())
        entries[key] = entity
    return entries


class Archive(object):
    def __init__(self, request):
        self.request = request
        key = set(request.matchdict.items())
        entries = blog_entries(request.registry)
        self.items = [
            entries[x] for x in entries
            if key.issubset(x)]
        if request.matchdict:
            self.date = datetime.date(
                int(request.matchdict.get('year')),
                int(request.matchdict.get('month', 1)),
                int(request.matchdict.get('day', 1)))

    @classmethod
    def matches(cls, registry):
        return [dict(x) for x in blog_entries(registry).keys()]


class Post(object):
    def __init__(self, request):
        entries = blog_entries(request.registry)
        entry = entries[frozenset(request.matchdict.items())]
        self.title = entry['title'].value
        self.body = entry['body'].value

    @classmethod
    def matches(cls, registry):
        return [dict(x) for x in blog_entries(registry).keys()]
