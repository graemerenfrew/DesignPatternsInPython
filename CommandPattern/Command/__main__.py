from create_order import CreateOrder
from ship_order import ShipOrder
from update_order import UpdateOrder
from no_command import NoCommand
#doing it this way is a bit crap, as we're effectively hardcoding the possible options
#we could overcome this by putting all in a package, and import * at runtime

import sys

def get_commands():
    ''' build a dictionary of possible command '''
    commands = (CreateOrder, UpdateOrder, ShipOrder)  #crap!
    return dict([cls.name, cls] for cls in commands)

def print_usage(commands):
    ''' if no commands are supplied'''
    print("usage : python3 -m Command CommandName [arguments]")
    print("Commands:")
    for command in commands.values():
        print('  %s' % command.description)

def parse_command(commands, args):
    ''' setdefault looks up the command supplied and if found it will return a reference to that command class '''
    command = commands.setdefault(args[0], NoCommand)
    return command(args)

commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

#find and exec the command
command = parse_command(commands, sys.argv[1:])
command.execute()