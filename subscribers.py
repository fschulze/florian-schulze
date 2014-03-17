from pyramid.events import subscriber
from pyramid.events import BeforeRender
from pyramid.renderers import get_renderer


@subscriber(BeforeRender)
def add_global(event):
    renderer = get_renderer("templates/master.pt")
    event['master'] = renderer.implementation().macros['master']
    renderer = get_renderer("templates/macros.pt")
    event['macros'] = renderer.implementation().macros
