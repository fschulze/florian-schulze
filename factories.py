from stasis.rst import RstNode
import datetime
import re
import unicodedata


def normalize_string(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = s.encode('ascii', 'replace').replace('?', '')
    s = re.sub('[- \t\n\r]+', '-', s)
    allowed = frozenset('abcdefghijklmnopqrstuvwxyz0123456789-')
    return ''.join(x for x in s if x in allowed)


def blog_entries(root):
        entries = {}
        for name in root:
            ob = root[name]
            if not isinstance(ob, RstNode):
                continue
            date = ob.metadata['date'].date()
            key = frozenset(dict(
                year=unicode(date.year),
                month=u"%02i" % date.month,
                day=u"%02i" % date.day,
                name=normalize_string(ob.title)).items())
            entries[key] = ob
        return entries


class Archive(object):
    def __init__(self, request):
        self.request = request
        key = set(request.matchdict.items())
        entries = blog_entries(request.registry['virtualroot'])
        self.items = [
            entries[x] for x in entries
            if key.issubset(x)]
        self.date = datetime.date(
            int(request.matchdict.get('year')),
            int(request.matchdict.get('month', 1)),
            int(request.matchdict.get('day', 1)))

    @classmethod
    def matches(cls, root):
        return [dict(x) for x in blog_entries(root).keys()]

class Post(object):
    def __init__(self, request):
        entries = blog_entries(request.registry['virtualroot'])
        entry = entries[frozenset(request.matchdict.items())]
        self.title = entry.title
        self.body = entry.body

    @classmethod
    def matches(cls, root):
        return [dict(x) for x in blog_entries(root).keys()]
