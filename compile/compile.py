import os
import sys
import hashlib

def readFile(nameOfFile):
    '''return lines of file'''
    line = None
    with open(nameOfFile, encoding="utf-8") as f:
        line = f.readlines()
        for i in range(len(line)):
            line[i] = line[i].split("\n")[0]
    return line


file_compiler = "compiler.txt"
file_flags = "flags.txt"
file_output = "output.txt"
file_surse = "surse.txt"

os.chdir("compile")
compiler = readFile(file_compiler)
flags = readFile(file_flags)
output = readFile(file_output)
surse = readFile(file_surse)
HASH = {}

def getHASH(nameOfFile):
    has = hashlib.md5()
    with open(nameOfFile, "rb") as f:
        buf = f.read()
        has.update(buf)
    return has.hexdigest()

def readHASHs():
    part = readFile("hash.txt")
    for one in part:
        value = one.split(" ")
        HASH[str(value[0])] = str(value[1])

def saveHASHs():
    with open("hash.txt", "w" ,encoding="utf-8") as f:
        for one in HASH.keys():
            f.write(str(one) + " " + str(HASH[one]) + "\n")




def creteComand():
    ret = str(compiler[0])
    for one in flags:
        ret = ret + " " + str(one)
    return ret

def creteObjects():
    comand = creteComand()
    ret = False
    for one in surse:
        h1 = getHASH(os.path.join("files", str(one)))
        if HASH.keys().__contains__(str(one)):
            h2 = HASH[str(one)]
            if h1 != h2:
                ret = True
                print(comand + " -c " + os.path.join("files", str(one))\
                          + " -o " + os.path.join("objects", str(one).split(".")[0] + ".o"))
                os.system(comand + " -c " + os.path.join("files", str(one))\
                          + " -o " + os.path.join("objects", str(one).split(".")[0] + ".o"))
                HASH[str(one)] = h1
            else:
                print("File " + str(one) + " without change")
        else:
            ret = True
            print(comand + " -c " + os.path.join("files", str(one))\
                      + " -o " + os.path.join("objects", str(one).split(".")[0] + ".o"))
            os.system(comand + " -c " + os.path.join("files", str(one))\
                      + " -o " + os.path.join("objects", str(one).split(".")[0] + ".o"))
            HASH[str(one)] = h1
    return ret


def creteProgram(oneC):
    mainExist = False
    for one in os.listdir():
        if one.split(".")[0] == "main":
            mainExist = True
            break
    if oneC or (mainExist == False):
        command = creteComand() + " -C"
        for one in surse:
            part = one.split(".")
            command += " " + os.path.join("objects", str(part[0])) + ".o"
        print(command + " -o " + str(output[0]))
        os.system(command + " -o " + str(output[0]))
    else:
        print("None to compile")

def main():
    readHASHs()
    os.chdir("..")
    oneChange = creteObjects()
    creteProgram(oneChange)
    os.chdir("compile")
    saveHASHs()

if __name__ == '__main__':
    main()
