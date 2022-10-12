#!/usr/bin/python3
""" console """


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "



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























if __name__ == '__main__':
    HBNBCommand().cmdloop()
