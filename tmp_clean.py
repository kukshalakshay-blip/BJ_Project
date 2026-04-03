import json
import os

files = ['1_data_loading_and_cleaning.ipynb', '2_feature_engineering_and_db_load.ipynb']

replacements = {
    # File 1 replacments
    "# Set display options for better visibility\n": "# Set display options\n",
    "# Define the path to our raw dataset\n": "# Define dataset path\n",
    "# Load the CSV using Pandas\n": "# Load CSV file\n",
    "# Note: Explicitly setting encoding for standard superstore datasets to avoid reading errors\n": "# Use fallback encoding\n",
    "# Quick sanity check of the top 5 rows\n": "# Inspect first 5 rows\n",
    "# Inspect data types and missing values footprint\n": "# Check data types & nulls\n",
    "# Produce summary statistics for numerical columns\n": "# Summary statistics\n",
    "# 2.1 Standardize Column Names (e.g., 'Order Date' -> 'order_date')\n": "# 2.1 Standardize Column Names\n",
    "# PostgreSQL prefers lowercase column names with underscores\n": "",
    "# 2.2 Remove Duplicate Rows\n": "# 2.2 Remove Duplicates\n",
    "# Strategy: \n": "",
    "# Fill missing float/int metrics (like profit/discount) with 0\n": "# Fill numerics with 0\n",
    "# Fill missing text variables (like Region/State) with 'Unknown'\n": "# Fill text with 'Unknown'\n",
    "# Convert to datetime object (Day/Month/Year or Month/Day/Year inferred automatically usually, but adjust format if necessary)\n": "# Convert to datetime\n",
    "# Sanity check on the newly assigned datatypes\n": "# Check new datatypes\n",
    "# Validate final clean dataset\n": "# Validate final dataset\n",
    "# Export clean data for the next phase\n": "# Export clean data\n",
    
    # File 2 replacements
    "# When loading from CSV, datetimes revert to strings. We just force them back to datetime once.\n": "# Convert strings back to datetime\n",
    "# Processing Time: How long did it take to ship orders?\n": "# Calculate processing time\n",
    "# The Superstore dataset typically has 'profit' and 'sales' columns.\n": "",
    "    # Creating a quick categorical profit indicator\n": "    # Categorical profit indicator\n",
    "# Database credentials\n": "# DB credentials\n",
    "db_user = 'postgres'    # Default user is usually postgres\n": "db_user = 'postgres'\n",
    "# Create the SQLAlchemy connection engine string\n": "# Create connection engine\n",
    "    # Test the connection\n": "    # Test connection\n",
    "# Save Final DataFrame to SQL Table\n": "# Save to SQL Table\n",
    "# This will be the table that your BI Dashboard Developer connects to via Power BI!\n": "",
    "    # if_exists='replace' will drop the table if it already exists, 'append' adds to it.\n": "",
    "# Save the fully engineered dataframe to a final CSV for the team\n": "# Save final CSV\n"
}

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
            
        for cell in notebook.get('cells', []):
            if cell['cell_type'] == 'code':
                new_source = []
                for line in cell['source']:
                    modified_line = line
                    for old, new in replacements.items():
                        if old in modified_line:
                            modified_line = modified_line.replace(old, new)
                    if modified_line != "":  # remove empty lines left by deleted comments
                        new_source.append(modified_line)
                cell['source'] = new_source

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
            f.write('\n')
        
        print(f"Updated comments in {filename}")
    else:
        print(f"File {filename} not found.")
