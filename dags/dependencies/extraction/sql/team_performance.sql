-- Create the team_performance table
DROP TABLE IF EXISTS team_performance;
CREATE TABLE team_performance (
    team_id INT NOT NULL PRIMARY KEY,
    team_name CHARACTER(14),
    conf_rank INT,
    team_division CHARACTER (10),
    div_rank INT,
    pts_rank INT,
    pts_pg FLOAT,
    reb_rank INT,
    reb_pg FLOAT,
    ast_rank INT,
    ast_pg FLOAT,
    opp_pts_rank INT,
    opp_pts_pg FLOAT
);

-- Insert data into the team_performance table from team_info_common
INSERT INTO team_performance (team_id, team_name, conf_rank, team_division, div_rank, pts_rank, pts_pg, reb_rank, reb_pg, ast_rank, ast_pg, opp_pts_rank, opp_pts_pg)
SELECT team_id,
    team_name,
    conf_rank,
    team_division,
    div_rank,
    pts_rank,
    pts_pg,
    reb_rank,
    reb_pg,
    ast_rank,
    ast_pg,
    opp_pts_rank,
    opp_pts_pg
FROM team_info_common;