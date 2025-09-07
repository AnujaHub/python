## Indentation in Python

indentation is part of the syntax and changes how the code runs.

- **Purpose**: Defines code blocks (loops, conditionals, functions, etc.).
- **Rule**: Consistent spaces or tabs (PEP 8 recommends 4 spaces).
- **Error**: Incorrect indentation causes `IndentationError` — Python won't run the code.
- **Example**:

```python
if True:
    print("Indented block")  # ✅ Correct
print("Outside block")       # ✅ Correct

if True:
print("Error")               # ❌ Incorrect indentation

```

## Tips

Always typecast first, then do math 😃

Keep indentation consistent (don’t mix tabs and spaces).

Use comments # to make code easier to understand.

```python
s = "H e l l o"

#  0  1  2  3  4   → positive indexes (left to right)
# -5 -4 -3 -2 -1   → negative indexes (right to left)

```

## Docstring

The first string after the function is called the **Document string** or **Docstring** in short.  
It is used to describe the functionality of the function.

The use of docstring in functions is optional, but it is considered a good practice.

### Example

```python
def greet():
    """
    This function prints a greeting message.
    """
    print("Hello, World!")

print(greet.__doc__)
```

## Arbitrary Keyword Arguments in Python

In Python, we can pass a variable number of arguments to a function using special symbols. These are useful when the number of inputs is not fixed.

### 1. `*args` (Non-Keyword Arguments)

- Used to pass a variable number of **non-keyworded** arguments.
- Inside the function, `args` behaves like a tuple containing all the values passed.

### 2. `**kwargs` (Keyword Arguments)

- Used to pass a variable number of **keyworded** arguments.
- Inside the function, `kwargs` behaves like a dictionary, where keys are argument names and values are their corresponding values.

These features make Python functions more flexible and adaptable.
