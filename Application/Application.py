import pymysql

host = 'rm-bp1oo27t8762xhlob0o.mysql.rds.aliyuncs.com'
port = 3306
dbName = 'amusementparkticketsystemdb'
user = 'lab_876627230'
password = '36956893b76b_#@Aa'

db = pymysql.connect(host=host, port=port, db=dbName, user=user, password=password)
csr = db.cursor()

def getmax():
    csr.execute("SELECT * FROM `ticketBooking`")
    r = csr.fetchall()
    ans = 1
    for result in r:
        ans = result[0]
    return ans

global i
i = getmax()

def a_login_submit(phoneNum, psw):
    csr.execute("SELECT password FROM visitor WHERE phoneNum = " + phoneNum)
    r = csr.fetchone()
    if r == None:
        return 0
    else:
        if str(r[0]) == psw:
            return 1
        else:
            return 0


def registNew(a, b, c):
    sql = "INSERT INTO visitor values('" + str(a) + "','" + str(b) + "','" + str(c) + "'," + "0)"
    csr.execute(sql)
    db.commit()


def displayPersonCenter(currentphone):
    sql = "select phoneNum, balance,nickName From visitor where phoneNum = " + currentphone
    csr = db.cursor(cursor=pymysql.cursors.DictCursor)
    csr.execute(sql)
    r = csr.fetchone()
    return r["phoneNum"], r["nickName"], r["balance"]


def addMoney(currentphone, num):
    csr.execute("UPDATE visitor SET balance = balance + '"
                + str(num) + "' WHERE phoneNum = '" + currentphone + "'")
    db.commit()


def getTicket():
    csr.execute("SELECT * FROM `ticket`")
    r = csr.fetchall()
    return r


def getBalance(currentPhoneNum):
    csr.execute("SELECT balance FROM visitor WHERE phoneNum=" + currentPhoneNum)
    r = csr.fetchall()
    return r

def ticketbooking(phonenumber, money, time, type, price, num, need):
    question = "UPDATE `visitor` SET `balance` = "
    question += str(int(money) - need)
    question += " WHERE phoneNum = \""
    question += phonenumber
    question += "\""
    csr.execute(question)
    db.commit()
    print(question)

    question = "UPDATE `ticket` SET `num` = \""
    question += str(int(num) - int(need / int(price)))
    question += "\" WHERE `date` = \""
    question += time
    question += "\""
    question += " AND `type` = \""
    question += type
    question += "\""
    csr.execute(question)
    db.commit()
    print(question)

    global i
    i = i+1
    question = "INSERT INTO `ticketBooking` (`id`,`phoneNum`,`type`,`date`,`ticketNum`,`totalPrice`,`bookingDate`,`isChecked`) VALUES (\'"
    question += (str(i) + "\', \'")
    question += (phonenumber + "\', \'")
    question += (type + "\', \'")
    question += (time + "\', \'")
    question += (str(int(need / int(price))) + "\' , \'")
    question += (str(int(need)) + "\' , \'")
    question += ("2021-7-23 \' , \'")
    question += ("未检票\'" + ");")
    csr.execute(question)
    db.commit()
    print(question)


def userbooking(currentPhoneNum):
    question = "SELECT * FROM `ticketBooking` WHERE `phoneNum` = \""
    question += currentPhoneNum
    question += "\""
    print(question)
    csr.execute(question)
    r = csr.fetchall()
    return r


def reback(item_text, currentPhoneNum):
    print("------------")
    question = "DELETE FROM `ticketBooking` WHERE `id`= \""
    question += item_text[0]
    question += "\";"
    print(question)
    csr.execute(question)
    db.commit()

    # 修改用户表，返还购票费用
    price = ""
    question = "SELECT price FROM `ticket` WHERE `date` = \""
    question += item_text[1]
    question += "\" AND `type` = \""
    question += item_text[2]
    question += "\""
    csr.execute(question)
    cursor = csr.fetchall()
    for result in cursor:
        price = str(result[0])
    money = ""
    question = "SELECT balance FROM `visitor` WHERE `phoneNum` = \""
    question += currentPhoneNum
    question += "\""
    csr.execute(question)
    cursor = csr.fetchall()

    for result in cursor:
        money = str(result[0])
    question = "UPDATE `visitor` SET `balance`= \""
    question += str(float(money) + float(price) * float(item_text[3]))
    question += "\" WHERE `phoneNum` = \""
    question += currentPhoneNum
    question += "\""
    print(question)
    csr.execute(question)
    db.commit()

    # 修改门票表，修改剩余数量
    sum = ""
    question = "SELECT num FROM `ticket` WHERE `date` = \""
    question += item_text[1]
    question += "\""
    question += " AND `type` = \""
    question += item_text[2]
    question += "\""
    csr.execute(question)
    cursor = csr.fetchall()
    for result in cursor:
        sum = str(result[0])
    question = "UPDATE `ticket` SET `num`= \""
    question += str(int(sum) + int(item_text[3]))
    question += "\" WHERE `date` = \""
    question += item_text[1]
    question += "\""
    question += " AND `type`= \""
    question += item_text[2]
    question += "\""
    print(question)
    csr.execute(question)
    db.commit()

def staffLoginSubmit(staffID, staffPassword):
    csr.execute("SELECT password FROM staff WHERE id = " + staffID)
    r = csr.fetchone()
    if r == None:
        return 0
    else:
        if str(r[0]) == staffPassword:
            return 1
        else:
            return 0


def staffGetTicketBooking(phoneNum):
    csr.execute("SELECT * FROM ticketbooking WHERE phoneNum = '" + phoneNum + "'")
    r = csr.fetchall()
    return r


def checkTicket(slct):
    csr.execute("UPDATE ticketbooking SET isChecked = '已检票' WHERE id = '" + str(slct[0]) + "'")
    db.commit()
