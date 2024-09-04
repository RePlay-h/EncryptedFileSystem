from time import sleep
from progress.bar import Bar
from hashlib import sha256

import os
from encrypted_file import EFile

def processHelloWorldFile(hello_file, password):
    try:
        with open(hello_file, mode="r+", encoding="utf-8") as eHelloWorld:

            if os.path.getsize(hello_file) == 0:
                eHelloWorld.write(password)
            else:
                hash_password = eHelloWorld.read()
                if password != hash_password:
                    return -1
        return 0
    except OSError:
        print("Please, create " + hello_file)
        return -1

    
if __name__ == "__main__":

    with Bar('Processing...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
    print("Welcome to  the eFiles ecosystem!")

    folder = input("Please, enter a path to your folder: ")
    hello_file = folder + "\\.HelloWorld.txt"

    password = input("Please, enter a password: ")
    hsh_password = sha256(bytes(password, "utf-8")).hexdigest()

    if processHelloWorldFile(hello_file, hsh_password) == 0:
        delta = sum([ord(sym) for sym in password])
        print("You can input commands to work with efilesystem")
        print("1) emove -path_to_file1 -path_to_file2")
        print("2) decode -file")
        print("3) break (to stop work)")

        cmd_str = input(">")
        buf = None
        while(cmd_str != "break"):
            cmd = cmd_str.split(" ")
            
            try:
                match cmd[0]:
                    case "emove": 
                        buf = EFile.read(cmd[1], 0)
                        EFile.encode(buf, delta)
                        EFile.writeBufferTo("".join(buf), cmd[2])
                        pass
                    case "decode":
                        buf = EFile.read(cmd[1], 1)
                        EFile.decode(buf, delta)
                        print("".join(buf))
                    case _:
                        print("Try a correct command")
            except IOError:
                print("Please, write a command currectly")
            cmd_str = input(">")
            
    else:
        print("Password is uncurrect!")
            



    




