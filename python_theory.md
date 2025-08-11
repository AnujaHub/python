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

tips:
Always type cast first, then do math:
