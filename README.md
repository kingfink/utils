#### Installation

`pip install git+https://github.com/kingfink/utils.git`


#### Overview

These utilities reformat the contents of a users' clipboard, speeding up mundane tasks.

#### Replace model references with a specific schema

Clipboard contents (in):

```
SELECT * FROM {{ ref('my_model') }};
```

Example Commands:

`$ u dbt`

`$ u dbt --schema=analytics_prod`

Clipboard contents (out):

```
SELECT * FROM analytics_prod.my_model;
```

#### Reformat a list to include in an `IN`

Clipboard contents (in):

```
id
--
1
2
3
4
5
```

Example Commands:

`$ u lst`

`$ u lst --data_type=number --header_row=True`

Clipboard contents (out):

```
1,2,3,4,5
```

#### Another example of list reformatting, with strings and no header

Clipboard contents (in):

```
a
b
c
d
e
```

Example Commands:

`$ u lst`

`$ u lst --data_type=string --header_row=False`

Clipboard contents (out):

```
'a','b','c','d','e'
```
