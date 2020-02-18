# The Console: 0x00. AirBnB clone

> This project is the first step of the AirBnB clone. The goal of the project was
to create a command interpreter that can:
>	- create a new object (eg. a new User or a new Place)
>	- retrieve an object from a file
>	- do operations on objects (count, compute stats, etc.)
>	- update attributes of an object
>	- destroy an object
	
| Directory | Description |
|--|--|
| Models | contains all the classes used (eg. `BaseModel`, `User`, `City`, etc.)
| Models/Engine | contains all storage classes
| Tests | contains all unit tests

### Usage

The following is how the interpreter works in interactive mode.

`help`: displays the commands the interpreter can use

```
~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit  show  update
```

`create`: creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`

```
(hbnb) create BaseModel
555447df-ef1a-4fcb-8d6f-cd79e309ad40
```


`quit`: command to exit the interpreter

```
(hbnb)
(hbnb) exit
*** Unknown syntax: exit
(hbnb)
(hbnb) quit
~/AirBnb_clone$
```
