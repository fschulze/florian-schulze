from babel.core import Locale
from operator import itemgetter
from factories import normalize_string
from pyramid.i18n import get_locale_name
from pyramid.view import view_config
from stasis.viewlet import viewlet_config


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

    @viewlet_config(
        'archive',
        factory='__main__.factories.Posts',
        renderer='templates/viewlets/archive.pt')
    def archive_viewlet(self):
        locale = Locale(get_locale_name(self.request))
        months = dict()
        for item in self.context.items.values():
            date = item.date.value
            key = (date.year, date.month)
            months[key] = months.get(key, 0) + 1
        items = []
        for year, month in sorted(months.keys(), reverse=True):
            count = months[(year, month)]
            url = self.request.relroute_path(
                'monthlyarchive',
                month="%02d" % month,
                year=year)
            items.append(dict(
                year=year,
                month=locale.months['stand-alone']['wide'][month],
                count=count,
                url=url))
        return dict(items=items)
