import pymysql
from config import DB_CONFIG   # le config.py qu'on a déjà défini

def conn_db():
    conn = pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        charset=DB_CONFIG["charset"]
    )
    return conn
