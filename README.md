# CALCGRAD

A simple autodiff engine in Python.

## Features

- Forward and backward automatic differentiation
- Computational graph
- Simple interface for gradients

## Usage

```python
from main import Variable

x = Variable(2.0)
y = Variable(3.0)
z = x * y + x
z.backward()

print(x.grad)
print(y.grad)
