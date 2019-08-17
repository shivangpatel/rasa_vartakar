# rasa_vartakar
It's a about making a stories in RASA from small chunks of conversation. Almost all possible way. 

*make a stories based on this idea.*

```
input = ['a', 'b', 'c', 'd']
output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
print(output)

Output: 
[[], ['a'], ['b'], ['c'], ['d'], ['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd'], ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]
```
