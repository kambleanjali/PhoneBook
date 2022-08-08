import pymysql

con = None
cur = None

def dbconnect():
    global con,cur
    try:
        con = pymysql.connect(host='localhost',
                        database='phonebook',
                        port=3306,
                        user='root',
                        password='')
        cur = con.cursor()
    except Exception as e:
        print(e)

def dbdisconnect():
    con.close()

def ShowContact():
    dbconnect()
    query = 'select * from Contact'
    cur.execute(query)
    #Showing the Contact from the cursor memory
    #fetchall() will fetch all the rows of the table as tuple of tuples
    Contact= cur.fetchall()
    dbdisconnect()
    return Contact

def searchContact(PhoneNumberId):
    dbconnect()
    query = f"select * from  Contact where PhoneNumberID ={PhoneNumberId}"
    cur.execute(query)
    Contact = cur.fetchone()
    dbdisconnect()
    return Contact

def insertContact(Firstname,lastname,workphone,homephone):
    dbconnect()
    query = f'insert into Contact(Firstname,lastname,workphone,homephone) values ("{Firstname}","{lastname}",{workphone},{homephone})'
    #will insert Contact in the cursor memory
    cur.execute(query)
    #insert the Contact in the actual database (permanent)
    con.commit()
    dbdisconnect()

def deleteContact(PhoneNumberID):
    dbconnect()
    query = f"delete from Contact where PhoneNumberID={PhoneNumberID}"
    cur.execute(query)
    con.commit()
    dbdisconnect()

def updateContact(PhoneNumberID,column,newvalue):
    dbconnect()
    if column=="lastname" or column=="homephone":
        query = f'update Contact set {column} = "{newvalue}" where PhoneNumberID={PhoneNumberID}'
    else:
        query = f'update Contact set {column} = {newvalue} where PhoneNumberID={PhoneNumberID}'

    cur.execute(query)
    con.commit()
    dbdisconnect()