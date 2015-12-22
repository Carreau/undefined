
"""
a simple package
"""


__version__ = '0.0.1'

import sys
import types

class Undefined(types.ModuleType):


    @property
    def Undefined(self):
        return self

    def __call__(self, value):
        return value is self

    def __repr__(self):
        return self.__class__.__name__

    __str__ = __repr__


Undefined.__name__ = 'Undefined'
Undefined = Undefined('undefined')

if sys.modules[__name__] is Undefined:
    print('doing nothing')
    pass
else:
   sys.modules[__name__] = Undefined
