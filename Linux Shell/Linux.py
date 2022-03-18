import os
username=os.getlogin()
pc=os.environ['COMPUTERNAME']
print("")
while True:
    print(username+"@"+pc+"~")
    print("$",end="")
    command=input()

    if 'echo' in command:
        sentence=command.replace('echo','')
        print(sentence)
        print("")
    elif 'pwd' == command:
        print(os.getcwd())
        print("")

    elif 'ls' in command:
        print(os.listdir(os.getcwd()))
        print("")
    
    elif 'exit' ==command:
        exit()
