create table if not exists transaction_items (
    id uuid not null,
    transaction_id uuid not null,
    created_ts timestamp without time zone not null default(now() at time zone 'utc'),
    created_year smallint not null default extract(year from now()),
    client_id uuid not null,
    account_id uuid not null,
    debit decimal(12,4),
    credit decimal(12,4),
    constraint pk_transaction_items primary key (created_year, client_id, id),
    -- no duplicate account id in the same transaction
    constraint u_transaction_items_1 unique (created_year, client_id, id, account_id),
    constraint fk_transaction_items_1 foreign key (client_id)
        references clients.clients (id) on delete restrict on update restrict,
    constraint fk_transaction_items_2 foreign key (created_year, client_id, transaction_id)
        references accounting.transactions (created_year, client_id, id) on delete restrict on update restrict,
    -- debit should not be equal to credit, excludes debit = 0 and credit = 0
    constraint chk_transaction_items_1 check (debit <> credit),
    -- if debit has a value, credit should be null or 0
    -- if credit has a value, debit should be null or 0
    constraint chk_transaction_items_2 check (
        (debit > 0 and (credit is null or credit = 0))
        or (credit > 0 and (debit is null or debit = 0))
    )
)
partition by range (created_year);

-- default partition
create table if not exists transaction_items_default
partition of transaction_items default;