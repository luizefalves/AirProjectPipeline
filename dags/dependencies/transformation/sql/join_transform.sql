DROP TABLE IF EXISTS transformation_table;
CREATE TABLE transformation_table (
  team_id INT PRIMARY KEY,
  team_name VARCHAR(255),
  conf_rank INT,
  team_division VARCHAR(255),
  div_rank INT,
  pts_rank INT,
  pts_pg FLOAT,
  reb_rank INT,
  reb_pg FLOAT,
  ast_rank INT,
  ast_pg FLOAT,
  opp_pts_rank INT,
  opp_pts_pg FLOAT
)
AS
  SELECT
    team_general.*,
    team_performance.team_name,
    team_performance.conf_rank,
    team_performance.team_division,
    team_performance.div_rank,
    team_performance.pts_rank,
    team_performance.pts_pg,
    team_performance.reb_rank,
    team_performance.reb_pg,
    team_performance.ast_rank,
    team_performance.ast_pg,
    team_performance.opp_pts_rank,
    team_performance.opp_pts_pg
  FROM team_general
  JOIN team_performance ON team_general.team_id = team_performance.team_id;
