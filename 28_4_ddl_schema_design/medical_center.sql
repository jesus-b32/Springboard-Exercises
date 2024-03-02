-- from the terminal run:
-- psql < medical_center.sql

DROP DATABASE IF EXISTS medical_center;

CREATE DATABASE medical_center;

\c medical_center

CREATE TABLE doctors
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  specialty TEXT NOT NULL
);

INSERT INTO doctors
  (first_name, last_name, specialty)
VALUES
  ('John', 'Doe', 'Family Physicians'),
  ('Jane', 'Smith', 'Cardiologists'),
  ('Cory', 'Squibbes', 'Dermatologists');

CREATE TABLE patients
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  sex TEXT NOT NULL,
  birthday DATE NOT NULL,
  insurance TEXT NOT NULL
);

INSERT INTO patients
  (first_name, last_name, sex, birthday, insurance)
VALUES
  ('Jennifer', 'Finch', 'female', '04-15-1997', 'Anthem'),
  ('Thadeus', 'Gathercoal', 'male', '09-05-1994', 'United Healthcare'),
  ('Sonja', 'Pauley', 'female', '05-30-1987', 'Kaiser Permanente');


CREATE TABLE visits
(
  id SERIAL PRIMARY KEY,
  doctor_id INTEGER REFERENCES doctors ON DELETE SET NULL,
  patient_id INTEGER REFERENCES patients ON DELETE SET NULL,
  visit_date DATE NOT NULL
);

INSERT INTO visits

  (doctor_id, patient_id, visit_date)
VALUES
  (1, 1, '04-15-2023'),
  (1, 2, '08-19-2023'),
  (3, 3, '06-15-2023'),
  (2, 1, '02-08-2023'),
  (2, 3, '12-15-2023');




  
CREATE TABLE diseases
(
  id SERIAL PRIMARY KEY,
  disease_name TEXT NOT NULL,
  disease_description TEXT
);

INSERT INTO diseases
  (disease_name, disease_description)
VALUES
  ('flu', ''),
  ('covid-19', ''),
  ('chicken pox', ''),
  ('heart disease', '');  






CREATE TABLE diagnoses
(
  id SERIAL PRIMARY KEY,
  visit_id INTEGER REFERENCES visits ON DELETE SET NULL,
  disease_id INTEGER REFERENCES diseases ON DELETE SET NULL,
  notes TEXT
);

INSERT INTO diagnoses
  (visit_id, disease_id, notes)
VALUES
  (1, 1, ''),  
  (2, 1, ''),  
  (3, 2, ''),  
  (4, 4, '');  