from time import sleep
from subprocess import call
import os

author = "Killereq_PL"
version = 0.3
class cmdObject:
    def __init__(self):
        print("\nPyCMD version", version, "by", author)
        print("Input 'help' to see all commands. \n")
    def echo(self, arg1: str) -> None:
        print(arg1)
        
    def clear(self):
	    _ = call('clear' if os.name == 'posix' else 'cls')
	    print("\nPyCMD version", version, "by", author)
	    print("Input 'help' to see all commands. \n")

    def help(self):
        print("""commands:
help (shows all commands),
echo <string>,
exit,
program <filename> (enters program mode),
clear
\n""")
    def program(self, filename: str) -> None:
        fn = filename+".pycmd"
        print("("+fn+")")
        try:
            file = open(fn, 'r+')
        except:
            file = open(fn, 'w')
            file.close()
            file = open(fn, 'r+')
        if file.read() != "":
            file.seek(0)
            print("Program contents:")
            print(file.read())
            print("")
            file.seek(0)
            lines = file.read().splitlines()
        else:
            lines = []
            print("Project with that name not found; created a new one.")
        print("Choose mode {modify <line>, run, overwrite, cancel}")
        cmds = ["finish", "echo", "delay"]
        mode = input("> ")
        if "overwrite" in mode:
            lines = []
            i = 0
            while True:
                i += 1
                cl = input(str(i)+" ")
                try:
                    if "finish" in cl:
                        print("Save file?")
                        s = input("(Y/N) ")
                        if "Y" in s:
                            """
                            {}
                            """.format("\n".join(lines))
                            file.seek(0)
                            file.write('\n'.join([i for i in lines]))
                            file.close()
                        break
                    else:
                        lines.append(cl)
                except ValueError:
                    print("ERROR: Command does not exist.")
                    i -= 1
                    continue
            return "restart"

        elif "modify" in mode:
            l = int(mode.replace("modify ", ""))
            modLine = input(str(l)+" ")
            lines[l-1] = modLine
            return "restart"
            
        elif "run" in mode:
            variables = {}
            for line in lines:
                if "echo" in line:
                    b = line.replace("echo ", "", 1)
                    if b in variables:
                    	b = variables[b]
                    self.echo(b)
                elif "delay" in line:
                    b = line.replace("delay ", "", 1)
                    if b in variables:
                    	b = variables[b]
                    sleep(int(b)/1000)
                elif "var" in line:
                    b = line.replace("var ", "", 1).split(" = ")
                    variables.update({b[0]:b[1]})
                elif "wait_for_input" in line:
                    b = line.replace("wait_for_input ", "", 1)
                    variables.update({b:input()})
                elif "if" in line:
                    b = line.replace("if ", "", 1)
                    c = b.split(" ", 2)
                    command = b.split(": ")[1]
                    print(command)
            sleep(1)
            return "restart"
        
        else:
            return "cancel"

cmd = cmdObject()
while True:
    a = input("> ")
    if "echo" in a:
        b = a.replace("echo ", "")
        cmd.echo(b)
    elif "exit" in a:
        break
    elif "help" in a:
        cmd.help()
    elif "program" in a:
        b = a.replace("program ", "")
        while True:
            if cmd.program(b) == "restart":
                print("\n\n")
                continue
            else:
                break
    elif "clear" in a:
    	cmd.clear()
    else:
        print("ERROR: Command does not exist.")    