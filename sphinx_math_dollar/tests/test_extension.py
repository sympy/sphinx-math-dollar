import pytest


def test(app):
    app.build()


@pytest.mark.sphinx(buildername='html')
def test_sphinx_build(app, status, warning):
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
