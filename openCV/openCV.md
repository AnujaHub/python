````markdown
# Handling Key Press in OpenCV

Use `cv.waitKey()` to listen for keys while showing video frames.

## Single Key (e.g., 'd' to quit)

```python
if cv.waitKey(20) & 0xFF == ord('d'):
    break
```
````

- `cv.waitKey(20)`: wait 20 ms for a key.
- `& 0xFF`: keeps last 8 bits (cross-platform).
- `ord('d')`: ASCII of 'd'.

## Multiple Keys ('d', 'q', or Esc)

```python
key = cv.waitKey(20) & 0xFF
if key in [ord('d'), ord('q'), 27]:  # 27 = Esc
    break
```

## Quit on Any Key

```python
if cv.waitKey(20) != -1:
    break
```

```

```
