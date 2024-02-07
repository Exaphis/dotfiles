"Adapted from https://gist.github.com/nova77/5403446"

import sys
from contextlib import redirect_stdout
import io

if sys.platform == 'darwin':
    from AppKit import NSPasteboard, NSArray
elif sys.platform.startswith('linux'):
    from subprocess import Popen, PIPE
else:
    raise ImportError("Clip magic only works on osx or linux!")

from IPython.core.magic import register_line_cell_magic, register_line_magic


def _copy_to_clipboard(arg):
    arg = str(globals().get(arg) or arg)

    if sys.platform == 'darwin':
        pb = NSPasteboard.generalPasteboard()
        pb.clearContents()
        a = NSArray.arrayWithObject_(arg)
        pb.writeObjects_(a)
    elif sys.platform.startswith('linux'):
        p = Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE)
        p.communicate(input=arg.encode('utf-8'))

    print('Copied to clipboard!')


def _run_cell(cell):
    return get_ipython().run_cell(cell).result


@register_line_cell_magic
def clip(line, cell=None):
    contents = cell or line
    _copy_to_clipboard(_run_cell(contents))


@register_line_cell_magic
def clipout(line, cell=None):
    contents = cell or line

    # TODO: tee?
    f = io.StringIO()
    with redirect_stdout(f):
        _run_cell(contents)

    o = f.getvalue()
    print(o)
    _copy_to_clipboard(o)


@register_line_magic
def histout(line):
    get_ipython().run_line_magic('hist', '-p -o ' + line)


# We delete it to avoid name conflicts for automagic to work
del clip, clipout, histout

