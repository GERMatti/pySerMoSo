from config import *
import socket

import sys
import listen
import node

### mainflags ###
ra_node = False
ra_server = False
ra_listen = False

config = False # use config and ignore argv
debug_o = False # show more output and use developer token

s_bot = False # start discord bot

node_port = "1234"
node_ip = '127.0.0.1'

db_user = "pySerMoSo"
db_pass = "supersecretpassword"
db_name = "PSMS"

token = ""
dev_token = ""

interval = 1


### start up sequence ###
def startup():
    if debug_o == True:
        print('asd')
        init_msg()
    elif config == True:
        node_port = NODE_PORT
        node_ip = NODE_IP
        interval = INTERVAL
        db_user = DB_USER
        db_pass = DB_PASS
        db_name = DB_NAME
        token = TOKEN
        dev_token = DEV_TOKEN
    
    print("Starting pySerMoSo...")

def init_msg():
    print("insert init message here")

#### help message ###
def help():
    print("insert help here")

### parse argument ###
def split_argv(argv, index):
    separator = ':'
    sargv = argv.split(separator,1)[index]
    return sargv

### switch arguments ### FIX NOT ACCESSABLE VALUES ### idk maybe put bool on other file?! ###
def switch(argv):
    if argv == "--help" or argv == "-h":
        help()
        return True # to stop the startup
    
    elif argv == "--node" or argv == "-n":
        if ra_server == True or ra_listen == True:
            ra_node == True
        else:
            print("[ERROR] You already parsed a working mode")
    elif argv == "--server" or argv == "-s":
        if ra_node == True or ra_listen == True:
            ra_server == True
        else:
            print("[ERROR] You already parsed a working mode")
    elif argv == "--listen" or argv == "-l":
        if ra_server == True or ra_node == True:
            ra_listen == True
        else:
            print("[ERROR] You already parsed a working mode")
        
    elif argv == "--debug" or argv == "-d":
        debug_o = True
    elif argv == "--config" or argv == "-c":
        config = True
        
    elif split_argv(argv, 0) == "--port" or split_argv(argv, 0) == "-p":
        node_port = split_argv(argv, 1)
    elif split_argv(argv,0) == "--address" or split_argv(argv,0) == "-a":
        node_ip = split_argv(argv,1)
        
    elif split_argv(argv,0) == "--database_user" or split_argv(argv,0) == "-du":
        db_user = split_argv(argv,1)
    elif split_argv(argv,0) == "--database_pass" or split_argv(argv,0) == "-dp":
        db_pass = split_argv(argv,1)
    elif split_argv(argv,0) == "--database_name" or split_argv(argv,0) == "-dn":
        db_name = split_argv(argv,1)
        
    elif split_argv(argv,0) == "--token" or split_argv(argv,0) == "-t":
        token = split_argv(argv,1)
    elif split_argv(argv,0) == "--dev_token" or split_argv(argv,0) == "-dt":
        dev_token = split_argv(argv,1)
        
    elif split_argv(argv,0) == "--interval" or split_argv(argv,0) == "-i":
        interval = int(split_argv(argv,1))
    else:
        print("[ERROR] unknown argument'" + argv + "'")


### initialization ###

if __name__ == "__main__":
    
    stop = False
    
    for i, arg in enumerate(sys.argv):
        if i > 0:
            stop = switch(str(sys.argv[i]))
        elif stop:
            break
        elif len(sys.argv) == 1:
            stop = True
            help()
        
    if stop:
        exit()
    