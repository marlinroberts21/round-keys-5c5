#!/usr/local/bin/python3

import sys, getopt, random
from typing import List

def main(argv):
    """
    Summary:
        Generates project names in an adjective-noun-number format.
    Args:
        argv (str []): command line arguments.
        -a <adjectiveFile> -n <nounFile.
    """    
    # print ('Number of arguments:', len(argv), 'arguments.')
    # print ('Argument List:', str(argv))

    # argvs = sys.argv[1:]

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
        
    # print (opts)
    # print (args)
    # print ('adject File: ', adjectFile)
    # print ('Noun File: ', nounFile)
    
    """
    with open(adjectFile, encoding="utf-8") as f:
        fullfile = f.readlines()
        for line in fullfile:
            adjectList.append(line.strip())

    with open(nounFile, encoding="utf-8") as f:
        fullfile = f.readlines()
        for line in fullfile:
            nounList.append(line.strip())
     """       
    
    """ 
    def load_list(file_name):
        tmp_list = []
        with open(file_name, encoding="utf-8") as f:
            fullfile = f.readlines()
        for line in fullfile:
            tmp_list.append(line.strip())
        return tmp_list
    """
    #adjectList = load_list(adjectFile)
    #nounList = load_list(nounFile)  
    
    def loadList(fileName: str, listObject: List):
        with open(fileName, encoding="utf-8") as f:
            fullFile = f.readlines()
        for line in fullFile:
            listObject.append(line.strip())

    adjectList = []
    nounList = []
    
    loadList(adjectFile, adjectList)
    loadList(nounFile, nounList)   
    
    # print(adjectList)
    # print(nounList)
    
    nounStr = random.choice(nounList)
    adjectStr = random.choice(adjectList)
    suffixInt = random.randint(1024,4096)
    
    finalStr = (f'{adjectStr.lower()}-{nounStr.lower()}-{hex(suffixInt).removeprefix("0x")}')
    print(finalStr)
    #print(f'{adjectStr.lower()}-{nounStr.lower()}-{hex(suffixInt).removeprefix("0x")}')
    #print(f'{adjectStr.lower()}-{nounStr.lower()}-{oct(suffixInt).removeprefix("0o")}')
    #print(f'{adjectStr.lower()}-{nounStr.lower()}-{bin(suffixInt).removeprefix("0b")}')
    

    return finalStr

if __name__ == "__main__":
    main(sys.argv[1:])