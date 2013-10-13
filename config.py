from stasis import Configurator


config = Configurator()
config.include('pyramid_chameleon')
config.include('stasis.rst')
config.add_static_view('static', 'static')
config.add_route(
    'index',
    pattern='/index.html')
config.add_route(
    'yearlyarchive',
    pattern='/{year:\d{4}}/index.html',
    factory='here.factories.Archive')
config.add_route(
    'monthlyarchive',
    pattern='/{year:\d{4}}/{month:\d{2}}/index.html',
    factory='here.factories.Archive')
config.add_route(
    'dailyarchive',
    pattern='/{year:\d{4}}/{month:\d{2}}/{day:\d{2}}/index.html',
    factory='here.factories.Archive')
config.add_route(
    'post',
    pattern='/{year:\d{4}}/{month:\d{2}}/{day:\d{2}}/{name}.html',
    traverse='/content/{year:\d{4}}-{month:\d{2}}-{day:\d{2}}-{name}.rst')
config.scan()
