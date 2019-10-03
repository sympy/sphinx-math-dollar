from ..math_dollar import split_dollars

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
