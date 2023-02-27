#!/usr/bin/python3
""" Defines the console class """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command shell for hbnb """

    prompt = "(hbnb) "

    def emptyline(self):
        """Ignores empty prompts"""
        pass

    def do_EOF(self):
        """Quits CMD at EOF"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, *args):
        """Creates a new instance of Basemodel"""
        if args[0] == "":
            print("** class name missing **")
        else:
            try:
                new_model = None
                new_model = eval(f"{args[0]}()")
                print (new_model.id)
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
