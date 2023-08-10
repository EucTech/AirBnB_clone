#!/usr/bin/python3
"""This is the console for the Airbnb"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
