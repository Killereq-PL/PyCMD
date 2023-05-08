version = "0.1"
class cmdObject:
    def __init__(self):
        print("\nPyCMD version", version)
        print("Input 'help' to see all commands. \n")
    def echo(self, arg1: str) -> None:
        print(arg1)
    def help(self):
        print("""commands:
help (shows all commands),
echo <string>,
exit,
program <filename> (enters program mode)
\n""")
    def program(self, filename: str) -> None:
        fn = filename+".pycmd"
        print("("+fn+")")
        try:
            file = open(fn, 'r')
        except:
            file = open(fn, 'w')
        file.mode = "r+"
        if file.read() != "":
            print("Program contents:")
            print(file.read())
            print("\n")
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
                    if cl in cmds[cmds.index(cl)]:
                        if "finish" in cl:
                            print("Save file?")
                            s = input("(Y/N) ")
                            if "Y" in s:
                                """
                                {}
                                """.format("\n".join(lines))
                                file.write()
                            break
                        else:
                            lines.append(cl)
                except ValueError:
                    print("ERROR: Command does not exist.")
                    i -= 1
                    continue
        elif "modify" in mode:
            l = mode.replace("modify ")
            


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
        cmd.program(b)
    else:
        print("ERROR: Command does not exist.")    
