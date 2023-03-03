import mysql.connector


credentials={
        'user':"root",
        'password':"root",
        'host':"192.168.1.10",
        'database':"WORLD"

}
db = mysql.connector.connect(**credentials)
def values():
        cursor = db.cursor()
        sql_stat="SELECT * FROM cityDetails"
        cursor.execute(sql_stat)
        values = cursor.fetchall()
        list =[]
        for i in range(10):
                list.append(values[i])
        return list

values()
