from config import *
import socket

import sys

import listen
import node
import server

### mainflags ###
ra_node = False
ra_server = False
ra_listen = False

config = False # use config and ignore argv
debug = False # show more output and use developer token

s_bot = False # start discord bot

node_port = "1234"
node_ip = '127.0.0.1'

db_user = "pySerMoSo"
db_pass = "supersecretpassword"
db_name = "PSMS"

token = ""
dev_token = ""

### initialization message ###
def init_msg():
    global ra_listen
    global ra_node
    global ra_server
    global node_port
    global node_ip
    global interval
    global db_user
    global db_pass
    global db_name
    global dev_token
    
    success = True
    
    print("[DEBUG] Initialization:")
    
    if ra_node == True:
        print("[DEBUG] Starting NODE")
    elif ra_server == True:
        print("[DEBUG] Starting SERVER")
    elif ra_listen == True:
        print("[DEBUG] Starting LISTEN")
        
    print("[DEBUG] Node port: ", node_port)
    print("[DEBUG] Node IP-Address: " + node_ip)
    print("[DEBUG] Node Interval: ", interval)
    print("[DEBUG] Database user: " + db_user)
    print("[DEBUG] Database password: " + db_pass)
    print("[DEBUG] Discord dev token: " + dev_token)
    if len(str(dev_token)) < 72:
        print("[ERROR] Developer token is to short")
        print("[ERROR] Stopping the Startup!")
        success = False
        
    return success

### start up sequence ###
def startup():
    success = True
    if config == True:
        global node_port
        global node_ip
        global interval
        global db_user
        global db_pass
        global db_name
        global token
        global dev_token
        
        node_port = NODE_PORT
        node_ip = NODE_IP
        interval = INTERVAL
        db_user = DB_USER
        db_pass = DB_PASS
        db_name = DB_NAME
        token = TOKEN
        dev_token = DEV_TOKEN
        print("[DEBUG] *** Using config.py for parameter ***")
    if debug == True:
        success = init_msg()
    
    if success:
        print("Starting pySerMoSo...")

#### help message ###
def help():
    print("insert help here")

### parse argument ###
def split_argv(argv, index):
    separator = ':'
    sargv = argv.split(separator,1)[index]
    return sargv

### switch arguments
def switch(argv):
    global ra_server
    global ra_node
    global ra_listen
    global node_port
    global node_ip
    global interval
    global db_user
    global db_pass
    global db_name
    global token
    global dev_token
    global config
    global debug
    
    if argv == "--help" or argv == "-h":
        help()
        return True # to stop the startup
    
    elif argv == "--node" or argv == "-n":
        if ra_server == False and ra_listen == False:
            ra_node = True
        else:
            print("[ERROR] Only spezify one working mode")
            return True
    elif argv == "--server" or argv == "-s":
        if ra_node == False and ra_listen == False:
            ra_server = True
        else:
            print("[ERROR] Only spezify one working mode")
            return True
    elif argv == "--listen" or argv == "-l":
        if ra_server == False and ra_node == False:
            ra_listen = True
        else:
            print("[ERROR] Only spezify one working mode")
            return True
        
    elif argv == "--debug" or argv == "-d":
        debug = True
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
        return True


### initialization ###

if __name__ == "__main__":

    interval = 1
    
    stop = False
    
    for i, arg in enumerate(sys.argv):
        if i > 0:
            stop = switch(str(sys.argv[i]))
        elif stop:
            break
        elif len(sys.argv) == 1:
            stop = True
        
    if stop:
        help()
        exit()
        
    startup()
    
    if ra_node:
        node.start()
    elif ra_server:
        server.start()
    elif ra_listen:
        listen.start()