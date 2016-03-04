import sys, os
# thanks to http://stackoverflow.com/users/1364048/mohamed-samy
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def success( msg, others=None):
    print OKGREEN + msg, others if others != None else '', ENDC

def info( msg, others=None):
    print OKBLUE + msg, others if others != None else '', ENDC

def warn( msg, others=None):
    print WARNING + msg, others if others != None else '', ENDC

def err( msg, others=None):
    print FAIL + msg, others if others != None else '', ENDC
