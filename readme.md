# Undefined

Ever needed a global object that act as `None` but not quite ?

Like for example key-word argument for function, where `None` make sens, so you need a default value.

One solution is to create as singleton object:

```
mysingleton = object()
```

Though it becomes difficult to track the singleton across libraries,
and teach users where to import this from. 

It's also relatively annoying use this singleton across library. 


Introducing `undefined`:

```
>>> import undefined
>>> from undefined import Undefined
>>> undefined is Undefined
True
```


# behavior

It work (for now) mostly like a singleton object

Though it's neither truthy not falsy

```
>>> if undefined: print(True)
raise NotImplementedError
```

# Casing ?

Because it is a module you can use it lowercase:

```
import undefined
```

Because it looks more like a keyword (`None`, `True`, `False`), you can use it upper case:

```
import undefined as Undefined
```

or

```
from undefined import Undefined
```

I tend to be torn between lowercase, for simplicity, and Uppercase.


# Why not `None`, difference with `None`

`undefined` is likely slower, and as it is a regular Python object there are a few  on purpose (or not difference).

### Unlike `None`, you can assign to it

```
>>> None = 3 
SyntaxError: can't assign to keyword
```

```
>>> undefined = 3
>>> undefned
3
```

### Unlike `None`, `undefined` is mutable

```
>>> undefined.value = 42
>>> undefined.value
42
```

(might be able to fix that with `__get_attr__`

### Unlike `None`, `undefined` is neither true not false.

If you test for boolean value of `undefind` if will raise. 
That is to say: the following will fail:

```
value = undefined
if value:
   pass # will raise before reaching here.
```

You have to check for identity:

```
value = undefined
other = 1
if value is undefined:
    pass # will execute
```

for info, undefined is not `True`,`False`, not undefined with respect to identity

```
>>> undefined is True
False

>>> undefined is False
False

>>>: undefined is None
False
```

### String form

`str(undefined)` raises. `repr(undefined)` is the unicode string `'Undefined'`
