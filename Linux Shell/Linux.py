import os
import pyttsx3
from pynput.keyboard import Key
import psutil
import datetime
import calendar
import platform
from pathlib import Path
global var

var=""
x=datetime.datetime.now()
mem=[]
cpu=[]
lists=[]
home_dir = Path.home()

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

engine.setProperty('rate',170)

def speak(str):
    engine.say(str)
    engine.runAndWait()

username=os.getlogin()
pc=os.environ['COMPUTERNAME']
print("")

while True:
    print(username+"@"+pc+"~"+var)
    print("$",end="")
    command=input()

    if 'echo $HOME' in command:
        home_dir_str = str( home_dir )
        print(home_dir_str)

    elif 'echo $SHELL' in command:
        print(platform.system())

    elif 'echo' in command:
        sentence=command.replace('echo','')
        print(sentence)
        print("")

    elif 'pwd' == command:
        print(os.getcwd())
        print("")
    
    elif 'ls -l' in command:
        sentence=command.replace('ls -l ','')
        print(os.stat(sentence))

    elif 'ls' in command:
        print(os.listdir(os.getcwd()))
        print("")
    
    elif 'say' in command:
        sentence=command.replace('say','')
        speak(sentence)
    
    elif 'cat' in command:

        if 'cat>>' in command:
            sentence=command.replace('cat>>','')
            key=Key.delete
            file=open(sentence,'a')
            while(True):
                content=str(input())
                if('^C' not in content):
                    file.write(content+"\n")
                else:
                    break
            content.replace("^C","")
            file.close()

        elif 'cat>' in command:
            sentence=command.replace('cat>','')
            key=Key.delete
            file=open(sentence,'w')
            while(True):
                content=str(input())
                if('^C' not in content):
                    file.write(content+"\n")
                else:
                    break
            content.replace("^C","")
            file.close()

        else:
            sentence=command.replace('cat ','')
            key=Key.delete
            file=open(sentence,'r')
            data=file.read()
            print(data)
            file.close() 

    elif 'cd' in command:
        if '..' in command:
            sentence=command.replace('cd ','')
            os.chdir(sentence)  
            folder_name = os.path.basename(os.getcwd())
            var=folder_name
        else:
            sentence=command.replace('cd ','')
            os.chdir(os.getcwd()+"\\"+sentence)  
            var=var +"\\" +sentence
    
    elif 'mkdir' in command:
        sentence=command.replace('mkdir ','')
        os.mkdir(sentence)
    
    elif'rmdir' in command:
        sentence=command.replace('rmdir ','')
        try:
            os.rmdir(sentence)
        except Exception as e:
            print(e)
    
    elif 'ps' in command:
        print("PID\t","MEM\t","CPU","STATUS","PROCESS")
        
        for process in psutil.process_iter():
            print(process.pid,"\t",round(process.memory_percent(),2),"\t",round(process.cpu_percent(),2),process.status(),process.name())

    elif 'cal' in command:
        yr=x.year
        mon=x.month
        print(calendar.month(yr,mon))
    
    elif 'date' in command:
        day_no=datetime.date.today().isoweekday()
        days=['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
        print(days[day_no],x)
    
    elif 'whoami' in command:
        print(username)
    
    elif 'uname -a' in command:
        print(platform.platform(),platform.machine())

    elif 'uname -r' in command:
        print(platform.release())

    elif 'uname -v' in command:
        print(platform.version())
    
    elif 'uname -m' in command:
        print(platform.processor())

    elif 'uname' in command:
        print(platform.system())
    
    elif 'exit' ==command:
        exit()
