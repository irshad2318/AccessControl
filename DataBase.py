from configparser import SafeConfigParser

import pyodbc

class DataBaseConn():
    """Connectin to Database Using pyodbc """

    def __init__(self, file):
        self.filepath = file
        self.parser = SafeConfigParser()
        self.parser.read(self.filepath)


    def DbConnCheck(self):
        try:
            self.password = self.parser.get('MSSQLSERVER', 'PWD')
            self.uid = self.parser.get('MSSQLSERVER', 'UID')
            self.d_base = self.parser.get('MSSQLSERVER', 'DB')
            self.server = self.parser.get('MSSQLSERVER', 'SERVER')
            print("connecting to DataBase  : ", '{}'.format(self.server) )
            self.cncn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + self.server +
                                       ';DATABASE=' + self.d_base + ';UID=' + self.uid + ';PWD=' + self.password)
            self.cur = self.cncn.cursor()
            

        except pyodbc.OperationalError:
            print("Error Connecting to Server check config file Or Network Connection")
            exit(0)
            

        except pyodbc.Error as err:
            print(err)
            
            print("UserName or Password Error Check the Config file ")
            exit(0)
        except KeyboardInterrupt:
            self.cnnc.close()
            print("Closing Connection ")
            exit(0)
        
        if self.cur:
                print("Connected to Database ", '{}'.format(self.d_base))
        

    




