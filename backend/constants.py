from dotenv import dotenv_values


CONFIG = dotenv_values('.env')

DB_USER = CONFIG['DB_USER']
DB_PASSWORD = CONFIG['DB_PASS']
DB_NAME = CONFIG['DB_NAME']
DB_PORT = CONFIG['DB_PORT']
