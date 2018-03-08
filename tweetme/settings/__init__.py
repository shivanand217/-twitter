# __init__ needs to import all the settings

from .base import *

from .production import *

try:
    from .local import *
except:
    pass