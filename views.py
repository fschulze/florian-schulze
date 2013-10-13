from pprint import pprint
from pyramid.compat import escape
from pyramid.view import view_config
import os


@view_config(
    route_name='index',
    renderer='templates/index.pt')
def index_view(context, request):
    return dict()


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
            items.append(dict(
                title=ob.title))
        return items

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
