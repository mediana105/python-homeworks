## Output for empty file

### 1. `simple_nl`:
```bash
(venv) $ simple_nl hw_1/artifacts/files/empty_file
(venv) $
```

### 2. `nl - b a`:
```bash
(venv) $ nl - b a hw_1/artifacts/files/empty_file
(venv) $
```

## Output for long file
### 1. `simple_nl`:
```bash
(venv) $ simple_nl hw_1/artifacts/files/long_file
     1  Millennials in the workplace
     2  Background
     3  Millennials (those born between the early 1980s and the early 1990s) make up a huge part of our workforce but they seem to lack loyalty to the companies and the leaders the
y work for. Multinational companies are noticing larger turnover rates of millennials as employee retention rates fall. This report looks at the findings of two large-scale surveys on the mindset of the millennial generation and explores how organisations can strive to address these needs, increase employee engagement and encourage retention.
     4
     5  Research
     6  In a global survey conducted by PricewaterhouseCoopers (PwC), more than 40,000 millennial (born between 1983 and 1993) and non-millennial responses were collected on the topics of workplace culture, communication and working styles, pay structure, career development, work–life balance, etc.
     7
     8  In a separate global survey conducted by Deloitte, more than 10,000 millennials participated in a study about their perceptions of the threats and opportunities in the complex world of work.
     9
    10  Key findings
    11  Millennials are as committed to their work as their more senior colleagues.
    12  Millennials value interesting work and a good work life balance. They do not believe that excessive work demands are worth sacrifices in their personal lives.
    13  Millennials want flexibility in their working hours and are willing to give up pay increases and promotions for a flexible working schedule. They believe that success should be measured by productivity and not by the number of hours they are seen in an office.
    14  Millennials want to feel supported and appreciated by their company and their superiors.
    15  Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
    16  Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.
    17  Recommendations
    18  Organisations and managers wanting to retain millennials should consider:
    19
    20  monitoring their workload and satisfaction levels with their work life balance
    21  creating a flexible work culture where employees have more control over their working hours and their work location
    22  providing meaningful work and interesting opportunities
    23  offering help and support in continuing professional development
    24  changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.
(venv) $
```

### 2. `nl -b a`:
```bash
(venv) $ nl -b a hw_1/artifacts/files/long_file
     1  Millennials in the workplace
     2  Background
     3  Millennials (those born between the early 1980s and the early 1990s) make up a huge part of our workforce but they seem to lack loyalty to the companies and the leaders the
y work for. Multinational companies are noticing larger turnover rates of millennials as employee retention rates fall. This report looks at the findings of two large-scale surveys on the mindset of the millennial generation and explores how organisations can strive to address these needs, increase employee engagement and encourage retention.
     4
     5  Research
     6  In a global survey conducted by PricewaterhouseCoopers (PwC), more than 40,000 millennial (born between 1983 and 1993) and non-millennial responses were collected on the topics of workplace culture, communication and working styles, pay structure, career development, work–life balance, etc.
     7
     8  In a separate global survey conducted by Deloitte, more than 10,000 millennials participated in a study about their perceptions of the threats and opportunities in the complex world of work.
     9
    10  Key findings
    11  Millennials are as committed to their work as their more senior colleagues.
    12  Millennials value interesting work and a good work life balance. They do not believe that excessive work demands are worth sacrifices in their personal lives.
    13  Millennials want flexibility in their working hours and are willing to give up pay increases and promotions for a flexible working schedule. They believe that success should be measured by productivity and not by the number of hours they are seen in an office.
    14  Millennials want to feel supported and appreciated by their company and their superiors.
    15  Millennials want more opportunities to develop their skills. These include technological skills, teamwork and interpersonal skills.
    16  Millennials believe that businesses and business leaders should contribute to the improvement of society and they are more likely to be loyal to a company with strong ethics.
    17  Recommendations
    18  Organisations and managers wanting to retain millennials should consider:
    19
    20  monitoring their workload and satisfaction levels with their work life balance
    21  creating a flexible work culture where employees have more control over their working hours and their work location
    22  providing meaningful work and interesting opportunities
    23  offering help and support in continuing professional development
    24  changing the organisations goals from being mainly about profit-making to motives that address social concerns and solve wider societal problems.
(venv) $ 
```

## Output for short file
### 1. `simple_nl`:
```bash
(venv) $ simple_nl hw_1/artifacts/files/short_file
     1  This file contains less than 10 lines.
     2  Hello world!
     3
     4  Fourth line
     5
     6  This is a test file.
(venv) $
```

### 2. `nl -b a`:
```bash
(venv) $ nl -b a hw_1/artifacts/files/short_file 
     1  This file contains less than 10 lines.
     2  Hello world!
     3
     4  Fourth line
     5
     6  This is a test file.
(venv) $ 
```

## Output for a non-existent file
### 1. `simple_nl`:
```bash
(venv) $  simple_nl hw_1/artifacts/files/text
nl: hw_1/artifacts/files/text: No such file or directory
(venv) $
```

### 2. `nl -b a`:
```bash
(venv) $  nl -b a hw_1/artifacts/files/text
nl: hw_1/artifacts/files/text: No such file or directory
(venv) $
```

## Output for a path
### 1. `simple_nl`:
```bash
(venv) $  simple_nl hw_1/artifacts/files/
nl: hw_1/artifacts/files/: Is a directory
(venv) $
```

### 2. `nl -b a`:
```bash
(venv) $  nl -b a hw_1/artifacts/files/
nl: hw_1/artifacts/files/: Is a directory
(venv) $
```

## Output for stdin
### 1. `simple_nl`:
```bash
(venv) $ simple_nl 
hello
     1  hello
world
     2  world

     3
sdkodfopdkfa
     4  sdkodfopdkfa
(venv) $
```

### 2. `nl -b a`:
```bash
(venv) $ nl -b a
hello
     1  hello
world
     2  world

     3
sdkodfopdkfa
     4  sdkodfopdkfa
(venv) $
```