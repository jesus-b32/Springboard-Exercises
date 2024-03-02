-- from the terminal run:
-- psql < medical_center.sql

DROP DATABASE IF EXISTS soccer_league;

CREATE DATABASE soccer_league;

\c soccer_league

CREATE TABLE teams 
(
  id SERIAL PRIMARY KEY,
  team_name TEXT NOT NULL,
  city TEXT
);

INSERT INTO teams 
  (team_name, city)
VALUES
  ('hell divers', 'super Earth'),
  ('usa', 'Earth');

CREATE TABLE referees
(
  id SERIAL PRIMARY KEY,
  referee_name TEXT NOT NULL
);

INSERT INTO referees
  (referee_name)
VALUES
  ('Jennifer'),
  ('Jim');


CREATE TABLE players
(
  id SERIAL PRIMARY KEY,
  player_name TEXT,
  team_id INTEGER REFERENCES teams ON DELETE SET NULL
);

INSERT INTO players

  (player_name, team_id)
VALUES
  ('John Doe', 1);




  
CREATE TABLE season
(
  id SERIAL PRIMARY KEY,
  season_start DATE NOT NULL,
  season_end DATE

);

INSERT INTO season
  (season_start, season_end)
VALUES
  ('03/01/2024', '05/01/2024');




CREATE TABLE matches
(
  id SERIAL PRIMARY KEY,
  home_team_id INTEGER REFERENCES teams ON DELETE SET NULL,
  away_team_id INTEGER REFERENCES teams ON DELETE SET NULL,
  match_location TEXT,
  match_date DATE,
  start_time TIME,
  refereer1_id INTEGER REFERENCES referees ON DELETE SET NULL,
  refereer2_id INTEGER REFERENCES referees ON DELETE SET NULL,
  season_id INTEGER REFERENCES season ON DELETE SET NULL

);

INSERT INTO matches
  (home_team_id, away_team_id, match_location, match_date, start_time, refereer1_id, refereer2_id, season_id)
VALUES
  (1, 2, 'LA', '03/01/2024', '08:30:00', 1, 2, 1);


CREATE TABLE goals
(
  id SERIAL PRIMARY KEY,
  player_id INTEGER REFERENCES players ON DELETE SET NULL,
  match_id INTEGER REFERENCES matches ON DELETE SET NULL

);

INSERT INTO goals
  (player_id, match_id)
VALUES
  (1,1);



CREATE TABLE lineups
(
  id SERIAL PRIMARY KEY,
  player_id INTEGER REFERENCES players ON DELETE SET NULL,
  match_id INTEGER REFERENCES matches ON DELETE SET NULL,
  team_id INTEGER REFERENCES teams ON DELETE SET NULL
);

INSERT INTO lineups
  (player_id, match_id, team_id)
VALUES
  (1,1,1);


CREATE TABLE results
(
  id SERIAL PRIMARY KEY,
  match_id INTEGER REFERENCES matches ON DELETE SET NULL,
  team_id INTEGER REFERENCES teams ON DELETE SET NULL,
  match_result TEXT
);

INSERT INTO results
  (match_id, team_id, match_result)
VALUES
  (1,1, 'win');