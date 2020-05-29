====================
 sphinx-math-dollar
====================

sphinx-math-dollar is a Sphinx extension to let you write LaTeX math using $$.

To enable install it

.. code::

   pip install sphinx-math-dollar

or

.. code::

   conda install -c conda-forge sphinx-math-dollar

Then in your ``conf.py``, add ``'sphinx_math_dollar'`` to your extensions list:

.. code:: python

   extensions = ['sphinx_math_dollar', 'sphinx.ext.mathjax']

   mathjax_config = {
       'tex2jax': {
           'inlineMath': [ ["\\(","\\)"] ],
           'displayMath': [["\\[","\\]"] ],
       },
   }


The ``mathjax_config`` is needed to prevent MathJax from parsing dollar signs
which are ignored by the extension because they should not be parsed as math.

You will now be able to use dollar signs for math, like ``$\int\sin(x)\,dx$``,
which will produce $\int\sin(x)\,dx$. You can also use double dollar signs for
display math, like ``$$\int\sin(x)\,dx$$``, which produces $$\int\sin(x)\,dx$$
(if you are reading this on GitHub, look at the version built by Sphinx `here
<https://www.sympy.org/sphinx-math-dollar/>`_). The usual Sphinx ``:math:``
and ``.. math::`` directives will also continue to work.

The extension will also work with docstrings when combined with the
`sphinx.ext.autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
extension.

Configuration
=============

sphinx-math-dollar uses a blacklist to determine which `docutils nodes
<http://docutils.sourceforge.net/docs/ref/doctree.html>`_ should not be
parsed. The default blacklist is

.. code::

   (FixedTextElement, literal, math)

``FixedTextElement`` covers the `Simple Body Elements
<http://docutils.sourceforge.net/docs/ref/doctree.html>`_ nodes.

Any docutils node that is contained in a blacklisted node or a subclass of a
blacklisted node will not have ``$math$`` parsed as LaTeX.

You can modify this by setting ``math_dollar_node_blacklist`` in ``conf.py``.
For example, to also prevent ``$math$`` from rendering in `headers nodes
<http://docutils.sourceforge.net/docs/ref/doctree.html#header>`_, add

.. code:: python

   from sphinx_math_dollar import NODE_BLACKLIST
   from docutils.nodes import header

   math_dollar_node_blacklist = NODE_BLACKLIST + (header,)

Note that configuring this variable replaces the default, so it is recommended
to always include the above default values (``NODE_BLACKLIST``) in addition to
additional nodes.

To debug which nodes are skipped, set the environment variable
``MATH_DOLLAR_DEBUG=1`` or set ``math_dollar_debug = True`` in ``conf.py``.

If you feel a node should always be part of the default blacklist, please make
a `pull request <https://github.com/sympy/sphinx-math-dollar>`_.

License
=======

MIT.
