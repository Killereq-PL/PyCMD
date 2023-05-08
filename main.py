class cmdObject:
    def __init__(self):
        print("susCMD initialized")
        print("input 'help' to see all commands \n")
    def echo(self, arg1: str) -> None:
        print(arg1)
    def help(self):
        print("""commands: {
help (shows all commands),
echo <string>,
exit,
program <filename> (enters program mode)
}""")
    def program(self, filename: str) -> None:
        print("program mode enabled ("+filename+")")
        fn = filename+".sus"
        try:
            file = open(fn, 'r')
        except IOError:
            file = open(fn, 'w')
            file.mode = "r"
        if file.read() != "":
            print("program contents:")
            print(file.read())
            print("\n")
            lines = []
        else:
            lines = file.read().splitlines()
        file.mode = "r+"
        print("choose mode {modify <line> <modified>, run, overwrite, cancel}")
        cmds = ["finish", "echo", "delay"]
        mode = input("> ")
        if "overwrite" in mode:
            lines = []
            i = 0
            while True:
                i += 1
                cl = input(str(i)+" ")
                if cl in cmds: #TODO: FIX
                    lines.append(cl)
                else:
                    print("command does not exist")
                    i -= 1
                    continue

cmd = cmdObject()
while True:
    a = input("> "))
    if "echo" in a:
        b = a.replace("echo ", "")
        cmd.echo(b)
    if "exit" in a:
        break
    if "help" in a:
        cmd.help()
    if "program" in a:
        b = a.replace("program ", "")
        cmd.program(b)
