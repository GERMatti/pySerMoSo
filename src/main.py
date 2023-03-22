from config import *
import socket

import sys
import gui
import node


if __name__ == "__main__":
    #print(f"Arguments count: {len(sys.argv)}")
    
    #for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")
        
    print(f"Name of the script      : {sys.argv[0]=}")
    print(f"Arguments of the script : {sys.argv[1:]=}")
    
    if sys.argv[1:] == ['node']:
        print("node")
    