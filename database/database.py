from psycopg2 import pool

class Database:
    connection_pool=None
    
    
    @classmethod
    def Init(cls):
        cls.connection_pool=pool.SimpleConnection(1,10,
                                      database="learning",
                                      user="progres",
                                      host="localhost")
               
    @classmethod
    def getconnection(cls):
        return cls.connection_pool.getconn()
        
    
    @classmethod
    def return_connection(cls,connection):
        Database.connection_pool.putconn(connection)
        
    
    @classmethod
    def closeall(cls):
        Database.connection_pool.closeall()
        
        
        
class CursorFromConnectionPool:
    connection_pool=None
    
    def __init__(self):
        self.connection=None
        self.cursor= None


    def __enter__(self):
        self.connection=Database.getconnection()
        self.cursor=self.connection.cursor()
        return self.cursor
    
    
    def __exit__(self,exception_type,exception_value,exception_traceback):
        if exception_value is not None:   # errors like TypeError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)