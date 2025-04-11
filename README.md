# nc (number counter)

nc is a small program that displays how many times a number was entered, and how many unique numbers were entered.

## Requirements

- Python 3.x

## Usage

### Windows:
 
```
python nc.py
```

### Mac / Linux:
 
```
chmod +x nc.py
./nc.py
```

## Example

```
$ ./nc.py

Begin entries. To delete the last entry, enter 'del'. To stop, enter an empty line.
-> 9
[9]
-> 30
[9, 30]
-> del
[9]
-> 300
[9, 300]
-> 400
[9, 300, 400]
-> 400
[9, 300, 400, 400]
-> 400.20 
[9, 300, 400, 400, 400.2]
-> 
Done.

Total numbers: 5
Total unique numbers: 4

9: 1
300: 1
400: 2
400.2: 1
```
