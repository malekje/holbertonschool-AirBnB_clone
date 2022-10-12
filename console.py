#!/usr/bin/python3
""" console """


from ast import arg
import cmd
from hashlib import new
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "

    classes = ["BaseModel"]

    @classmethod
    def do_quit(self, args):
        """ Exit command """
        return True
    
    def do_EOF(self, args):
        """ Exit command """
        return True
    
    def emptyline(self):
        """ Empty line should not execute anything """
        pass
    
    def do_create(self, args):
        """Creates new instance of BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if args[0] == 1:
            print("** instance id missing **")
            return
        else:
            total_obj = storage.all()
            new_entry = args[0] + "." + args[1]
            if new_entry in total_obj:
                print(total_obj[new_entry])
            else:
                print("** no instance found **")


    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
    
    def do_all(self, args):
        """Prints all string representation of all instances """
    
    def do_update(self, args):
        """Updates an instance based on the class name and id"""
    



















if __name__ == '__main__':
    HBNBCommand().cmdloop()
