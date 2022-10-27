# AirBnB clone - The console
![hbnb_logo](https://user-images.githubusercontent.com/31927278/195620241-be19cc9d-7bda-4120-bdc4-baa3333882b3.png)
Description :package:
======
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

# Execution :small_blue_diamond:
## Interactive
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

Models used in this project :dart:
======
| File | Description |
| ------ | ----------- |
| [base_model.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)  | BaseModel class for all classes. |
| [user.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/user.py) | User class. |
| [city.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/city.py)   | City class. |
| [place.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/place.py)   | Place class. |
| [state.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/state.py)   | State class. |
| [amenity.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/amenity.py)   | Amenity class. |
| [review.py](https://github.com/malekje/holbertonschool-AirBnB_clone/blob/main/models/review.py)   | Review class. |

How to use the commands :white_check_mark:
======
| Commands | Usage |
| ------ | ----------- |
| `help`  | displays all commands available. | 
| `create` | creates new object (ex. a new User, Place).| 
| `update`   | 	updates attribute of an object. |
| `destroy`   | destroys specified object. |
| `show`   | retrieve an object from a file, a database. |
| `all`   | display all objects in class. |
| `quit`   | exits the program. |


# Built With
+ Language: Python3
+ Style guidelines: Pep8

Authors ✒️
======
+ [Malek Mayeh](https://github.com/malekje)
