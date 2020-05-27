-- esquema.sql
-- Toda definição de banco deverá ser feita nesse arquivo


drop table if exists posts;
create table posts (
  id integer primary key autoincrement,
  titulo string not null,
  autor string not null,
  texto string not null
);

drop table if exists presenca;
create table presenca (
  id integer primary key autoincrement,
  email string not null,
  presente BIT not null,
  resposta string not null,
  comentarios string
);