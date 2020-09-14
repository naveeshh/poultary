create table products(
    product_id serial primary key,
    product_name character varying NOT NULL,
    product_price float not null,
    product_details character varying,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    is_deleted BOOL DEFAULT 'f'
);


create table Orderdetails(
  orderdetails_id  serial primary key  not null,
	product_id int references products(product_id),
	created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	modified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	is_deleted BOOL DEFAULT 'f'


);

ALTER TABLE orderdetails
RENAME COLUMN orderdetails_id TO order_details_id;
alter table orderdetails add column quantity float not null,
add column actual_price float not null,
add column discount float not null;


alter table orderdetails rename to order_details;




alter table customers add column customer_details varchar,
add column customer_ph_num bigint,
add column created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
add column modified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
add column is_deleted BOOL DEFAULT 'f' ;

ALTER TABLE customers
RENAME COLUMN work_aera TO work_area;



delete from orders;
alter table orders add column order_status varchar not null,
add column created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
add column modified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
add column is_deleted BOOL DEFAULT 'f' ;

create table dailyproductprice(
    serial_no  serial primary key  not null,
	product_id int references products(product_id) not null,
	product_price int not null,
	created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	modified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	is_deleted BOOL DEFAULT 'f'
);

alter table dailyproductprice rename to daily_product_price;


