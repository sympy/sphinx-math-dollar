For this test, $math$ should render as math and ``$nomath$`` should not.

====================
 $math$ in a header
====================

``$nomath$`` in code

>>> print("$nomath$")
$nomath$

a definition list with $math$
    some $math$

.. code::

   $nomath$

.. raw:: html

   $nomath$

..
   $nomath$ in a comment


No double math :math:`$nomath$`

No double dollar signs (will change in the future) $$nomath$$.

List items are manually disabled in the blacklist in conf.py

1. $nomath$

* $nomath$
