====================
 sphinx-math-dollar
====================

sphinx-math-dollar is a Sphinx extension to let you write LaTeX math using $$.

To enable install it

.. code::

   pip install sphinx-math-dollar

or

.. code::

   conda install sphinx-math-dollar

Then in your ``conf.py``, add ``'sphinx_math_dollar'`` to your extensions list:

.. code:: python

   extensions = ['sphinx_math_dollar', 'sphinx.ext.mathjax']

You will now be able to use dollar signs for math, like ``$\int\sin(x)\,dx$``,
which will produce $\int\sin(x)\,dx$ (if you are reading this on GitHub, look
at the version built by Sphinx `here
<https://www.sympy.org/sphinx-math-dollar/>`_). The usual Sphinx ``:math:``
directive will also continue to work.

The extension will also work with docstrings when combined with the
`sphinx.ext.autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
extension.

License
=======

MIT.
