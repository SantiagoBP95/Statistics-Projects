# Statistics-Projects

Practical and educational projects covering descriptive statistics, probability, statistical
inference, and database management.

## Contents

### Statistical Inference
- `Uber vs Lyft price dataset analysis/` — statistical analysis of Uber vs. Lyft fare data
  (Kaggle dataset), notebook + PDF write-up.

### Exploratory Data Analysis
- `AED_titanic/` — exploratory data analysis of the Titanic dataset in R (RMarkdown
  report + preprocessing/analysis scripts under `src/`).

### Database Management
- `course_management_system_db/` — relational database design for a course/subscription
  management system (PostgreSQL): ER diagram, table scripts, seed data, and a Dash/Plotly
  dashboard (`Dashboard.py`) querying enrollment and course metrics. Connection settings are
  read from environment variables — copy `.env.example` to `.env` and fill in your local
  Postgres credentials before running `Dashboard.py` / `ConexionPY.py`.

## Technologies
- Python (NumPy, Pandas, Matplotlib, SciPy, Dash/Plotly, psycopg2)
- R (RMarkdown)
- PostgreSQL

## License
This repository is licensed under the MIT License.
