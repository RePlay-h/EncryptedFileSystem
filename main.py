from time import sleep
from progress.bar import Bar
from hashlib import sha256

import os
from encrypted_file import EFile

def processHelloWorldFile(hello_file, password):
    try:

        # open a ".HelloWorld.txt"
        with open(hello_file, mode="r+", encoding="utf-8") as eHelloWorld:

            # if file hasn't got a password, we save it into the file
            if os.path.getsize(hello_file) == 0:
                eHelloWorld.write(password)
    
            #else the programm read hash of password and compare it with current hash
            else:
                hash_password = eHelloWorld.read()
                if password != hash_password:
                    return -1
        return 0
    
    # if specified path doesn't exist
    except OSError:
        print("Please, create " + hello_file)
        return -1

    
if __name__ == "__main__":

    # progress bar (just for fun)
    with Bar('Processing...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
    print("Welcome to  the eFiles ecosystem!")

    # path to the encrypted filesystem
    folder = input("Please, enter a path to your folder: ")
    hello_file = folder + "\\.HelloWorld.txt"

    password = input("Please, enter a password: ")

    # get a hash of password to compare it with password_hash in the ".HelloWorld.txt"
    hsh_password = sha256(bytes(password, "utf-8")).hexdigest()

    # if everything is gool than a function return 0, else -1
    if processHelloWorldFile(hello_file, hsh_password) == 0:
        delta = sum([ord(sym) for sym in password])
        print("You can input commands to work with efilesystem")
        print("1) emove -path_to_file1 -path_to_file2")
        print("2) decode -file")
        print("3) break (to stop work)")

        cmd_str = input(">")
        buf = None

        # just read command by command
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
            except:
                print("Please, write a command currectly")
            cmd_str = input(">")
            
    else:
        print("Password is uncurrect!")
            



    




