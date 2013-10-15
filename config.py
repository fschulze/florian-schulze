from stasis import Configurator
from stasis.entities import Column, types
from stasis.node import Node


config = Configurator()
config.include('pyramid_chameleon')
config.include('stasis.entities')
config.include('stasis.walker')
config.include('stasis.rst')
config.add_entity_aspect(
    'title',
    Column('title', types.Unicode))
config.add_entity_aspect(
    'date',
    Column('date', types.DateTime))
config.add_entity_aspect(
    'body',
    Column('body', types.Unicode))
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
