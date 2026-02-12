from ..math_dollar import split_dollars
import pytest

def test_split_dollars():
    assert split_dollars("Text") == [("text", "Text")]
    assert split_dollars(r"$\sin(x)$") == [("math", r"\sin(x)")]
    assert split_dollars(r"$\sin(x)") == [("text", r"$\sin(x)")]

    assert split_dollars(r"$\sin(x)$ and $\cos(x)$") == \
        [
            ("math", r"\sin(x)"),
            ("text", " and "),
            ("math", r"\cos(x)"),
        ]
    assert split_dollars(r"The functions $\sin(x)$ and $\cos(x)$.") == \
        [
            ("text", "The functions "),
            ("math", r"\sin(x)"),
            ("text", " and "),
            ("math", r"\cos(x)"),
            ("text", "."),
        ]

    assert split_dollars(r"$\sin(x)$ and $\cos(x)$") == \
        [
            ("math", r"\sin(x)"),
            ("text", " and "),
            ("math", r"\cos(x)"),
        ]

    assert split_dollars("Math that is split across lines $\\sin(x) +\n\\cos(x)$.") == \
        [
            ("text", "Math that is split across lines "),
            ("math", "\\sin(x) +\n\\cos(x)"),
            ("text", "."),
        ]

    assert split_dollars('$f(n) = 0 \text{ if $n$ is prime}$ $f(n) = 0 \text{ if $n$ is prime}$ \text{ if $n$ is prime}')

    assert split_dollars(r"$ ls") == [("text", "$ ls")]
    assert split_dollars("$ cd ..\n$ ls") == [("text", "$ cd ..\n$ ls")]

    assert split_dollars(r"\$13 + \$14") == [("text", "$13 + $14")]
    assert split_dollars(r"$\$13 + \$14$") == [("math", "$13 + $14")]
    assert split_dollars(r"$\$13$.") == [("math", "$13"), ("text", ".")]
    assert split_dollars(r"    $\sin(x)$") == [("text", "    "), ("math", r"\sin(x)")]

    assert split_dollars(r"$$\sin(x)$$") == [("display math", r"\sin(x)")]
    assert split_dollars(r"$$\sin(x)$") == [("text", r"$$\sin(x)$")]
    assert split_dollars(r"$$\sin(x)") == [("text", r"$$\sin(x)")]
    assert split_dollars(r"\$$\sin(x)$$") == [("text", r"$$\sin(x)$$")]
    assert split_dollars(r"\$\$\sin(x)\$\$") == [("text", r"$$\sin(x)$$")]
    assert split_dollars(r"$\sin(x)$ and $$\cos(x)$$") == \
        [
            ("math", r"\sin(x)"),
            ("text", " and "),
            ("display math", r"\cos(x)"),
        ]
def test_unmatched_dollar_raises():
    with pytest.raises(ValueError):
        split_dollars("This costs $12", unmatched="error")  # unmatched

def test_escaped_dollar_ok():
    assert split_dollars(r"This costs \$12") == [("text", "This costs $12")]


def test_unmatched_dollar_error_mode():
    with pytest.raises(ValueError):
        split_dollars(r"$\sin(x)", unmatched="error")

def test_escaped_dollar_still_ok():
    assert split_dollars(r"This costs \$12", unmatched="error") == [("text", "This costs $12")]