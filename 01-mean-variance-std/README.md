# Mean-Variance-Standard Deviation Calculator

## Problem
The goal was to create a function that takes a list of 9 digits and converts 
them into a 3x3 NumPy array. From that matrix, the function must calculate the 
mean, variance, standard deviation, max, min, and sum along both axes (rows and 
columns) as well as for the flattened matrix. The output must be returned as a 
specific dictionary format, and the function must raise a `ValueError` if the 
input list does not contain exactly 9 elements.

## What I built
A Python script using NumPy to handle matrix transformations and statistical 
calculations. The core logic involves:
- Validation: Ensuring the input list is the correct length before processing
- Reshaping: Using `.reshape(3, 3)` to transform a 1D list into a 2D matrix
- Axis-specific logic: Calculating statistics for columns (axis=0) and rows (axis=1)
- Data formatting: Converting NumPy arrays to Python lists using `.tolist()`

## How to run
```bash
python main.py
```

## Key concepts learned
- Matrix dimensionality: How data is structured in a 3x3 grid vs a flat array
- NumPy axes: `axis=0` operates vertically (columns), `axis=1` horizontally (rows)

## Output example
```python
calculate([0,1,2,3,4,5,6,7,8])

{
  'mean':               [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance':           [[6.0, 6.0, 6.0], [0.667, 0.667, 0.667], 6.667],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.582],
  'max':                [[6, 7, 8], [2, 5, 8], 8],
  'min':                [[0, 1, 2], [0, 3, 6], 0],
  'sum':                [[9, 12, 15], [3, 12, 21], 36]
}
```