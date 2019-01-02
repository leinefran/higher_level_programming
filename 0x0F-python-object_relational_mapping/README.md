# 0x0F. Python - Object-relational mapping

### This project in the Higher Level Programming series is about:

 * How to connect to a MySQL database from a Python script
 * How to SELECT rows in a MySQL table from a Python script
 * How to INSERT rows in a MySQL table from a Python script
 * What ORM means
 * How to map a Python Class to a MySQL table

## Requirements for Python scripts
 * Allowed editors: vi, vim, emacs
 * Your files will be executed with MySQLdb version 1.3.x
 * Your files will be executed with SQLAlchemy version 1.2.x
 * All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
 * All your files should end with a new line
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file, at the root of the folder of the project, is mandatory
 * Your code should use the PEP 8 style (version 1.7.*)
 * All your files must be executable
 * The length of your files will be tested using wc
 * All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
 * All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
 * All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

---
File|Task
---|---
0-select_states.py | a script that lists all states from the database hbtn_0e_0_usa
1-filter_states.py | a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
2-my_filter_states.py | a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
3-my_safe_filter_states.py | a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument, and that is safe from MySQL injections
4-cities_by_state.py | a script that lists all cities from the database hbtn_0e_4_usa
5-filter_cities.py | a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
model_state.py | a python file that contains the class definition of a State and an instance Base = declarative_base()
7-model_state_fetch_all.py | a script that lists all State objects from the database hbtn_0e_6_usa
8-model_state_fetch_first.py | a script that prints the first State object from the database hbtn_0e_6_usa
9-model_state_filter_a.py | a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
10-model_state_my_get.py | a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
11-model_state_insert.py | a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
12-model_state_update_id_2.py | a script that changes the name of a State object from the database hbtn_0e_6_usa
13-model_state_delete_a.py | a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
model_city.py | a Python file similar to model_state.py named model_city.py that contains the class definition of a City
14-model_city_fetch_by_state.py | a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa


## Author
Leine Valente