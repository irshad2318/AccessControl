import DataBase as Db 
import datetime

conn = db("config/mssql.conf")
conn.dbConnCheck()

def att(dstart, d_end, empcard, sql ):
        """" take attendance"""
        dat_start = dstart
        dat_dend = d_end

        

        for i in empcard:
               
                sql =  sql
                att_row = conn.curs.execute(sql, i, dat_start, dat_dend)
                
                print("Department :" , "From Date : " '{}' " To Date : " '{}'.format(dat_start, dat_dend))
                print("-"*70)
                print("EMPID    EMPNAME          DATE        TIMEIN    TIMEOUT     TOTAL")
                print("-"*70)
                for row in att_row:
                    s = (datetime.datetime.strptime(row[4], '%H:%M:%S')+ datetime.timedelta(hours=3))
                    s2 =(datetime.datetime.strptime(row[3], '%H:%M:%S')+ datetime.timedelta(hours=3))
                    s3 = datetime.datetime.strftime(s2, "%H:%M:%S")
                    s4 = datetime.datetime.strftime(s, "%H:%M:%S")
                    if s3 == s4:
                        s4  = 'No Punch'
                    
                  

                    print(row[0] ,"|", row[1],"|", row[2],"|",s3,"|",s4,"|",str(datetime.timedelta(minutes=row[5])) ,"|")
            
            
                print("-"*70)
        cncn.close()
        print("Please check the Report folder for pdf file ")