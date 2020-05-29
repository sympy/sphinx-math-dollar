import re

def split_dollars(text):
    r"""
    Split text into text and math segments.

    Returns a list of tuples ``(type, text)``, where ``type`` is either
    ``"text"`` or ``"math"`` and ``text`` is the text.

    Example:

    >>> split_dollars(r"The functions $\sin(x)$ and $\cos(x)$.")
    [('text', 'The functions '), ('math', '\\sin(x)'), ('text', ' and '),
    ('math', '\\cos(x)'), ('text', '.')]

    More precisely, do a regular expression search.  To match as math, the
    first character after the first $ should not be a space. This is to avoid
    false positives with things like

    $ cd ~
    $ ls

    Escaped dollars (\$) are also not matched as math delimiters, however all
    escaped dollars are replaced with normal dollars in the final output.

    Math is allowed to be split across multiple lines, as its assumed the
    dollars will appear in places like docstrings where line wrapping is
    desired.

    This also doesn't replaces dollar signs enclosed in curly braces,
    to avoid nested math environments, such as ::

      $f(n) = 0 \text{ if $n$ is prime}$

    Thus the above line would get matched fully as math.

    """
    # This searches for "$blah$" inside a pair of curly braces --
    # don't change these, since they're probably coming from a nested
    # math environment.  So for each match, we replace it with a temporary
    # string, and later on we substitute the original back.
    _data = {}
    def repl(matchobj):
        s = matchobj.group(0)
        t = "___XXX_REPL_%d___" % len(_data)
        _data[t] = s
        return t
    # Match $math$ inside of {...} and replace it with dummy text
    # TODO: This will false positive if the {} are not themselves in math
    text = re.sub(r"({[^{}$]*\$[^{}$]*\$[^{}]*})", repl, text)
    # matches $...$
    dollars = re.compile(r"(?<!\$)(?<!\\)\$(\$)?([^\$ ](?:(?<=\\)\$|[^\$])*?)(?<!\\)\$(?(1)\$|)")
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
        math_fragment = m.group(2)
        double_dollar = m.group(1)
        start = m.end()
        _add_fragment(text_fragment, 'text')
        if double_dollar:
            _add_fragment(math_fragment, 'display math')
        else:
            _add_fragment(math_fragment, 'math')
    _add_fragment(text[start:end], 'text')

    return res
