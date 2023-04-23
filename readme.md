
# THIS README FILE IS NOT COMPLETE
This project was made for Docker version >= 20.10.16
### START WITH "python project_starter.py"
----------------------
# AirProjectPipeline

This is a sample project to illustrate an Airflow DAG pipeline using Docker.

## Overview

The project includes:

- Docker Compose configuration file to run a PostgreSQL database, an Airflow webserver, an Airflow scheduler,a Flower instance for monitoring tasks and a Flask REST API .
- A DAG pipeline with three tasks:
  - `database_ingestion` task creates a table from csv NBA dataset in the PostgreSQL database.
  - `extracting_data` extract data into new tables.
  - `postgres_transform_data` join the extracted tables into a final table
  - `flask_container_build` creates a REST API with Flask to list the data to the final user
- A `requirements.txt` file containing the necessary Python dependencies for the DAG.

The project is based on a set of csv tables made available on Kaggle:
draft_combine_stats, draft_history, game, game_info, game_summary, inactive_players, line_score, officials, other_stats, play_by_play, player, team, team_details, team_history, team_info_common.

From these tables, a sample of three tables is used for data extraction: team_details, and team_info_common.

The team_general table was created from the team_details table, and the team_performance table was created from the team_info_common table. This allowed for the extraction of general team data and performance information.

In the transformation stage, these tables were combined into a third table called transformation_table. This table contains the necessary information for the queries that will be made by the API and displayed in the browser.

## Usage

To run the project, follow these steps:

1. Clone the repository: `git clone https://github.com/luizefalves/AirProjectPipeline.git`
2. Navigate to the project directory: `cd AirProjectPipeline`
3. Run the setup script: `python project_starter.py`
4. Monitor the DAG in the Airflow webserver if you want: `http://localhost:8080`
5. Open the API in your web browser: `http://localhost:8081/`


## Dataset Columns Details    
-------------------  NOT DONE YET ---------------------
### You can check the official NBA's statistical terms glossary here: `https://www.nba.com/stats/help/glossary`


    div_rank - This is a ranking of the team within its division based on its win-loss record compared to other teams in the same division. The NBA has six divisions, and each division has five teams.

    pts_rank - This is a ranking of the team's scoring offense based on the average number of points the team scores per game. The ranking is determined by comparing the team's scoring average to that of other teams in the league.

    conf_rank - This is a ranking of the team's win-loss record compared to other teams in its conference. The NBA has two conferences, the Eastern Conference and the Western Conference, and each conference has 15 teams.

    ast_rank - This is a ranking of the team's ability to generate assists, which is a measure of how well the team shares the ball and creates scoring opportunities for teammates. The ranking is determined by comparing the team's average number of assists per game to that of other teams in the league.

    opp_pts_rank - This is a ranking of the team's defensive performance based on the average number of points the team allows its opponents to score per game. The ranking is determined by comparing the team's opponents' scoring average to that of other teams in the league.

Each of these metrics provides a different perspective on a team's performance and can be used to compare a team's performance to that of other teams in the league. It's worth noting that these metrics are just a few of many that can be used to evaluate NBA teams, and that a comprehensive evaluation of a team's performance should take into account multiple metrics and factors.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.   