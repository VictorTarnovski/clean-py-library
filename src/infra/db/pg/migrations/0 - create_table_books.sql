create table if not exists "books" (
  "id" uuid not null default uuid_generate_v4(),
  "name" varchar(50)
);