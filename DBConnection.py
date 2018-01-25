import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='TrollCop',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

def insertUser(userName, spamCount = 0):
    with connection.cursor() as cursor:
        print("InsertUser",userName)
        cursor.execute("insert into `Users` values( %s, %s)",(userName, spamCount))
        connection.commit()
    


def isExistingUser(userName):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `Users` where userName = '%s'" % (userName)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            
            return True
    
    return False

def updateUser(userName):
    with connection.cursor() as cursor:
        sql = "SELECT spamCount FROM `Users` where userName = '%s'" % (userName)
        cursor.execute(sql)
        result = cursor.fetchone()
        spamCount = result.get('spamCount')
        spamCount += 1
        sql = "Update `Users` set spamCount = %s where userName = '%s'" % (spamCount,userName)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            connection.commit()
            return True
            
 
    return False


def retrieveUsers(): 
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `Users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)
   

def insertTweet(tweetId, userName, tweet, timestamp, isTroll):
    with connection.cursor() as cursor:
        cursor.execute("insert into `Tweets` values( %s, %s, %s, %s, %s)",(tweetId, userName, tweet, timestamp, int(isTroll)))
        connection.commit()
 

def retrieveUsers(): 
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `Tweets`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)
   
