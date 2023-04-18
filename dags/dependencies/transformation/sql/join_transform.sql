DROP TABLE IF EXISTS transformation_table;
CREATE TABLE transformation_table AS
          SELECT
            team_general.*,
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