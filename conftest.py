import pytest
from sphinx.testing.path import path


try:
    import pytest_doctestplus.plugin
    pytest_doctestplus
except ImportError:
    raise ImportError("Install pytest-doctestplus to run the tests")


pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'sphinx_math_dollar' / 'tests'
