def loadLines(nomeFicheiro):
    try:
        file = open(nomeFicheiro,"r")
        something = file.read().splitlines()
        file.close()
        return something
    except:
        return ["Erro"]