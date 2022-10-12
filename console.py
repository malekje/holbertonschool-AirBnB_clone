#!/usr/bin/python3
""" console """


import cmd



class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    cmd.PROMPT = "(hbnb) "



    @classmethod
    def do_quit(self, args):
        """ Exit command """
        return True
    
    def do_EOF(self, args):
        """ Exit command """
        return True
    
    def emptyline(self):
        """empty line should not execute anything"""
        pass























if __name__ == '__main__':
    HBNBCommand().cmdloop()
