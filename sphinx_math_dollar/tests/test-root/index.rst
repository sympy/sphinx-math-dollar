For this test, $math$ should render as math and ``$nomath$`` should not.
$$displaymath$$ should render as display math (TODO: Some of these don't
actually make sense for display math)

====================
 $math$ in a header
====================

============================
 $$displaymath$$ in a header
============================

``$nomath$`` in code
``$$nomath$$``

>>> print("$nomath$")
$nomath$
>>> print("$$nomath$$")
$$nomath$$

a definition list with $math$
    some $math$

a definition list with $$displaymath$$
    some $$displaymath$$

.. code::

   $nomath$
   $$nomath$$

.. raw:: html

   $nomath$
   $$nomath$$

..
   $nomath$ in a comment
   $$nomath$$


No double math :math:`$nomath$`, :math:`$$nomath$$`

.. math::
   $nomath$

.. math::
   $$nomath$$

Double dollar signs $$displaymath$$.

List items are manually disabled in the blacklist in conf.py

1. $nomath$

2. $$nomath$$

* $nomath$

* $$nomath$$
