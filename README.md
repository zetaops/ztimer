
##ZTimer ##

### Easy to use class based timing / benchmarking tool for Python ###

Define your test codes in a class that extends Timer class then run it:

```python


from ztimer import Timer, M


class DotDict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

dot_dict = DotDict({'a': 1})
a_dict = {'a': 1}

class MyTest(Timer):

    def dot_notation(self):
        dot_dict.a

    def bracket_notation(self):
        a_dict['a']

    def by_getter(self):
        a_dict.get('a')



MyTest(2*M)
    
MyTest() # equivalent to MyTest(M) or  MyTest(repeat=1000000, show_results=False, hide_unsorted=True) 
```
     

### Generates: ###

    Running dot_notation [ 3 / 3 ] 

    
    Each method run 2,000,000 times:
    
    bracket_notation   : 0.33024 sec  
    by_getter          : 0.5028 sec 1.5x slower 
    dot_notation       : 2.13898 sec 6.5x slower

