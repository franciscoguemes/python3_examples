# Rename Files App
This a Python based that renames files in batch mode.

## Usage
THe application can be used in the command line in the following ways

```bash
$ rename files --filter ".py" --old "[0-9][0-9]" -new "04d"
```

* TODO: Define the format of the _--new_ option. A possibility could be the formating 
of the strings in Java/Python. It can also be some SQL funciton imput, etc ...

Let's assume we have a directory with the following files
```
01-first.py
02-second.py
03-third.py
my-app.py
README.md
```

The expected result of the given command will be:
```
0000-first.py
0001-second.py
0002-third.py
my-app.py
README.md
```

The application will only have into account the files that have the ".py" extension because it is 
defined like that in the filter.

From the filtered files the application will try to match the regex supplied in the _--old_ option.
If the expression is matched then the application will try to replace with the given expression in
the _--new_ option. In this case a number of 4 digits. 
