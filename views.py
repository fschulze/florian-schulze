from operator import itemgetter
from factories import normalize_string
from pyramid.view import view_config


@view_config(
    route_name='post',
    renderer='templates/post.pt')
def post_view(context, request):
    return dict(
        title=context.title,
        content=context.body)


class ArchiveView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def items(self):
        items = []
        for ob in self.context.items:
            date = ob['date'].value
            url = self.request.relroute_path(
                'post',
                year=date.year,
                month="%02d" % date.month,
                day="%02d" % date.day,
                name=normalize_string(ob['title'].value))
            items.append(dict(
                date=date,
                title=ob['title'].value,
                body=ob['body'].value,
                url=url))
        return sorted(items, key=itemgetter('date'), reverse=True)

    @view_config(
        route_name='index',
        renderer='templates/index.pt')
    def index_view(self):
        return dict(
            items=self.items()[:5])

    @view_config(
        route_name='yearlyarchive',
        renderer='templates/archive.pt')
    def yearlyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y"),
            items=self.items())

    @view_config(
        route_name='monthlyarchive',
        renderer='templates/archive.pt')
    def monthlyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y-%m"),
            items=self.items())

    @view_config(
        route_name='dailyarchive',
        renderer='templates/archive.pt')
    def dailyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y-%m-%d"),
            items=self.items())
