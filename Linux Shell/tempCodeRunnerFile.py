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
    
    elif 'login' in command:
        print(os.get_exec_path('a.exe'))
    
