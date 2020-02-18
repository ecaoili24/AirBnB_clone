#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Does nothing on ENTER"""
        pass

    def do_create(self, arg):
       """Creates and saves new instance of BaseModel. Prints id"""
       if len(arg) < 2:
           print ("**class name missing**")
           return
       arglist = arg.split()
       try:
           b = eval(arglist[0])()
           b.save()
           print(b.id)
       except:
           print ("** class doesn't exist**")
           return











if __name__ == '__main__':
    HBNBCommand().cmdloop()
