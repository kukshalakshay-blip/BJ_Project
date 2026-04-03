# Superstore Data Engineering Pipeline

## Overview
This repository contains the Data Engineering phase of a Business Intelligence (BI) project based on the **Sample - Superstore** dataset. The primary goal is to take raw sales data through a robust pipeline—handling data cleaning, feature engineering, and ultimately loading the structured data into a PostgreSQL database. This prepares the data cleanly for downstream analytics, machine learning, and dashboarding.

## Project Structure
- **`1_data_loading_and_cleaning.ipynb`**: Initial data exploration, handling missing values, standardizing date formats, addressing outliers, and basic data cleaning.
- **`2_feature_engineering_and_db_load.ipynb`**: Creation of new analytical features (e.g., profit margins, shipping durations) and the automated pipeline to load the final structured data securely into a PostgreSQL Database.

## Data Files
- `Sample - Superstore.csv`: The raw, unprocessed source data.
- `cleaned_superstore.csv`: The intermediate dataset saved after the first cleaning phase.
- `final_engineered_data.csv`: The final, feature-rich dataset completely ready for BI dashboard consumption.

## Core Technologies
- **Python** (Pandas) for data wrangling
- **Jupyter Notebook** for interactive step-by-step processing
- **PostgreSQL** for final relational data storage
- **Git/GitHub** for version control
