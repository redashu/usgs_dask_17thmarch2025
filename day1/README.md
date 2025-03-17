### Cloud -- The need of the day 

<img src="cl1.png">

### Dask with all possible Compute ENV 

<img src="cl2.png">

### Making Python ENV ready for Dask 

### Remote Linux Machine -- Connecting with SSH Protocol 

### From PowerShell / Terminal 
```sh
ssh ubuntu@54.172.190.69
```

### Python VENV 

<img src="cl3.png">

### Checking Python Version 

```sh
ubuntu@ip-172-31-24-249:~$ python3 -V
Python 3.12.3

# Install some extra Python related software 
```

### Creating VENV in Python 

```sh
ubuntu@ip-172-31-24-249:~$ python3 -m venv ashu-env 
ubuntu@ip-172-31-24-249:~$ ls
ashu-env
```

### Activating Python VENV 

```sh
ubuntu@ip-172-31-24-249:~$ source ashu-env/bin/activate
(ashu-env) ubuntu@ip-172-31-24-249:~$ 
```

### Some Basic Data Structures in Python 

```python
(ashu-env) ubuntu@ip-172-31-24-249:~$ python3
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> tuple()
()
>>> list()
[]
>>> dict()
{}
>>> 

# Creating tuple 
>>> t1 = (1, 2, 3, 100)
>>> t1
(1, 2, 3, 100)
>>> type(t1)
<class 'tuple'>
>>> len(t1)
4

>>> t2 = (1, 2, 4, 100, "hello world", 4.5)
>>> type(t2)
<class 'tuple'>
>>> len(t2)
6

>>> t1
(1, 2, 3, 100)
>>> t1[0]
1
>>> t1[2]
3
```

### Tuple Basic Info 

<img src="tup1.png">

### Some Basic Info About List 

```python
>>> l1 = [2, 6, 1, 9]
>>> type(l1)
<class 'list'>
>>> l1
[2, 6, 1, 9]

>>> l2 = [2, 66, 11, 99, 5.3, "hello dask"]
>>> len(l2)
6

>>> l1
[2, 6, 1, 9]
>>> l1.append(100)
>>> l1
[2, 6, 1, 9, 100]

>>> l1.insert(0, 878)
>>> l1
[878, 2, 6, 1, 9, 100]
>>> l1.append(t1)
>>> l1
[878, 2, 6, 1, 9, 100, (1, 2, 3, 100)]
```

### Dict in Python 

```python
>>> d1 = {1: "ashu", 9: 100, "hi": 8000}
>>> d1
{1: 'ashu', 9: 100, 'hi': 8000}
>>> d1.keys()
dict_keys([1, 9, 'hi'])
>>> d1.values()
dict_values(['ashu', 100, 8000])

>>> d1[9]
100
>>> d1
{1: 'ashu', 9: 100, 'hi': 8000}
>>> d1[2] = 1000
>>> d1
{1: 'ashu', 9: 100, 'hi': 8000, 2: 1000}
```

### Limitations in Python Data Structure 

<img src="ds1.png">

### For Big Data Pipeline Transformation Temp Results Also Lead to OOM Error 

<img src="ds2.png">

### Intro to Python Dask 

<img src="ds3.png">

Dask is a flexible, open-source library for parallel computing in Python. It is designed to scale Python code from single machines to large clusters, enabling efficient handling of larger-than-memory datasets and parallelizing computations. Dask integrates seamlessly with the Python ecosystem, including libraries like NumPy, pandas, and scikit-learn.
