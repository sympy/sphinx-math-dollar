from .math_dollar import split_dollars

from docutils.nodes import NodeVisitor

class MathDollarReplacer(NodeVisitor):
    def visit_Text(self, node):
        _data = split_dollars(node.astext())

def process_doctree(app, doctree):
    pass

def setup(app):
    app.connect("doctree-read", process_doctree)
