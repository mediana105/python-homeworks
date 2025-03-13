## Output for empty file

### 1. `simple_wc`:
```bash
(venv) $ simple_wc hw_1/artifacts/files/empty_file
0 0 0 hw_1/artifacts/files/empty_file
(venv) $
```

### 2. `wc`:
```bash
(venv) $ wc hw_1/artifacts/files/empty_file
0 0 0 hw_1/artifacts/files/empty_file
(venv) $
```

## Output for long file
### 1. `simple_wc`:
```bash
(venv) $ simple_wc hw_1/artifacts/files/long_file
24 369 2536 hw_1/artifacts/files/long_file
(venv)
```

### 2. `wc`:
```bash
(venv) $ wc hw_1/artifacts/files/long_file
  24  369 2536 hw_1/artifacts/files/long_file
```

## Output for short file
### 1. `simple_wc`:
```bash
(venv) $ simple_wc hw_1/artifacts/files/short_file
6 16 93 hw_1/artifacts/files/short_file
(venv) 
```

### 2. `wc`:
```bash
(venv) $ wc hw_1/artifacts/files/short_file
6 16 93 hw_1/artifacts/files/short_file
(venv)
```

## Output for more than one file
### 1. `simple_wc`:
```bash
(venv) $ simple_wc hw_1/artifacts/files/long_file  hw_1/artifacts/files/short_file hw_1/artifacts/files/empty_file
24 369 2536 hw_1/artifacts/files/long_file
6 16 93 hw_1/artifacts/files/short_file
0 0 0 hw_1/artifacts/files/empty_file
30 385 2629 total
```

### 2. `wc`:
```bash
(venv) $ wc hw_1/artifacts/files/long_file  hw_1/artifacts/files/short_file hw_1/artifacts/files/empty_file
  24  369 2536 hw_1/artifacts/files/long_file
   6   16   93 hw_1/artifacts/files/short_file
   0    0    0 hw_1/artifacts/files/empty_file
  30  385 2629 total
(venv)
```

## Output for a non-existent file
### 1. `simple_wc`:
```bash
(venv) $  simple_wc hw_1/artifacts/files/text
wc: hw_1/artifacts/files/text: No such file or directory
(venv) $
```

### 2. `wc`:
```bash
(venv) $  wc hw_1/artifacts/files/text
wc: hw_1/artifacts/files/text: No such file or directory
(venv) $
```

## Output for a path
### 1. `simple_wc`:
```bash
(venv) $  simple_wc hw_1/artifacts/files/
wc: hw_1/artifacts/files/: Is a directory
0 0 0 hw_1/artifacts/files/
(venv) $
```

### 2. `wc`:
```bash
(venv) $  wc hw_1/artifacts/files/
wc: hw_1/artifacts/files/: Is a directory
      0       0       0 hw_1/artifacts/files/
(venv) $
```

## Output for long stdin
### 1. `simple_wc`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\nLine11\nLine12\nLine13\nLine14\nLine15\nLine16\nLine17" | simple_wc
17 17 110
(venv) $
```

### 2. `wc`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\nLine11\nLine12\nLine13\nLine14\nLine15\nLine16\nLine17" | wc
     17      17     110
(venv) $
```

## Output for short stdin
### 1. `simple_wc`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9" | simple_wc
9 9 54
(venv) $
```

### 2. `wc`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9" | wc
9       9      54
(venv) $
```