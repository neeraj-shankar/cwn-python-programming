import os
from dotenv import load_dotenv

CURRENT_DIR = os.getcwd()
print(f"Current Directory: {CURRENT_DIR}")

# Reading environment file 
load_dotenv("./environment_file.env") # Returns True if file is found else False
db_host = os.environ.get("DB_HOST") 
print(f"Extracted Host: {db_host}")
print(f"Type of Extracted Host: {type(db_host)}")
