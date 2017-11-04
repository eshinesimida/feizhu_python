# -*- coding: utf-8 -*-
import MySQLdb
import uuid
import random

class xiechengDAO(object):
    def __init__(self,host="********",user="root",password="*******", db="1224"
                         ):
        self.host = host
        self.db = db
        self.user = user
        self.password = password



    def savehotellink(self,listPageInfo):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,use_unicode=1,charset='utf8')
        cursor = db.cursor()
        for hotel in listPageInfo:
            try:
                    id = uuid.uuid1()
                    cursor.execute("insert IGNORE into feizu(jingqu,province,user,comment,time,category,ID)values(%s,%s,%s,%s,%s,%s,%s)" ,
                                   (hotel["jingqu"],hotel["province"],hotel["user"],hotel["comment"],hotel["time"],hotel["category"],hotel["ID"]))
            except Exception,e:
                print hotel["user"]
        db.commit()
        cursor.close()
        db.close()

