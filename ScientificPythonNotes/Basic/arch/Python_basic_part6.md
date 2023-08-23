# _Python for Scientific Data Analysis_


#  Basic Python

## Section 6: Dictionaries 

For lists, Python uses numbers to define indices.  E.g. things[1] means "the 2nd element of the list `things'".   A _dictionary_ goes a step further, you can use _anything_ to index a list: names, numbers, whatever.  

Here's an example of how it works:

```
stuff = {'name': 'Beavis', 'age': 15, 'weight': 145}
```

_stuff_ is a dictionary.   What is the 'name' in the dictionary? _Beavis_.  Age? _15_. Weight? _145_.  

You can pull up this information as follows:

```
stuff = {'name': 'Beavis', 'age': 15, 'weight': 145}
>>>print(stuff['name'])
Beavis
>>>print(stuff['age'])
15
>>>print(stuff['weight'])
145
```

Like with lists indexed by numbers, to grab the _dictionary_ value for a variable, you use the brackets '[ ]'.   

You can also add elements to a _dictionary_:

```
stuff['city']="Highland, Texas"
>>> print(stuff['city'])
Highland, Texas
```

You can also put things into the dictionary with strings.

```
stuff[1]="Settle Down Beavis"
stuff[2]="I dreamed I was at school last night"
```

Now ...

```
>>>print(stuff)
{'name': 'Beavis', 'age': 15, 'weight': 145, 'city': 'Highland, Texas', 1: 'Settle Down Beavis', 2: 'I dreamed I was at school last night'}
```

You can also delete elements of a dictionary:

```
>>> del stuff['weight']
>>> del stuff[2]
>>> print(stuff)
{'name': 'Beavis', 'age': 15, 'city': 'Highland, Texas', 1: 'Settle Down Beavis'}

```


Here's a more detailed example:

```
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)


```


This results in the following the following:

```
----------
NY State has:  New York
OR State has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has:  Detroit
Florida has:  Jacksonville
----------
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
----------
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
----------
Oregon state is abbreviated OR and has city Portland
Florida state is abbreviated FL and has city Jacksonville
California state is abbreviated CA and has city San Francisco
New York state is abbreviated NY and has city New York
Michigan state is abbreviated MI and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist

```