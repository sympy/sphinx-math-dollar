===========
 Changelog
===========

1.3 (2026-02-05)
=================

- Fix crash when encountering unknown node types. The extension now skips
  unknown nodes with a warning instead of crashing (@MarelliF).
- Return metadata in ``setup()`` to improve compatibility with parallel
  processing (@dabacon).
- Add ``pyproject.toml`` for modern Python packaging.
- Migrate CI from Travis CI to GitHub Actions.
- Add Sphinx 9 compatibility by replacing ``sphinx.testing.path`` with
  ``pathlib``.
- Update supported Python versions to 3.11, 3.12, 3.13, 3.14, and PyPy 3.11.
- Add support for ``\(...\)`` and ``\[...\]`` math delimiters.

1.2.1 (2022-04-25)
==================

- Drop Python 2.7 support (@oscargus).
- Make the extension more future-proof against future docutils versions
  (thanks @gmilde).
- Mark the extension as parallel read safe (@namurphy).
- Update versioneer (@oscargus).
- Replace sphinx-testing with sphinx.testing (@oscargus).

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
