/**
 * inventory management
 */
set schema 'inventory';


/** functions **/
\ir procs/categories/categories_all.sql
\ir procs/categories/category_add.sql

\ir procs/items/item_add.sql
\ir procs/items/item_update.sql

\ir procs/items/items_all.sql
\ir procs/items/items_by_name.sql
\ir procs/items/item_by_id.sql



set schema 'public';