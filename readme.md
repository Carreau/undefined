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

It work (for now) mostly like a singleton object, meaning it's truth-y

```
>>> if undefined: print(True)
True
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

