import os
from os.path import dirname, abspath

from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

BASE_DIR = f'{dirname(abspath(__file__))}/'
env_path = Path(BASE_DIR) / '.env'
load_dotenv(dotenv_path=env_path)

os.environ["BASE_DIR"] = BASE_DIR

#print(os.getenv('BASE_DIR'))
