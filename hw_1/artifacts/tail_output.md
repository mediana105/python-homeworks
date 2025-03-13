## Output for empty file

### 1. `simple_tail`:
```bash
(venv) $ simple_tail hw_1/artifacts/files/empty_file
(venv) $
```

### 2. `tail`:
```bash
(venv) $ tail hw_1/artifacts/files/empty_file
(venv) $
```

## Output for long file
### 1. `simple_tail`:
```bash
(venv) $ simple_tail hw_1/artifacts/files/long_file
Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.      
Recommendations
Organisations and managers wanting to retain millennials should consider:

monitoring their workload and satisfaction levels with their work life balance
creating a flexible work culture where employees have more control over their working hours and their work location
providing meaningful work and interesting opportunities
offering help and support in continuing professional development
changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.(venv)
```

### 2. `tail`:
```bash
(venv) $ tail hw_1/artifacts/files/long_file
Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.      
Recommendations
Organisations and managers wanting to retain millennials should consider:

monitoring their workload and satisfaction levels with their work life balance
creating a flexible work culture where employees have more control over their working hours and their work location
providing meaningful work and interesting opportunities
offering help and support in continuing professional development
changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.(venv)
```

## Output for short file
### 1. `simple_tail`:
```bash
(venv) $ simple_tail hw_1/artifacts/files/short_file
This file contains less than 10 lines.
Hello world!

Fourth line

This is a test file.(venv) 
```

### 2. `tail`:
```bash
(venv) $ tail hw_1/artifacts/files/short_file
This file contains less than 10 lines.
Hello world!

Fourth line

This is a test file.(venv)
```

## Output for more than one file
### 1. `simple_tail`:
```bash
(venv) $ simple_tail hw_1/artifacts/files/long_file  hw_1/artifacts/files/short_file hw_1/artifacts/files/empty_file
==> hw_1/artifacts/files/long_file <==
Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.      
Recommendations
Organisations and managers wanting to retain millennials should consider:

monitoring their workload and satisfaction levels with their work life balance
creating a flexible work culture where employees have more control over their working hours and their work location
providing meaningful work and interesting opportunities
offering help and support in continuing professional development
changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.
==> hw_1/artifacts/files/short_file <==
This file contains less than 10 lines.
Hello world!

Fourth line

This is a test file.
==> hw_1/artifacts/files/empty_file <==
(venv)
```

### 2. `tail`:
```bash
(venv) $ tail hw_1/artifacts/files/long_file  hw_1/artifacts/files/short_file hw_1/artifacts/files/empty_file
==> hw_1/artifacts/files/long_file <==
Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.      
Recommendations
Organisations and managers wanting to retain millennials should consider:

monitoring their workload and satisfaction levels with their work life balance
creating a flexible work culture where employees have more control over their working hours and their work location
providing meaningful work and interesting opportunities
offering help and support in continuing professional development
changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.
==> hw_1/artifacts/files/short_file <==
This file contains less than 10 lines.
Hello world!

Fourth line

This is a test file.
==> hw_1/artifacts/files/empty_file <==
(venv)
```

## Output for a non-existent file
### 1. `simple_tail`:
```bash
(venv) $  simple_tail hw_1/artifacts/files/text
tail: hw_1/artifacts/files/text: No such file or directory
(venv) $
```

### 2. `tail`:
```bash
(venv) $  tail hw_1/artifacts/files/text
tail: cannot open 'hw_1/artifacts/files/text' for reading: No such file or directory
(venv) $
```

## Output for a path
### 1. `simple_tail`:
```bash
(venv) $  simple_tail hw_1/artifacts/files/
tail: hw_1/artifacts/files/: Is a directory
(venv) $
```

### 2. `tail`:
```bash
(venv) $  tail hw_1/artifacts/files/
tail: error reading 'hw_1/artifacts/files/': Is a directory
(venv) $
```

## Output for long stdin
### 1. `simple_tail`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\nLine11\nLine12\nLine13\nLine14\nLine15\nLine16\nLine17" | simple_tail
Line1
Line2
Line3
Line4
Line5
Line6
Line7
Line8
Line9
Line10
Line11
Line12
Line13
Line14
Line15
Line16
Line17
(venv) $
```

### 2. `tail`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\nLine11\nLine12\nLine13\nLine14\nLine15\nLine16\nLine17" | tail
Line8
Line9
Line10
Line11
Line12
Line13
Line14
Line15
Line16
Line17
(venv) $
```

## Output for short stdin
### 1. `simple_tail`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9" | simple_tail
Line1
Line2
Line3
Line4
Line5
Line6
Line7
Line8
Line9
(venv) $
```

### 2. `tail`:
```bash
(venv) $ echo -e "Line1\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9" | tail
Line1
Line2
Line3
Line4
Line5
Line6
Line7
Line8
Line9
(venv) $
```