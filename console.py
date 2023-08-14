#!/usr/bin/python3
"""This is the console for the Airbnb"""

import cmd
import sys
import shlex
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """This is the cmd class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Function that exits the program with quit"""
        return True

    def do_EOF(self, arg):
        """This function handles end of file
            when Ctrl+D is used
        """
        return True

    def emptyline(self):
        """should not do anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if arg is None:
            print("** class name missing **")
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        # gets the class name
        obj = storage.classes()[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        if args is None:
            print("** class name missing **")
            return
        else:
            argss = args.split()
            if argss[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(argss) < 2:
                print("** instance id missing **")
                return

            key = f"{argss[0]}.{argss[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        argss = args.split()
        if len(argss) < 1:
            print("** class name missing **")
            return

        if argss[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(argss) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(argss[0], argss[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        argss = shlex.split(args)
        if argss:
            if argss[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in storage.all().items()
                      if type(value).__name__ == argss[0]])
        else:
            print([str(value) for key, value in storage.all().items()])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        value = shlex.split(args)
        if len(value) == 0:
            print("** class name missing **")
            return
        if value[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(value) < 2:
            print("** instance id missing **")
            return

        ins_id = value[1]
        # check if the instance exists using
        # the id and classname
        key = f"{value[0]}.{ins_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]

        try:
            if len(value) < 3:
                print("** attribute name missing **")
                return
                # checking if the attribute has no value
            if len(value) < 4:
                print("** value missing **")
            else:
                attr_name = value[2]
                attr_value = value[3].strip('"')

                # setattr(obj, attr_name, eval(attr_value))
                setattr(obj, attr_name, attr_value)
        except Exception as e:
            pass
            storage.save()

    def do_count(self, line):
        """
            This function counts the number of instances
            in a class
        """
        count = 0
        cls_name = line
        obj = storage.all()
        for key in obj.keys():
            val = key.split('.')
            if val[0] == cls_name:
                count += 1
        print(count)

    def default(self, line):
        """
            This gets all the instance of the class
        """
        value = line.split('.')
        if value[1] == "all()":
            self.do_all(value[0])

        elif value[1] == "count()":
            self.do_count(value[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
