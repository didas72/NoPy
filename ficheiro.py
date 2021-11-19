def loadLines(nomeFicheiro):
    try:
        file = open(nomeFicheiro,"r")
        something = file.read().splitlines()
        file.close()
        print(something)
    except:
        file = []
        pass

    return file