create or replace function location_get(
    p_client_id clients.clients.id%type,
    p_location_id inventory.locations.id%type
)
returns table (
    location_id inventory.locations.id%type,
    facility_id inventory.facilities.id%type,
    name inventory.locations.name%type,
    floor_id inventory.locations.floor_id%type,
    aisle_id inventory.locations.aisle_id%type,
    area_id inventory.locations.area_id%type,
    section_id inventory.locations.section_id%type,
    shelf_id inventory.locations.shelf_id%type,
    rack_id inventory.locations.rack_id%type,
    level_id inventory.locations.level_id%type,
    bin_id inventory.locations.bin_id%type
)
as $$
begin
    return query
    select
        a.id,
        a.facility_id,
        a.name,
        a.floor_id,
        a.aisle_id,
        a.area_id,
        a.section_id,
        a.shelf_id,
        a.rack_id,
        a.level_id,
        a.bin_id
    from inventory.locations a
    where a.client_id = p_client_id
        and a.id = p_location_id;
end
$$
language plpgsql
stable;