-- settings.sql
CREATE DATABASE books;
CREATE USER booksuser
WITH PASSWORD 'books';
GRANT ALL PRIVILEGES ON DATABASE books TO booksuser;

