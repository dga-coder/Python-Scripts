import cx_Oracle, os, sys

def db_connect():
    # Build a DSN (can be subsitited for a TNS name)
    dsn = cx_Oracle.makedsn("r720a", 1521, "oraR720A")
    db = cx_Oracle.connect("GGPS_PROD", "123", dsn)
    cursor = db.cursor()
    return cursor
db_connect()
cursor = db_connect()
#def db_lookup(cursor):
    #cursor.execute("SELECT RSID, OBJECTID,  L_T_ADD_I,  L_F_ADD_I,  R_T_ADD_I,  R_F_ADD_I FROM gi_road_segment where RSID=541500")
sql = "SELECT RSID, OBJECTID,  L_T_ADD_I,  L_F_ADD_I,  R_T_ADD_I,  R_F_ADD_I FROM gi_road_segment where RSID=541500"
results = cursor.fetchall()
    #print row
    #return row
for row in results:
    RSID = row[0]
    OBJECTID = row[1]
    L_T_ADD_I = row[2]
    L_F_ADD_I = row[3]
    R_T_ADD_I = row[4]
    R_F_ADD_I = row[5]
    print (RSID, OBJECTID,  L_T_ADD_I,  L_F_ADD_I,  R_T_ADD_I,  R_F_ADD_I)

#cursor = db_connect()
#db_connect()
#print db_lookup(cursor)
#print db_lookup(cursor)
