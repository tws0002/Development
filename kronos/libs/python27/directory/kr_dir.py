import os

def currentmkdir(path,name):
    """
    En...
    This func is create currentfolder
    Sample***
    currentmkdir(r"H:/user","WORK")
    ======current_dir=====
                |
                |--WORK

    """
    try:
        os.mkdir(path + "//"+name)

    except OSError:
        pass



def expanmkdirs(path,*args):
    """
    En...
    This func is create currentfolders
    Sample***
    expanmkdirs(r"H:/user","WORK","TEST","CACHE")
    ======current_dir=====
                |
                |--WORK
                |--TEST
                |--CACHE

    """

    try:
       for i in args:
           os.makedirs(path + "\\" + str(i))

    except OSError:
        pass



def setProjects(path,projectname,*args):
    """
    En...
    This func is create project set
    Sample***
    expanmkdirs(r"H:/user","WORK","TEST","CACHE")
    ======current_dir=====
                |
                |            |--WORK
                |--Project --|--TEST
                             |--CACHE
    
    """

    root = str(projectname)

    try:
       for childdir in args:
           expanmkdirs(path + "\\" + root + "\\", str(childdir))
    except OSError:
        pass
