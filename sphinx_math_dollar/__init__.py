from .math_dollar import split_dollars
from .extension import setup

__all__ = ['split_dollars', 'setup']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
