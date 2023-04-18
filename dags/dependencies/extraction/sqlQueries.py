team_details_drop = "DROP TABLE IF EXISTS team_details CASCADE"
team_history_drop = "DROP TABLE IF EXISTS team_history CASCADE"
team_info_common_drop = "DROP TABLE IF EXISTS team_info_common CASCADE"


team_details_create = """CREATE TABLE team_details(
   team_id            INTEGER  NOT NULL PRIMARY KEY 
  ,abbreviation       VARCHAR(3) NOT NULL
  ,nickname           VARCHAR(13) NOT NULL
  ,yearfounded        INTEGER  NOT NULL
  ,city               VARCHAR(13) NOT NULL
  ,arena              VARCHAR(26) NOT NULL
  ,arenacapacity      INTEGER  NOT NULL
  ,owner              VARCHAR(35) NOT NULL
  ,generalmanager     VARCHAR(18) NOT NULL
  ,headcoach          VARCHAR(16) NOT NULL
  ,dleagueaffiliation VARCHAR(33) NOT NULL
  ,facebook           VARCHAR(41) NOT NULL
  ,instagram          VARCHAR(37) NOT NULL
  ,twitter            VARCHAR(35) NOT NULL
)"""

team_history_create = """CREATE TABLE team_history(
   team_id          INTEGER  NOT NULL 
  ,city             VARCHAR(25) NOT NULL
  ,nickname         VARCHAR(13) NOT NULL
  ,year_founded     INTEGER  NOT NULL
  ,year_active_till INTEGER  NOT NULL
  ,PRIMARY KEY (team_id, year_founded)
  ,FOREIGN KEY (team_id) REFERENCES team_details (team_id)
)"""

team_info_common_create = """CREATE TABLE team_info_common(
   team_id           INTEGER  NOT NULL PRIMARY KEY 
  ,season_year       VARCHAR(7) NOT NULL
  ,team_city         VARCHAR(13) NOT NULL
  ,team_name         VARCHAR(13) NOT NULL
  ,team_abbreviation VARCHAR(3) NOT NULL
  ,team_conference   VARCHAR(4) NOT NULL
  ,team_division     VARCHAR(9) NOT NULL
  ,team_code         VARCHAR(12) NOT NULL
  ,team_slug         VARCHAR(12) NOT NULL
  ,w                 INTEGER  NOT NULL
  ,l                 INTEGER  NOT NULL
  ,pct               NUMERIC(5,3) NOT NULL
  ,conf_rank         INTEGER  NOT NULL
  ,div_rank          INTEGER  NOT NULL
  ,min_year          INTEGER  NOT NULL
  ,max_year          INTEGER  NOT NULL
  ,league_id         INTEGER  NOT NULL
  ,season_id         INTEGER  NOT NULL
  ,pts_rank          INTEGER  NOT NULL
  ,pts_pg            NUMERIC(5,1) NOT NULL
  ,reb_rank          INTEGER  NOT NULL
  ,reb_pg            NUMERIC(4,1) NOT NULL
  ,ast_rank          INTEGER  NOT NULL
  ,ast_pg            NUMERIC(4,1) NOT NULL
  ,opp_pts_rank      INTEGER  NOT NULL
  ,opp_pts_pg        NUMERIC(5,1) NOT NULL
)"""

create_table_queries = [team_details_create,team_history_create,team_info_common_create]
drop_table_queries = [team_details_drop,team_history_drop,team_info_common_drop]
tableNames = ['team_details','team_history','team_info_common']