import logging
log = logging.getLogger(__name__)

import json

import pyramid.httpexceptions as exception
from pyramid.view import view_config, notfound_view_config, forbidden_view_config, exception_view_config
from pyramid.renderers import render


@view_config(
    route_name='home',
    renderer='saas.app:templates/default.html',
    request_method='GET'
)
def view_default(request):
    services = request.services()

    navigators = services['navigators']

    page_actions = services['page.actions']

    available = services['modules']
    modules = []
    for module_name, module in available.items():
        descriptor = module.getDescriptor()
        modules.append({
            'module_name': module_name,
            'help': descriptor['help'],
            'template': descriptor['template'],
            'icon': descriptor['icon']
        })

    return {
        'modules': modules,
        'navigators': navigators,
        'actions': page_actions
    }

@view_config(
    route_name='user.dashboard',
    renderer='saas.app:templates/dashboard.html',
    request_method='GET',
    permission='user.authenticated'
)
def view_dashboard(request):
    return {}