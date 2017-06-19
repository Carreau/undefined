"""
a simple package
"""


__version__ = '0.0.6'

import sys
import types

class Undefined(types.ModuleType):
    """
    Simply a global object that act as undefined.
    """

    __version__ = __version__


    @property
    def Undefined(self):
        return self

    def __call__(self, value):
        return value is self

    def __eq__(self, other):
        raise NotImplementedError('Cannot compare undefined')

    def __repr__(self):
        return self.__class__.__name__

    def __bool__(self):
        raise NotImplementedError('Undefined is not defined, neither True, nor False.')

    def __str__(self):
        raise NotImplementedError("Cannot represent undefined !")


Undefined.__name__ = 'Undefined'
Undefined = Undefined('undefined', """
    Simply a global object that act as undefined.
    """
)

Undefined.__version__ = __version__

if sys.modules[__name__] is Undefined:
    print('doing nothing')
    pass
else:
   sys.modules[__name__] = Undefined
