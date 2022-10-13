# AirBnB clone - The console
![hbnb_logo](https://user-images.githubusercontent.com/31927278/195620241-be19cc9d-7bda-4120-bdc4-baa3333882b3.png)
Desciption :package:
======
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

# Execution
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Non interactive 
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
Testing 📏
======
Unittests for the HolbertonBnB project are defined in the [tests](https://github.com/malekje/holbertonschool-AirBnB_clone/tree/main/tests) folder. To run the entire test suite simultaneously, execute the following command:
```
$ echo "python3 -m unittest discover tests" | bash
```
Authors ✒️
======
+ [Malek Mayeh](https://github.com/malekje)
