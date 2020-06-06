import logging
log = logging.getLogger(__name__)

from saas.app.core.services import get_service
from saas.app.modules.admin.module import AdminModule


def includeme(config):
    log.info('including: saas.app.modules.admin')

    config.include('saas.app.modules.admin.stores')
    config.include('saas.app.modules.admin.views')
    config.include('saas.app.modules.admin.views.api')

    services = get_service(None)
    modules = services['modules']
    modules['admin'] = AdminModule()

    navigators = services['navigators']
    navigators['admin'] = {
        'title': 'System Administration',
        'help': 'Manage clients, users and roles',
        'icon': '<span class="material-icons">view_quilt</span>',
        'template': 'saas.app.modules.admin:templates/module.html'
    }