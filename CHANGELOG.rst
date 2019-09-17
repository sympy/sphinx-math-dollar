===========
 Changelog
===========

1.1 (2019-09-17)
================

- Allow ``$math$`` in more places.
- Add the configuration variable ``math_dollar_node_blacklist`` to configure
  which docutils nodes should not have ``$math$`` replaced.
- Add tests for the extension part of the code.
- Add ``math_dollar_debug`` configuration options and ``MATH_DOLLAR_DEBUG``
  environment variable to print out debug info on when ``$math$`` is skipped.

1.0 (2019-09-16)
================

Initial release.
