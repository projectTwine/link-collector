import os, multiprocessing

# Dynamic Threading
CORES = (multiprocessing.cpu_count()) * 2
PROJECT_NAME = ''
HOMEPAGE = ''
PATH = ''


def Initiate():
    global PROJECT_NAME, HOMEPAGE, PATH
    # Linux clean command when using Linux terminal
    # print("\033c")
    PROJECT_NAME = input("Please enter Project name: ")
    # Linux clean command when using Linux terminal
    # print("\033c")
    HOMEPAGE = input("Please enter the url to crawl: ")
    # Linux clean command when using Linux terminal
    # print("\033c")
    print(
        "Please enter the directory path where the queue and crawled txt files will be store: ",
        end="")

    # This will contain Project path
    PATH = str(input())

    # We are checking if the user entered something
    if len(PATH.strip()) == 0:
        PATH = os.path.expanduser("~") + "\\Desktop\\"

    # This formats the path so the path is not deformed
    # error : Path\User/Project Name\files
    # Correction : Path/User/Project Name/files
    if "\\" in PATH:
        PATH = PATH.replace("\\", "/")
        if not PATH.endswith("/"):
            PATH += "/"


def getProjectName():
    global PROJECT_NAME
    return PROJECT_NAME


def getHomePage():
    global HOMEPAGE
    return HOMEPAGE


def getPath():
    global PATH
    return PATH


def getCores():
    global CORES

    # This checks if the CORES is none or zero
    if CORES is None or CORES == 0:
        CORES = 2

    return CORES
