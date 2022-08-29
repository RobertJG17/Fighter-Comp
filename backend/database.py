import sqlalchemy
import pgconfig
import pg8000


# CLASS IMPLEMENTATION TO INTERACT WITH DATABASE THROUGH ENDPOINTS
class DataBase:
    def __init__(self):
        # create connection pool to re-use connections
        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=pgconfig.getconn
        )

        self.engine = engine

    # Methods
    def queryHandler(self, col: str):
        with self.engine.connect() as db_conn:
            match col:
                case 'basic': data=self.basicFighterInfo(db_conn)
                case 'fighters': data=self.allFighters(db_conn)
                case 'styles': data=self.allStyles(db_conn)
                case 'gyms': data=self.allGyms(db_conn)
                case 'all': data=self.all(db_conn)
                case _: pass
        
        return data

    # DEF MAIN QUERIES
    def basicFighterInfo(self, db_conn):
        return db_conn.execute(f'''
            SELECT fighter, href, "weight-class", hometown, "trains-at", style, height, age 
            FROM fighters ORDER BY fighter;
        ''')

    def allFighters(self, db_conn):
        return db_conn.execute(f'''SELECT fighter FROM fighters;''')

    def allStyles(self, db_conn):
        return db_conn.execute(f'''SELECT DISTINCT(style) col FROM fighters ORDER BY col;''')

    def allGyms(self, db_conn):
        return db_conn.execute(f'''SELECT DISTINCT("trains-at") col FROM fighters ORDER BY col;''')
    
    def all(self, db_conn):
        return db_conn.execute(f'''SELECT * FROM fighters;''')