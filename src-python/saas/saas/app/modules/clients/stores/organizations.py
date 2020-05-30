import logging
log = logging.getLogger(__name__)

from uuid import UUID

from saas.app.core.services.connection import ConnectionManager
from saas.app.core.stores.base import BaseStore


class OrganizationsStore(BaseStore):

    def __init__(self, manager: ConnectionManager, name: str):
        super(OrganizationsStore, self).__init__(manager, name)

    def add(self, clientId: UUID, name: str, description: str):
        '''add organization to client
        '''
        try:
            [(result, )] = super(OrganizationsStore, self).runProcTransactional(
                'clients.organization_add', clientId, name, description)
            return result
        except Exception as e:
            log.error(e)
            raise Exception('Unable to add organization to client')


    def setParentOrg(self, clientId: UUID, orgId: UUID, parentOrgId: UUID):
        '''set parent organization id
        '''
        try:
            super(OrganizationsStore, self).runProcTransactional(
                'clients.organization_set_parent', [clientId, orgId, parentOrgId])
        except Exception as e:
            log.error(e)
            raise Exception('Unable to set parent organization id')