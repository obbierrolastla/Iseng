from requests import *
from bs4 import BeautifulSoup as bs
from sys import argv


#config start

base_url='http://your.school.sch.id'
username='username'
password='password'

#config end

headers={"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
cookie=''
myClass=[]

def error(message):
    print("[*] Error: %s" %message)
    exit(1)

def getCookie(username,password):
    
    global cookie
    global headers

    url=base_url+'/login/do_login/'
    body={"ajaran":"2020","username":username,"password":password}
    
    p=post(url,data=body,headers=headers)
    cookie+=p.headers['Set-Cookie']
    if(p.text!='student'):
        return 1

def getAllClass():

    global headers
    global cookie
    global myClass

    headers.update({"Cookie":cookie,"Referer":"http://m2k.madrasahkudus.online/studentmaster/kelas","Content-Length":"1785"})
    url=base_url+'/studentmaster/grid_kelas'
    body='draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&keyword='
    page=post(url,data=body,headers=headers).text
    soup=bs(page,'html.parser')
    a_tag=soup.find_all('a')
    for i in range(len(a_tag)):
        the_a=a_tag[i]['href']
        the_a=the_a.replace('/me\\','/absensi\\')
        the_a=the_a.replace('\\/','/')
        myClass.append(the_a[2:(len(the_a)-2)])
    #return result

def doLogin(url):
    get(url,headers=headers)

def banner():
    print("""
    \t\t| Auto-Login |\t\t
    """)

def main():
    if((base_url=='http://your.school.sch.id') or (username=='username')):
        error("Please set up to your actual data (read 'README.md' file)")

    banner()
    if(getCookie(username,password)==1):
        error("Login gagal")

    getAllClass()
    print("Total Kelas Anda: %s" %(str(len(myClass))))
    for i in range(len(myClass)):
        doLogin(myClass[i])
        print('kelas ke '+str(i+1))
    
    print("Anda telah login ke SEMUA kelas")

if __name__=="__main__":
    main()


