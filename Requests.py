import sqlite3

try:
    connection = sqlite3.connect("Database.db")
    _context = connection.cursor()
except sqlite3.Error as e:
    _context = ""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def GetRows(query):
    try:
        connection.row_factory = dict_factory
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print (e)
        return None

def GetRow(query):
    try:
        connection.row_factory= dict_factory
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchone()
    except Exception as e:
        print (e)
        return None

def ExecuteWithParams(query,params):
    try:
        _context.execute(query,params)
        connection.commit()
    except  Exception as e:
        print(e)
        return False
    return True

def Execute(query):
    try:
        _context.execute(query)
        connection.commit()
    except  Exception as e:
        print(e)
        return False
    return True

def CheckLogin(username,password):
    query = "SELECT * FROM USERS WHERE Username='{}' and Password='{}'".format(username,password)
    result = GetRow(query)
    if(result != None):
        return result["ID"]
    return -1

def AddUser(firstName,lastName,phone,username,password,isAdmin):
    if(firstName == "" or lastName == "" or username =="" or password == "" or isAdmin == ""):
        return False

    testUsername = username
    query = "SELECT * FROM USERS WHERE LOWER(Username)='{}'".format(testUsername.lower())
    if(GetRow(query) != None):
        return False

    query = "INSERT INTO 'USERS' (Firstname,Lastname,Phone,Username,Password,isAdmin) VALUES(?,?,?,?,?,?)"
    return ExecuteWithParams(query,(firstName,lastName,phone,username,password,isAdmin))

def AddChild(fullname,city,birthday,sitting):
    if(fullname == ""):
        return False
    testName = fullname
    query = "SELECT * FROM Children WHERE LOWER(FullName)='{}'".format(testName.lower())
    if(GetRow(query) != None):
        return False
    query = "INSERT INTO 'CHILDREN' (FullName,City,Birthday,Sitting) VALUES(?,?,?,?)"
    return ExecuteWithParams(query,(fullname,city,birthday,sitting))

def ResetPass(username,phone,password):
    query = "SELECT * FROM USERS WHERE USERNAME='{}' and PHONE='{}'".format(username,phone)
    if(GetRow(query) == None):
        return False
    query = "UPDATE USERS SET PASSWORD='{}' WHERE USERNAME ='{}'".format(password,username)
    return Execute(query)

def RemoveUser(id):
    query = "DELETE FROM USERS WHERE ID={}".format(id)
    return Execute(query)

def GetUser(id):
    query  = "SELECT * FROM USERS WHERE ID={}".format(id)
    return GetRow(query)

def AskForHoliday(id,date):
    query = "SELECT * FROM HOLIDAYREQUESTS WHERE UserID={} and date='{}'".format(id,date)

    if(GetRow(query) != None):
        return False
    query = "INSERT INTO 'HOLIDAYREQUESTS' (UserID,Date) VALUES(?,?)"
    return ExecuteWithParams(query,(id,date))

def GetHolidays():
    query = "SELECT * FROM HOLIDAYREQUESTS"
    return GetRows(query)

def GetUserHolidayRequests(id):
    query = "SELECT * FROM HOLIDAYREQUESTS WHERE UserID={}".format(id)
    return GetRows(query)

def AddCommentForChild(id,child,comment):
    try:
        testName = child
        query = "SELECT * FROM CHILDREN WHERE LOWER(FullName)='{}'".format(testName.lower())
        if(GetRow(query) == None):
            return False
        query = "INSERT INTO 'ChildrenComments' (UserID,Child,Comment) VALUES(?,?,?)"
        return ExecuteWithParams(query,(id,child,comment))
    except Exception as e:
        print(e)
        return False

def GetComments():
    query = "SELECT * FROM CHILDRENCOMMENTS"
    return GetRows(query)

def GetChildComments(child):
    query = "SELECT * FROM CHILDRENCOMMENTS WHERE LOWER(Child)='{}'".format(child.lower())
    return GetRows(query)

def SendRecommend(id,text):
    query = "INSERT INTO 'Recommends'(UserID,Comment) VALUES(?,?)"
    return ExecuteWithParams(query,(id,text))

def GetRecommendations():
    query = "SELECT * FROM Recommends"
    return GetRows(query)

def AddImage(path):
    query = "INSERT INTO 'IMAGES'(Path) VALUES(?)"
    return ExecuteWithParams(query,(path,))

def UpdateImage(path,desc):
    query = "UPDATE IMAGES SET Description='{}' WHERE Path='{}'".format(desc,path)
    return Execute(query)

def DeleteImage(path):
    query = "DELETE FROM IMAGES WHERE Path='{}'".format(path)
    return Execute(query)

def GetChild(name):
    testname = name
    query ="SELECT * FROM CHILDREN WHERE LOWER(FullName)='{}'".format(testname.lower())
    child = GetRow(query)
    if(child == None):
        return None
    comments = GetChildComments(name)
    return (child,comments)

def GetImages():
    query = "SELECT * FROM IMAGES"
    return GetRows(query)
