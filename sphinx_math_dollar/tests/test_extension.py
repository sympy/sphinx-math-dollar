import os

from sphinx_testing import with_app

@with_app(buildername='html', srcdir=os.path.join(os.path.dirname(__file__), 'test-build'),
          copy_srcdir_to_tmpdir=True)
def _test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir/'index.html').read_text()

    assert r"\(math\)" in html
    assert r"\[displaymath\]" in html
    assert "$nomath$" in html

    assert "$math$" not in html
    assert "$$displaymath$$" not in html

    assert r"\(nomath\)" not in html
    assert r"\(displaymath\)" not in html

    assert r"\[math\]" not in html
    assert r"\[nomath\]" not in html

    assert not status.read()
    assert not warning.read()

def test_sphinx_build():
    _test_sphinx_build()
