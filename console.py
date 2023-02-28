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
        """Creates a new instance of a class.
        I.e.: create BaseModel"""
        if args[0] == "":
            print("** class name missing **")
        else:
            try:
                new_model = None
                new_model = eval(f"{args[0]}()")
                print (new_model.id)
                storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, *args):
        """ Prints the string representation of an instance based on
        the class name and id"""
        if args[0] == "":
            print("** class name missing **")
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                all_objs = storage.all()
                obj_class = eval(f"str({args[0]})")
                obj_id = args[1]
                obj = None
                for obj_class in all_objs.items():
                    for obj_id in all_objs.keys():
                        obj = all_objs[obj_id]
                        if obj.id == args[1]:
                            print(obj)
                        else:
                            obj = None
                if obj == None:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")


    def do_destroy(self, *args):
        """ destroys an instance based on the class name and id"""
        if args[0] == "":
            print("** class name missing **")
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                all_objs = storage.all()
                obj_class = eval(f"str({args[0]})")
                obj_id = args[1]
                obj = None
                for obj_class in all_objs.items():
                    for obj_id in all_objs.keys():
                        obj = all_objs[obj_id]
                if obj == None:
                    print("** no instance found **")
                else:
                    all_objs.pop(obj_id)
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")


    def do_all(self, *args):
        """ Prints all string representation of all instances based or not on
        the class name.
        Ex: $ all BaseModel or $ all. """
        all_objs = storage.all()
        if args[0] == "":
            for i in all_objs.keys():
                print(all_objs[i])
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            try:
                obj_class = eval(f"str({args[0]})")
                for obj_class in all_objs.items():
                    for i in all_objs.keys():
                        print(all_objs[i])
            except NameError:
                print("** class doesn't exist **")



    def do_update(self, *args):
        """Updates an instance based on the class name and id by adding or
        updating the attribute"""
        if args[0] == "":
            print("** class name missing **")
        else:
            args = "".join(args)
            args = tuple(map(str, args.split(" ")))
            all_objs = storage.all()
            obj_class = eval(f"str({args[0]})")
            try:
                obj_id = args[1]
            except IndexError:
                print("** instance id missing **")
                return 0
            try:
                obj_attrib = args[2]
            except IndexError:
                print("** attribute name missing **")
                return 0
            try:
                new_value = args[3]
            except IndexError:
                print("** value missing **")
                return 0
            try:
                obj = None
                key = obj_class + "." + obj_id
                for key in all_objs.keys():
                        obj = all_objs[key]
            except NameError:
                print("** class doesn't exist **")
                return 0
            try:
                if obj == None:
                    print("** no instance found **")
                    return 0
                else:
                    obj.__dict__[args[2]] = eval(args[3])
            except Exception:
                obj.__dict__[args[2]] = args[3]
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
