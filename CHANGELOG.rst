===========
 Changelog
===========

1.2 (2020-09-17)
================

- Add support for double dollar signs for display math.

1.1.1 (2019-09-30)
==================

- Fix a bug where the extension would force a full rebuild every time. Note
  that the ``math_dollar_node_blacklist`` config value now no longer
  automatically triggers a rebuild when it is changed, as it is impossible to
  do so without rebuilding every time.

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
