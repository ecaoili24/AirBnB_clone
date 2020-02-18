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
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])()
        except:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        flag = 0
        dict_obj = storage.all()
        for key, value in dict_obj.items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                del dict_obj[key]
                storage.save()
                flag = 1
                break
        if flag == 0:
            print("** no instance found **")
            return

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in ["BaseModel", "User", "State", "City", "Place",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        flag = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                flag = 1
        if flag == 0:
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        else:
            model = storage.all()[".".join(arg_list[:2])]
            arg_list[3] = arg_list[3].strip('\"')
            if arg_list[3].isdigit():
                arg_list[3] = int(arg_list[3])
            setattr(model, arg_list[2], arg_list[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
