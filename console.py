#!/usr/bin/python3
"""
The console for AirBnB clone, hbnb
"""
import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter. This is the entry point"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Handles empty spaces when you press ENTER"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates and saves new instance of BaseModel. Prints id"""
        if len(arg) < 1:
            print("**class name missing**")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])()
            obj.save()
            print(obj.id)
        except:
            print("** class doesn't exist**")
            return

    def do_show(self, arg):
        """prints the string representation of the instance
        based on class name and id"""
        if len(arg) < 2:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])()
        except:
            print("**class doesn't exist**")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        flag = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                print(value)
                flag = 1
        if flag == 0:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if len(arg_list) == 0:
            print("** class name missing **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
