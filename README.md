# nc (number counter)

nc is a small program that counts the total amount of times a given number is 
entered.

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

Enter numbers. To stop, enter an empty line.
-> 1
[1]
-> .34
[1, 0.34]
-> 4
[1, 0.34, 4]
-> 1
[1, 0.34, 4, 1]
-> 4
[1, 0.34, 4, 1, 4]
-> 1
[1, 0.34, 4, 1, 4, 1]
-> 
Done.

Total numbers: 6
Total unique numbers: 3

0.34: 1
1: 3
4: 2
```

