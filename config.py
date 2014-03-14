from libstasis.entities import Column, types
from stasis import Configurator


config = Configurator()
config.include('pyramid_chameleon')
config.include('libstasis.entities')
config.include('libstasis.walker')
config.include('libstasis.rst')
config.add_entity_aspect(
    'title',
    Column('value', types.Unicode))
config.add_entity_aspect(
    'date',
    Column('value', types.DateTime))
config.add_entity_aspect(
    'body',
    Column('value', types.Unicode))
config.add_filesystem_walker('posts', 'content')
config.add_static_view('static', 'static')
config.add_route(
    'index',
    pattern='/index.html')
config.add_route(
    'yearlyarchive',
    pattern='/{year}/index.html',
    factory='__main__.factories.Archive')
config.add_route(
    'monthlyarchive',
    pattern='/{year}/{month}/index.html',
    factory='__main__.factories.Archive')
config.add_route(
    'dailyarchive',
    pattern='/{year}/{month}/{day}/index.html',
    factory='__main__.factories.Archive')
config.add_route(
    'post',
    pattern='/{year}/{month}/{day}/{name}.html',
    factory='__main__.factories.Post')
config.scan()
