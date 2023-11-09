/* CREATE TABLE SHELVES */

create extension if not exists "uuid-ossp";

create table if not exists "shelves" (
  "id" uuid not null default uuid_generate_v4(),
  "name" varchar(50)
);