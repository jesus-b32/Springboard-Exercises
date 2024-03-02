-- from the terminal run:
-- psql < medical_center.sql

DROP DATABASE IF EXISTS craigslist;

CREATE DATABASE craigslist;

\c craigslist

CREATE TABLE region 
(
  id SERIAL PRIMARY KEY,
  region_name TEXT NOT NULL
);

INSERT INTO region 
  (region_name)
VALUES
  ('LA'),
  ('San Francisco'),
  ('New York City');

CREATE TABLE users
(
  id SERIAL PRIMARY KEY,
  user_name TEXT NOT NULL,
  user_password TEXT NOT NULL,
  preffered_region_id INTEGER REFERENCES region ON DELETE SET NULL
);

INSERT INTO users
  (user_name, user_password, preffered_region_id)
VALUES
  ('Jennifer', 'password', 1),
  ('Thadeus', 'password1', 1),
  ('Sonja', 'password2', 3);


CREATE TABLE category
(
  id SERIAL PRIMARY KEY,
  category_name TEXT
);

INSERT INTO category

  (category_name)
VALUES
  ('books'),
  ('electronics'),
  ('tools'),
  ('video games');




  
CREATE TABLE posts
(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  post_text TEXT,
  locaton TEXT,
  category_id INTEGER REFERENCES category ON DELETE SET NULL,
  region_id INTEGER REFERENCES region ON DELETE SET NULL,
  user_id INTEGER REFERENCES users ON DELETE SET NULL

);

INSERT INTO posts
  (title, post_text, locaton, category_id, region_id, user_id)
VALUES
  ('iPhone 15', 'Refurbished iPhone 15 in great working condition', 'Passedena', 2, 1, 1);