
##ZTimer ##

### Easy to use class based code timer / benchmarking tool for Python ###

Define your test codes in a class that extends Timer class and call it:

    from timer import Timer
    
    
    class A(object):
        obj_cache = {'a': {}, 'b': 12345, 'c': []}
        def __getattribute__(self, key):
            try:
                return object.__getattribute__(self, 'obj_cache')[key]
            except KeyError:
                return object.__getattribute__(self, key)
    
    
    class AA(object):
        obj_cache = {'a': {}, 'b': 12345, 'c': []}
        def __getattribute__(self, key):
            if key in super(AA, self).__getattribute__('obj_cache'):
                return object.__getattribute__(self, 'obj_cache')[key]
            else:
                return object.__getattribute__(self, key)
    
    class B(object):
        a = {}
        b = 12345
        c = []
    
    a = A()
    aa = AA()
    b = B()
    
    class Tst(Timer):
    
        def getattribute_with_tryexcept(self):
            a.a, a.b, a.c
    
        def getattribute_with_ifelse(self):
            aa.a, aa.b, aa.c
    
        def without_getattribute(self):
            b.a, b.b, b.c
    
    
    
    Tst()


### Generates: ###


    getattribute_with_ifelse                : 3.13824  sec 
    getattribute_with_tryexcept             : 1.80899  sec 
    without_getattribute                    : 0.30323  sec 
    
    Each method run 1,000,000 times, sorted results listed bellow:
    
    without_getattribute                    : 0.30323  sec 
    getattribute_with_tryexcept             : 1.80899  sec 
    getattribute_with_ifelse                : 3.13824  sec

