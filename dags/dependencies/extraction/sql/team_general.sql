-- Create the team_general table
    DROP TABLE IF EXISTS team_general;
    CREATE TABLE team_general (
        team_id            SERIAL PRIMARY KEY,
        abbreviation       VARCHAR(3) NOT NULL,
        city               VARCHAR(13) NOT NULL,
        arena              VARCHAR(26) NOT NULL,
        generalmanager     VARCHAR(18) NOT NULL,
        headcoach          VARCHAR(16) NOT NULL,
        instagram          VARCHAR(37) NOT NULL
    );


-- Insert data into the team_performance table from team_details
    INSERT INTO team_general (team_id, abbreviation, city, arena, generalmanager, headcoach, instagram)
    SELECT team_id,
        abbreviation,
        city,
        arena,
        generalmanager,
        headcoach,
        instagram
    FROM team_details;