import logging
log = logging.getLogger(__name__)

from saas.app.core.services.connection import ConnectionManager
from saas.app.core.stores.base import BaseStore, StoreException

from uuid import UUID


class LocationStore(BaseStore):

    def __init__(self, manager: ConnectionManager, name: str):
        super(LocationStore, self).__init__(manager, name)

    def add(self, 
        client_id: UUID, 
        location_id: UUID, 
        facility_id: UUID, 
        name: str, 
        floor_id: str, 
        aisle_id: str, 
        area_id: str,
        section_id: str,
        shelf_id: str, 
        rack_id: str, 
        level_id: str, 
        bin_id: str) -> None:
        try:
            super(LocationStore, self).runProcTransactional('inventory.location_add', [
                client_id, 
                location_id, 
                facility_id,
                name,
                floor_id, 
                aisle_id, 
                area_id,
                section_id,
                shelf_id, 
                rack_id, 
                level_id, 
                bin_id
            ])
        except Exception as e:
            log.error(e)
            raise StoreException('Unable to add inventory location')

    def update(self, 
        client_id: UUID, 
        location_id: UUID, 
        facility_id: UUID, 
        name: str, 
        floor_id: str, 
        aisle_id: str, 
        area_id: str,
        section_id: str,
        shelf_id: str, 
        rack_id: str, 
        level_id: str, 
        bin_id: str) -> None:
        try:
            super(LocationStore, self).runProcTransactional('inventory.location_update', [
                client_id, 
                location_id, 
                facility_id,
                name,
                floor_id, 
                aisle_id, 
                area_id,
                section_id,
                shelf_id, 
                rack_id, 
                level_id, 
                bin_id
            ])
        except Exception as e:
            log.error(e)
            raise StoreException('Unable to update inventory location')

    def get(self, client_id: UUID, location_id: UUID) -> {}:
        try:
            result = super(LocationStore, self).runProc('inventory.location_get', [
                client_id,
                location_id
            ])
            if len(result) > 0:
                return result[0]
            else:
                raise StoreException('No location found')
        except Exception as e:
            log.error(e)
            raise StoreException('Unable to retrieve location')

    def filter(self, client_id: UUID, filter: str) -> []:
        try:
            # result = super(LocationStore, self).runProc('inventory.location_fiter', [
            #     str(client_id),
            #     f"%{filter}%"
            # ])
            result = super(LocationStore, self).execute(
                'select * from inventory.location_filter(%(client_id)s,%(filter)s)',
                { 
                    'client_id': client_id, 
                    'filter': f'%{filter}%'
                }
            )
            return result
        except Exception as e:
            log.error(e)
            raise StoreException('Unable to retrieve filtered list of location')