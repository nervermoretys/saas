/**
 * retrieve all clients
 */
create or replace function clients_all ()
returns table (
    id clients.clients.id%type,
    active clients.clients.active%type,
    name clients.clients.name%type,
    address clients.clients.address%type,
    country_id clients.clients.country_id%type
)
as $$
begin
    return query
    select
        a.id,
        a.active,
        a.name,
        a.address,
        a.country_id
    from clients.clients a;
end
$$
language plpgsql
stable;