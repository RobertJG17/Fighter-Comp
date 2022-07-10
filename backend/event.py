from pyparsing import col
import sqlalchemy
import pg8000
from google.cloud.sql.connector import Connector

import pgconn

class DataBase:

    # Attributes
    engine = None

    def __init__(self):
        pass

    # Methods
    # ENGINE INITIALIZATION
    def get_engine(self):
        # create connection pool to re-use connections
        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=pgconn.getconn
        )

        self.engine = engine

    def queryHandler(self, col: str):
        if self.engine is None: return

        with self.engine.connect() as db_conn:
            print('COL:', col)
            if col == 'fighters': return self.allFighters(db_conn)
            if col == 'styles': return self.allStyles(db_conn)
            if col == 'gyms': return self.allGyms(db_conn)
            if col == 'all': return self.all(db_conn)
            
        db_conn.close()

    # DEF MAIN QUERIES
    def allFighters(self, db_conn):
        return db_conn.execute(f'''SELECT fighter FROM fighters ORDER BY fighter''').fetchall()

    def allStyles(self, db_conn):
        return db_conn.execute(f'''SELECT DISTINCT(style) col FROM fighters ORDER BY col''').fetchall()

    def allGyms(self, db_conn):
        return db_conn.execute(f'''SELECT DISTINCT("trains-at") col FROM fighters ORDER BY col''').fetchall()
    
    def all(self, db_conn):
        return db_conn.execute(f'''SELECT * FROM fighters''').fetchall()
    


