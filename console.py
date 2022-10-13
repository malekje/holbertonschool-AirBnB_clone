#!/usr/bin/python3
""" console """


from ast import arg
import cmd
from hashlib import new
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "

    classes = ["BaseModel", "State", "City", "Amenity", "Place", "Review"]

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
    
    def do_create(self, arg):
        """Creates new instance of BaseModel"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval("{}()".format(args[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        total_obj = storage.all()
        new_entry = args[0] + "." + args[1]
        if new_entry in total_obj:
            print(total_obj[new_entry])
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            new_object = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            delete_item = False
            for key in all_obj.keys():
                if new_object == key:
                    delete_item = True
            if delete_item == True:
                del all_obj[new_object]        
                storage.save()
            else:
                print("** no instance found **")
            

    def do_all(self, args):
        """ Prints all string representation of all instances """
        args = args.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            str_list = []
            for v in storage.all().values():
                if len(args) > 0 and args[0] == v.__class__.__name__:
                    str_list.append(v.__str__())
                    print(str_list)
                elif len(args) == 0:
                    str_list.append(v.__str__())
                    print(str_list)
                else:
                    print("** no instance found **")

    
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split(" ")
        obj = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if ("{}.{}".format(arg[0], arg[1])) not in storage.all().keys:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        else:
            print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
