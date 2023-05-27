import os.path as osp

def FileExist(file):
    if osp.isfile(file):
        return True
    else:
        return False

def IsEmptyLine(line):
    return len(line.strip()) == 0


def RemoveEmptyLines(file):
    if not FileExist(file):
        print ("file non found!!")
        return
    temp=list()
    f = open(file,"r+")
    d = f.readlines()
    f.close()
    for line in d:
        if line.strip():
            temp.append(line)

    f=open(file,"w")
    f.writelines(temp)
    f.close()


#'E:\\OneDrive\\Python\\paolo\\pnr.txt'