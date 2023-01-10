# Calculate Rankings

Calculates the results of a league. 

The team results are sorted from the top (Winners) to the bottom (Losers)
Teams with the same league score are given the same Rank

Example: 
1. Tarantulas: 6 pts
2. Lions: 5 pts
3. FC Awesome: 1 pts
3. Snakes: 1 pts
5. Grouches: 0 pts

Game results can be manually inserted or imported from a file.
Results are stored while the program is running so multiple inputs can be made.
And the results can be printed at the end.

Here is an example of a file to import:

```txt
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

#### FORMAT RULES
- Results are not imported if a line contains the incorrect formats
- Teams cannot be the same
- No empty lines are allowed
- Team names can contain more than one word




## Usage
- Python 3.11.1 is required.
- No additional libraries are required.

### Run program
Navigate into the src directory and run:
```python
python Main.py
```
### Run tests
Navigate into the tests folder and run:
```python
python -m unittest test_Calculate_Rankings.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)