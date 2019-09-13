import re

def split_dollars(text):
    r"""
    Replace dollar signs with backticks.

    More precisely, do a regular expression search.  Replace a plain
    dollar sign ($) by a backtick (`).  Replace an escaped dollar sign
    (\$) by a dollar sign ($).  Don't change a dollar sign preceded or
    followed by a backtick (`$ or $`), because of strings like
    "``$HOME``".  Don't make any changes on lines starting with
    spaces, because those are indented and hence part of a block of
    code or examples.

    This also doesn't replaces dollar signs enclosed in curly braces,
    to avoid nested math environments, such as ::

      $f(n) = 0 \text{ if $n$ is prime}$

    Thus the above line would get changed to

      :math:`f(n) = 0 \text{ if $n$ is prime}`
    """
    # This searches for "$blah$" inside a pair of curly braces --
    # don't change these, since they're probably coming from a nested
    # math environment.  So for each match, we replace it with a temporary
    # string, and later on we substitute the original back.
    _data = {}
    def repl(matchobj):
        nonlocal _data
        s = matchobj.group(0)
        t = "___XXX_REPL_%d___" % len(_data)
        _data[t] = s
        return t
    # Match $math$ inside of {...} and replace it with dummy text
    # TODO: This will false positive if the {} are not themselves in math
    text = re.sub(r"({[^{}$]*\$[^{}$]*\$[^{}]*})", repl, text)
    # matches $...$
    dollars = re.compile(r"(?<!\$)(?<!\\)\$([^\$ ][^\$]*?)\$")
    res = []
    start = 0
    end = len(text)
    def _add_fragment(t, typ):
        t = t.replace(r'\$', '$')
        # change the original {...} things in:
        for r in _data:
            t = t.replace(r, _data[r])
        if t:
            res.append((typ, t))

    for m in dollars.finditer(text):
        text_fragment = text[start:m.start()]
        math_fragment = m.group(1)
        start = m.end()
        _add_fragment(text_fragment, 'text')
        _add_fragment(math_fragment, 'math')
    _add_fragment(text[start:end], 'text')

    return res
