# The Console: 0x00. AirBnB clone

This project is the first step of the AirBnB clone. The goal of the project was
to create a command interpreter that can:
>	- create a new object (eg. a new User or a new Place)
>	- retrieve an object from a file
>	- update attributes of an object
>	- destroy an object
	
| Directory | Description |
|--|--|
| Models | contains all the classes used (eg. `BaseModel`, `User`, `City`, etc.)
| Models/Engine | contains the file `file_storage.py` that holds class `FileStorage`
| Tests | contains all unit tests

### Usage

The following is how the interpreter works in interactive mode.

`help`: displays the commands the interpreter can use

```
~/AirBnB_clone$ ./console.py
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit  show  update
```

`create`: creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`

```
(hbnb) create BaseModel
79ee3ea4-3851-4ceb-bf88-8bc535190ee4  # BaseModel id number
```

`show`: prints the string representation of an instance based on the class name and `id`
`update`: updates an instance based on the class name and `id` by adding or updating attribute (saves the change into the JSON file)

```
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
[BaseModel] (79ee3ea4-3851-4ceb-bf88-8bc535190ee4) {'id': '79ee3ea4-3851-4ceb-bf88-8bc535190ee4', 'created_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766357), 'updated_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766389)}
(hbnb)
(hbnb) update BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4 first_name "Betty"
(hbnb)
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
[BaseModel] (79ee3ea4-3851-4ceb-bf88-8bc535190ee4) {'first_name': 'Betty', 'updated_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766389), 'id': '79ee3ea4-3851-4ceb-bf88-8bc535190ee4', 'created_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766357)}
```

`destroy`: deletes an instance based on the class name and `id`

```
(hbnb) destroy BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
(hbnb)
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
** no instance found **
```

`quit`: command to exit the interpreter

```
(hbnb) exit
*** Unknown syntax: exit
(hbnb)
(hbnb) quit
~/AirBnb_clone$  # successfully exited the interpreter
```
