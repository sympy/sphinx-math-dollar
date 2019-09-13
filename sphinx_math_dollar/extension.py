from .math_dollar import split_dollars

from docutils.nodes import GenericNodeVisitor, Text, math, paragraph

class MathDollarReplacer(GenericNodeVisitor):
    def default_visit(self, node):
        return node

    def visit_Text(self, node):
        if not isinstance(node.parent, paragraph):
            return
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

def process_doctree(app, doctree):
    doctree.walk(MathDollarReplacer(doctree))

def setup(app):
    app.connect("doctree-read", process_doctree)
