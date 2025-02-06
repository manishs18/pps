import utilities as uti
import os

#print(uti.__name__)



if __name__=="__main__":
    print(uti.multiply(3,3))
    print(f'Current name of file: {__file__}')
    print(f'Dirctory of the file: {os.path.dirname(__file__)}')

