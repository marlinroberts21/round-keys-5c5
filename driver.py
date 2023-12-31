#!/usr/local/bin/python3

import subprocess, os

def main():
    # main
    # subprocess.call(["ls","-al"])

    completedProcess = subprocess.run(["python3","pyArgTest1.py","-a", "adjectives.txt", "-n", "nouns.txt"], capture_output=True)
    projectName = completedProcess.stdout.decode("utf-8").strip()
    
    os.mkdir(projectName)
    os.chdir(projectName)
    
    print(os.getcwd())
    
    
    
    print(projectName)

if __name__ == "__main__":
    main()