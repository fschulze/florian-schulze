from operator import itemgetter
from factories import normalize_string
from pyramid.view import view_config


def get_post_info(post, request):
    date = post['date'].value
    url = request.relroute_path(
        'post',
        year=date.year,
        month="%02d" % date.month,
        day="%02d" % date.day,
        name=normalize_string(post['title'].value))
    return dict(
        date=date,
        title=post['title'].value,
        url=url,
        body=post['body'].value)


@view_config(
    route_name='post',
    renderer='templates/post.pt')
def post_view(context, request):
    return get_post_info(context, request)


class ArchiveView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def items(self):
        items = []
        for ob in self.context.items:
            items.append(
                get_post_info(ob, self.request))
        return sorted(items, key=itemgetter('date'), reverse=True)

    @view_config(
        route_name='index',
        renderer='templates/index.pt')
    def index_view(self):
        return dict(
            items=self.items()[:5])

    @view_config(
        route_name='yearlyarchive',
        renderer='templates/index.pt')
    def yearlyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y"),
            items=self.items())

    @view_config(
        route_name='monthlyarchive',
        renderer='templates/index.pt')
    def monthlyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y-%m"),
            items=self.items())

    @view_config(
        route_name='dailyarchive',
        renderer='templates/index.pt')
    def dailyarchive_view(self):
        return dict(
            title=self.context.date.strftime("%Y-%m-%d"),
            items=self.items())
