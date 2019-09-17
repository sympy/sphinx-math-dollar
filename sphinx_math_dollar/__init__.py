from .math_dollar import split_dollars
from .extension import setup, NODE_BLACKLIST

__all__ = ['split_dollars', 'setup', 'NODE_BLACKLIST']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
