def mkperson():
    file=open("D:\studio\person\\ren33.png","rb")
    data=file.read()
    file.close()
    
    for i in range(1,10001):
        new_file=open("D:\studio\person\person1w\wname"+str(i)+"_"+"wid"+str(i)+".jpg","wb")
        new_file.write(data)
    
    new_file.close()
def mkcsv():
    with open('D:\studio\person\person1w.csv',mode='a') as filename:
        for i in range(1,10001):
            filename.write('267,wname'+str(i)+',enName2,wid'+str(i)+',,0,1111,update,otherid,externalid,42,20200402,17788888888,0,0,remark')

            filename.write('\n')# 换行

if __name__ == '__main__':
    #mkperson()
    mkcsv()