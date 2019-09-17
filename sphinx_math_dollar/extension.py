from __future__ import print_function
import os
import sys

from .math_dollar import split_dollars

from docutils.nodes import GenericNodeVisitor, Text, math, FixedTextElement, literal
from docutils.transforms import Transform

NODE_BLACKLIST = node_blacklist = (FixedTextElement, literal, math)

DEBUG = bool(os.environ.get("MATH_DOLLAR_DEBUG", False))

class MathDollarReplacer(GenericNodeVisitor):
    def default_visit(self, node):
        return node

    def visit_Text(self, node):
        parent = node.parent
        while parent:
            if isinstance(parent, node_blacklist):
                if DEBUG and any(i == 'math' for i, _ in split_dollars(node.rawsource)):
                    print("sphinx-math-dollar: Skipping", node, "(node_blacklist = %s)" % (node_blacklist,), file=sys.stderr)
                return
            parent = parent.parent
        data = split_dollars(node.rawsource)
        nodes = []
        has_math = False
        for typ, text in data:
            if typ == "math":
                has_math = True
                nodes.append(math(text, Text(text)))
            elif typ == "text":
                nodes.append(Text(text))
            else:
                raise ValueError("Unrecognized type from split_dollars %r" % typ)
        if has_math:
            node.parent.replace(node, nodes)

class TransformMath(Transform):
    # See http://docutils.sourceforge.net/docs/ref/transforms.html. We want it
    # to apply before things that change rawsource, since we have to use that
    # to get the version of the text with backslashes. I'm not sure which all
    # transforms are relevant here, other than SmartQuotes, so this may need
    # to be adjusted.
    default_priority = 500
    def apply(self, **kwargs):
        self.document.walk(MathDollarReplacer(self.document))

def config_inited(app, config):
    global node_blacklist, DEBUG
    node_blacklist = config.math_dollar_node_blacklist
    DEBUG = config.math_dollar_debug

def setup(app):
    app.add_transform(TransformMath)
    app.add_config_value('math_dollar_node_blacklist', NODE_BLACKLIST, 'env')
    app.add_config_value('math_dollar_debug', DEBUG, '')

    app.connect('config-inited', config_inited)
