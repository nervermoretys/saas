import logging
log = logging.getLogger(__name__)

def includeme(config):
    log.info('including: saas.app.modules.accounting.api')

    config.add_route(
        'api.accounting.accounts.types',
        '/api/accounting/accounts/types'
    )

    config.add_route(
        'api.accounting.accounts.add',
        '/api/accounting/accounts/add'
    )

    config.add_route(
        'api.accounting.accounts.assign.parent',
        '/api/accounting/accounts/parent/assign'
    )
    
    config.add_route(
        'api.accounting.accounts.all',
        '/api/accounting/accounts/all'
    )

    config.add_route(
        'api.accounting.accounts.children',
        '/api/accounting/accounts/children'
    )

    config.add_route(
        'api.accounting.account.tree',
        '/api/accounting/accounts/tree'
    )