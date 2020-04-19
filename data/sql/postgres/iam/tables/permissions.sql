/**
 * permissions
 */
create table if not exists permissions (
    id bigserial,
    active boolean not null default true,
    name varchar(100) not null,
    constraint pk_permissions primary key (id),
    constraint u_permission_1 unique (name)
);

insert into permissions (name) values 
('admin.clients'),
('admin.security.permissions'),
('admin.security.roles'),
('user.authenticated')
on conflict do nothing;