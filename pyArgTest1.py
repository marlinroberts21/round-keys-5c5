#!/usr/local/bin/python3

import sys, getopt, random
from typing import List


def loadList(fileName: str, listObject: List[str]):
    """
    Summary:
        Loads a list of words from a file into a given list.

    Args:
        fileName (str): Name of file to load.
        listObject (List): List to hold words.
    """        
    with open(fileName, encoding="utf-8") as f:
        fullFile = f.readlines()
    for line in fullFile:
        listObject.append(line.strip())

def main(argv):
    """
    Summary:
        Generates project names in an adjective-noun-number format.
    Args:
        argv (str []): command line arguments.
        -a <adjectiveFile> -n <nounFile>
    """    
    
    # test comment
    adjectFile = '' 
    nounFile = ''

    try:
        opts, args = getopt.getopt(argv,"a:n:")
    except getopt.GetoptError:
        print ("Error parsing arguments. Usage:")
        print ('pyArgTest1.py -a <adjectFile> -n <nounFile>')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-a"):
            adjectFile = arg
        if opt in ("-n"):
            nounFile = arg
            
    if adjectFile == '' or nounFile == '':
        print ("Missing argument. Usage:")
        print ('pyArgTest1.py -a <adjectFile> -n <nounFile>')
        sys.exit()
    
    adjectList = []
    nounList = []
    
    loadList(adjectFile, adjectList)
    loadList(nounFile, nounList)   
    
    nounStr = random.choice(nounList)
    adjectStr = random.choice(adjectList)
    suffixInt = random.randint(1024,4096)
    
    finalStr = (f'{adjectStr.lower()}-{nounStr.lower()}-{hex(suffixInt).removeprefix("0x")}')
    print(finalStr)
    
    
    
if __name__ == "__main__":
    main(sys.argv[1:])