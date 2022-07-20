import os
import subprocess
import pyttsx3
import psutil
import shutil
import datetime
import calendar
import platform
import Commands
from termcolor import cprint
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
present=os.getcwd()
temp=present.split('\\')
n=len(temp)
var=temp[n-1]
print("")

while True:
    cprint(username+"@"+pc+"~"+var,"green")
    cprint("$","yellow",end="")
    command=input()

    if '|' in command:
        words=command.split(" | ")
        for i in words:
            Commands.commands(i)

    elif 'echo $HOME' in command:
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
        try:
            sentence=command.replace('ls -l ','')
            mask=oct(os.stat(sentence).st_mode)[-3:]
            print(mask)
        except:
            cprint('file not found','red')

    elif 'ls' in command:
        print(os.listdir(os.getcwd()))
        print("")
    
    elif 'say' in command:
        sentence=command.replace('say','')
        speak(sentence)
    

    elif 'cat' in command:

        if 'cat>>' in command:
            sentence=command.replace('cat>>','')
            try:
                file=open(sentence,'a')
                while(True):
                    content=str(input())
                    if('^C' not in content):
                        file.write(content+"\n")
                    else:
                        break
                content.replace("^C","")
                file.close()
            except Exception as e:
                cprint(e,'red')

        elif 'cat>' in command:
            sentence=command.replace('cat>','')
            try:
                file=open(sentence,'w')
                while(True):
                    content=str(input())
                    if('^C' not in content):
                        file.write(content+"\n")
                    else:
                        break
                content.replace("^C","")
                file.close()
            except Exception as e:
                cprint(e,'red')

        else:
            sentence=command.replace('cat ','')
            try:
                file=open(sentence,'r')
                data=file.read()
                cprint(data,'magenta')
                file.close() 
            except Exception as e:
                cprint(e,'red')

    elif 'cd' in command:
        if '..' in command:
            sentence=command.replace('cd ','')
            try:
                os.chdir(sentence)  
                folder_name = os.path.basename(os.getcwd())
                var=folder_name
            except Exception as e:
                cprint(e,'red')
        else:
            sentence=command.replace('cd ','')
            try:
                os.chdir(os.getcwd()+"\\"+sentence)  
                var=var +"\\" +sentence
            except:
                cprint("Not found","red")
    
    elif 'mkdir' in command:
        sentence=command.replace('mkdir ','')
        os.mkdir(sentence)
    
    elif'rmdir' in command:
        sentence=command.replace('rmdir ','')
        try:
            os.rmdir(sentence)
        except Exception as e:
            cprint(e,"red")
    
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
    
    elif 'wc -l' in command:
        filename=command.replace('wc -l ','')
        try:
            f=open(filename,'r')
            data=f.read()
            count=-1
            for line in data.split("\n"):
                count=count+1
            print(count)
            f.close()
        except Exception as e:
            cprint(e,'red')

    elif 'wc -w' in command:
        filename=command.replace('wc -w ','')
        try:
            f=open(filename,'r')
            data=f.read()
            count=1
            for word in data.split(" "):
                count=count+1
            print(count)
            f.close()
        except Exception as e:
            cprint(e,'red')

    elif 'wc -c' in command:
        filename=command.replace('wc -c ','')
        try:
            f=open(filename,'r')
            data=f.read()
            count=-2
            for char in data:
                count=count+1
            print(count)
            f.close()
        except Exception as e:
            cprint(e,'red')
    
    elif 'clear' in command:
        subprocess.call('cls',shell=True)
    
    elif 'exec c' in command:
        cmd=command.replace("exec c ","")
        try:
            subprocess.call(["gcc",cmd])
            subprocess.call("./a.exe")
            print("")
        except Exception as e:
            cprint(e,'red')

    elif 'exec j' in command:
        cmd=command.replace("exec j ","")
        try:
            subprocess.call(["javac",cmd])
            cmd=cmd.replace(".java","")
            subprocess.call(["java",cmd])
            print("")
        except Exception as e:
            cprint(e,'red')

    elif 'exec py' in command:
        cmd=command.replace("exec py ","")
        try:
            subprocess.call(["python",cmd])
            print("")
        except Exception as e:
            cprint(e,'red')
    
    elif 'cp' in command:
        sentence=command.replace('cp ','')
        try:
            index=sentence.split("  ")
            src=index[0]
            dest=index[1]
            shutil.copy(src,dest)
        except Exception as e:
            cprint(e,'red')

    elif 'mv' in command:
        sentence=command.replace('mv ','')
        try:
            index=sentence.split("  ")
            src=index[0]
            dest=index[1]
            shutil.move(src,dest)
        except Exception as e:
            cprint(e,'red')

    elif 'chmod' in command:
        sentence=command.replace('chmod ','')
        query=sentence.split(" ")
        try:
            num=query[0]
            octal=int(num,8)
            os.chmod(query[1],octal)
        except Exception as e:
            cprint("Invalid command",'red')
    
    elif 'vi' in command:
        sentence=command.replace('vi ','')
        try:
            file=open(sentence,'w')
            while(True):
                content=str(input())
                if('^C' not in content):
                    file.write(content+"\n")
                else:
                    break
                content.replace("^C","")
            file.close()
        except Exception as e:
            cprint(e,'red')
        
    elif '.sh' in command:
        try:
            file=open(command,"r")
            data=file.read()
            for line in data.split("\n"):
                Commands.commands(line)
        except Exception as e:
            cprint(e,'red')
    
    elif 'grep' in command:
        sentence=command.replace('grep ', '')
        ele=sentence.split(" ")
        try:
            file=open(ele[1],"r")
            data=file.read()

            for line in data.split('\n'):
                if ele[0] in line:
                    cprint(line,"cyan")
                else:
                    pass
        except Exception as e:
            cprint(e,'red')
    
    elif 'sudo adduser' in command:
        sentence=command.replace('sudo adduser ','net user /add ')
        subprocess.call(sentence)
    
    elif 'sudo userdel' in command:
        sentence=command.replace('sudo userdel ','net user /del ')
        subprocess.call(sentence)
    
    elif 'help' in command:
        try:
            file=open('help.txt','r')
            data=file.read()

            for line in data.split("\n"):
                cprint(line,'magenta')
        
        except Exception as e:
            cprint('not found','red')
    
    elif 'color' in command:
        try:
            subprocess.call(command,shell=True)
        except Exception as e:
            print("invalid color")

    elif 'exit' ==command:
        exit()
    
