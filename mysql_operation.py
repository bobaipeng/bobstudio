# -*- encoding: utf-8 -*-

import pymysql
import logging
import uuid as uuidtool
log = logging.getLogger(__name__)
import time
class MysqlOperation():

    def exeute_sql(conn,cur,sql,param):
        print()

if __name__ == '__main__':

    params1=[]
    params2=[]
    params3=[]
    params4=[]
    userid = 271473
    uid=1590165283392288531
    usercode= '75'
    image_url='/images/person/20221109/164/5faa5a6056944b62b1cdc58dae376df7.jpg'
    group_id =6
    person_feature='up5IMr4DVtU80NXSvSRUN7y8Q0c9STVpPaEXfTzthBc9CRXyvgTRsbwJb2i9XIKnO3zgBzv3mZ28Ugl%2BvaMzPb0zeqo%2BIjprPRcZnr22dCc94FhRvNpLkDwf4K88o3navON%2F0D2pI%2BI9K35OPcG76r2irOE9ZASFvJXnbrynJSM9sNioPaao4jyT4AQ9fVJtPaWZYb23AES9357Iu5PEEDy0qBs8tbAUPZpW7T4u9eC9Xj81vdaHOD2sBDm8nhC6vW8rPL2XBEe8V51evFqVID3ocf487wAcPC%2BiC708K9%2B8tSUBPP%2BHBr3DKNm93U%2F5vX5SJL2pSXC9LEVPvctU771m8B%2B953I5PHzy7b1WucM9Jr3bvBT71L31Kaa9gBnIvXG9Xz016oO9nETNvTWQvjy0UAE8mqjxPKw%2B6DvpnAw9plpZvN8nrD2UZvc7zkdBvjJHVb0ZrEu9W0t%2Bvd%2FFA72EXnW8C7f5PQDOdj4EuzQ9BTWJPLQN3D1MYK%2B%2BE%2FaovceRwbqzWGu9H8XDPCQHcD0kb5s9n%2FgnvSY%2FZbwPGNQ8ghU0PWV5FbyMj6c9dKB0OhjL%2Fr2wihA9NQGmPJtlOz1SKPg84KB4vWGpUzyKr3m8%2FlZVvOwjnz0BWAC9LYitPIcUWL3gKZC%2BAzMmvht9JT39Yda8Ai7dPemGPzko2SI8pZRCuuSZuL0IrRe7Th5hvbpPir2M1lk89aLdvQCpfr2oO3q9jvxiPY9r3D2ee4a9JmoMO9RGdb2Ko8e8gph9vipGOL1nLkc9PEKpvWUaD720pWa9aZI2O%2FbKAL0C0aq9SX7ovWKlEryieEI9jF%2FpO2Ogd70IxSQ9T13vPd6tSj0NSCs8qgQ5vTfjez2miT%2B9Ao3au%2BF8HTxGcby8nHG2varKrL3JQEM8qQkqvRuD4D1BKvu9LzFmvWFBfL1rlA28uxPvPKren73GUya9fMMhvXAwgT2Sdng9OI6FPQ4CWr2UQMY%2BAIAwvStzzj2ZIFm9LD96O2lpXD0ZP987%2Bhz9PasugL28NZS9PJXXPWw5x7vYf1A9JnrcvQy9Ob3uDAe9jWSMPGA3xb0W%2FXY7IwbePcYSXT00ivs9iJ1TPPDdiT0DNDa8pX%2BJO5w7er3whpm7A60lvQ4WML2Te2c8eIL%2Fu687JLxc6oa7pKamvYPfsb2IVH686I5XPalFOjpmlaI9wmbZvUR7WD0ngjM8ddY%2FPD8bDbxgj2W9%2BdbMvJwCZj17S4K97gSnuz0X2L2Xwa29iXhkvL%2BkHr2dDkU9mDxCvPDONj0mqkm9DfxJPVGp0byTr347wgNbvFO9pL0tEnS9eJQZPJp1bL1Tiqu9T6HzvSC7jj0F09683JEuu39TaA%3D%3D'
    cog_uid= 271473
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for index in range(27,97):
        params1=[]
        params2=[]
        params3=[]
        params4=[]
        for i in range(0,10000):
            userid=userid+1
            time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            name = str(uuidtool.uuid1())
            code = name
            data = (userid,name,code,usercode,time1,time1)
            params1.append(data)
            uid=uid+1
            data1 = (uid,image_url,userid,usercode,time1,time1)
            params2.append(data1)
            group_id=index
            data2 = (group_id,userid,usercode,time1,time1)
            params3.append(data2)

            cog_uid=cog_uid+1
            data3 = (cog_uid,image_url,person_feature,userid,name,time1,time1)
            params4.append(data3)
        conncc = pymysql.connect(host='10.151.5.79', user='root', password='senseBA2019*', port=30306, database='person',
                                        charset='utf8',ssl_verify_identity=True) # 创建连接
        conncc.ping(reconnect=True)                             
        curcc = conncc.cursor()  # 创建游标
        _sql1 = "INSERT INTO person.person VALUES ( %s,%s,'','',%s,'','','','','','',0,'','',0,NULL,NULL,%s,%s,NULL,%s,NULL,0,NULL,NULL,'',NULL);"
        print(curcc.executemany(_sql1, params1))
        curcc.close()
        conncc.commit()
        conncc.close()

        conncc = pymysql.connect(host='10.151.5.79', user='root', password='senseBA2019*', port=30306, database='person',
                                        charset='utf8',ssl_verify_identity=True) # 创建连接
        conncc.ping(reconnect=True)                             
        curcc = conncc.cursor()  # 创建游标
        _sql2 = "INSERT INTO person.person_image VALUES (%s,%s,NULL,NULL,%s,0,%s,%s,NULL,%s);"
        print(curcc.executemany(_sql2, params2))
        curcc.close()
        conncc.commit()
        conncc.close()

        conncc = pymysql.connect(host='10.151.5.79', user='root', password='senseBA2019*', port=30306, database='person',
                                        charset='utf8',ssl_verify_identity=True) # 创建连接
        conncc.ping(reconnect=True)                             
        curcc = conncc.cursor()  # 创建游标
        _sql3 = "INSERT INTO person.person_group_member VALUES (%s,%s,NULL,'0',0,%s,%s,NULL,%s);"
        print(curcc.executemany(_sql3, params3))
        curcc.close()
        conncc.commit()
        conncc.close()


        conncc = pymysql.connect(host='10.151.5.79', user='root', password='senseBA2019*', port=30306, database='person',
                                        charset='utf8',ssl_verify_identity=True) # 创建连接
        conncc.ping(reconnect=True)                             
        curcc = conncc.cursor()  # 创建游标
        _sql4 = "INSERT INTO cognitivesvc.person_face_feature VALUES(%s,%s,%s,'KM_feature_face_nart_cuda11.0-trt7.1-int8-T4_b32_2.51.0.model',%s,%s,NULL, 0,'cognitivesvc',%s, NULL,%s,'', 0);" 
        print(curcc.executemany(_sql4, params4))
        curcc.close()
        conncc.commit()
        conncc.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))