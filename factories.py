import datetime


class Archive(object):
    def __init__(self, request):
        self.request = request
        root = self.request.root_node
        date = datetime.date(
            int(request.matchdict.get('year')),
            int(request.matchdict.get('month', 1)),
            int(request.matchdict.get('day', 1)))
        result = []
        for name in root['content']:
            ob = root['content'][name]
            ob_date = ob.metadata['date'].date()
            if 'day' not in request.matchdict:
                ob_date = ob_date.replace(day=1)
            if 'month' not in request.matchdict:
                ob_date = ob_date.replace(month=1)
            if ob_date == date:
                result.append(ob)
        self.date = date
        self.items = result

    @classmethod
    def matches(cls, root):
        matches = set()
        for name in root['content']:
            ob = root['content'][name]
            matches.add(ob.metadata['date'].date())
        matches = [
            dict(
                year=x.year,
                month="%02i" % x.month,
                day="%02i" % x.day)
            for x in matches]
        return matches
