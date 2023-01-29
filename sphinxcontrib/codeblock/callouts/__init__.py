"""
sphinxcontrib.codeblock.callouts
"""

import re
from pathlib import Path
from typing import List

from docutils import nodes
from docutils.nodes import Node
from pygments.formatters import HtmlFormatter
from pygments.token import Comment
from sphinx.highlighting import PygmentsBridge
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset_file


logger = logging.getLogger(__name__)


class CodeBlockCalloutsDirective(SphinxDirective):
    has_content = True

    def run(self) -> List[Node]:
        node = nodes.container()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)
        if len(node.children) != 1 or not isinstance(node.children[0], nodes.enumerated_list):
            logger.warning(__('The content of code-block-callouts should be an enumerated list'),
                           location=(self.env.docname, self.lineno))
            return []

        node.children[0]['classes'].append('code-block-callouts')

        return node.children


class CodeBlockCalloutsHtmlFormatter(HtmlFormatter):
    def __init__(self, **options):
        super().__init__(**options)

        self.span_element_openers[Comment.Callout] = '<span class="code-block-callouts"><span>'
        self.span_element_openers[Comment.Callout.Close] = ' '

    def format(self, tokensource, outfile):
        return super().format(self.new_tokens(tokensource), outfile)

    def new_tokens(self, tokensource):
        for token in tokensource:
            if token[0] == Comment.Single:
                matched = re.match(r'# (\d+)', token[1])
                if matched:
                    # replace a callout comment token by Comment.Callout token
                    yield (Comment.Callout, matched[1])
                    yield (Comment.Callout.Close, ' ')
                else:
                    yield (Comment.Callout, token[1])
            else:
                yield token


def copy_static_file(app, exc):
   if app.builder.format == 'html' and not exc:
       staticdir = Path(app.builder.outdir) / '_static'
       css = Path(__file__).parent / 'static/codeblock-callouts.css'
       copy_asset_file(str(css), str(staticdir))


def setup(app):
    app.add_css_file('codeblock-callouts.css')
    app.add_directive('code-block-callouts', CodeBlockCalloutsDirective)
    app.connect('build-finished', copy_static_file)
    PygmentsBridge.html_formatter = CodeBlockCalloutsHtmlFormatter

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
