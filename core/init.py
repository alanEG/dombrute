import platform

def initFileSl():
    if platform.system() == "Windows":
        fileSl = '\\'
    else:
        fileSl = '/'
    return fileSl