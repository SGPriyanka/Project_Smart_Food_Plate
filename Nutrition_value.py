import MySQLdb
import sys
def getValues(fid)
    x=fid
    db=MySQLdb.connect(host="gndb2.cff0wq1cnhui.us-west-2.rds.amazonaws.com",port=3306,user="",passwd="",db="Sample")
    co=db.cursor()
    co.execute("SELECT * FROM fruits WHERE fid=%d" %(x))
    data=co.fetchall()
    for row in data:
        print(row)
    db.close()

def setConsumedValues()
    x=fid
    db=MySQLdb.connect(host="gndb2.cff0wq1cnhui.us-west-2.rds.amazonaws.com",port=3306,user="",passwd="",db="Sample")
    co=db.cursor()
    co.execute("SELECT * FROM fruits WHERE fid=%d" %(x))
    data=co.fetchall()
    for row in data:
        print(row)
    db.close()
