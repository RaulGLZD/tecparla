from pathlib import Path

def leeLis(*ficlis):
    lista =[]
    
    for fichero in ficlis:
        with open(fichero, 'rt') as fplis:   #filepointer
            lista += [palabra.strip() for palabra in fplis]
    
    return lista

def pathName(dir, nom, ext):
    """
    Construye el path completo del fichero a partir de su
    direccion, nombre de señal y extension.

    El resultado es un objeto de la clase 'Path'
    """
    return dir + '/' + nom + '.' + ext

def chkPathName(path):

    Path(path).parent.mkdir(parents = True , exist_ok= True)