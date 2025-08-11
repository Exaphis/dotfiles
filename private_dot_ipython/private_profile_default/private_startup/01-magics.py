"Adapted from https://gist.github.com/nova77/5403446"
import sys
from subprocess import Popen, PIPE
from contextlib import redirect_stdout
import io

from IPython.core.magic import register_line_cell_magic, register_line_magic

def _get_implementation():
    try:
        _get_implementation.impls
    except AttributeError:
        _get_implementation.impls = {}

        if sys.platform.startswith('linux'):
            def _clip(arg):
                p = Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE)
                p.communicate(arg.encode('utf-8'))
            _get_implementation.impls['linux'] = _clip

        elif sys.platform == 'darwin':
            def _clip(arg):
                p = Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE)
                p.communicate(arg.encode('utf-8'))
            _get_implementation.impls[sys.platform] = _clip

        # add further platforms below here:
        else:
            raise ImportError("Clip magic doesn't work on your platform: '{}'".format(sys.platform))


    return _get_implementation.impls['linux'] \
            if sys.platform.startswith('linux') \
        else _get_implementation.impls[sys.platform]


def _copy_to_clipboard(arg):
    try:
        arg = str(globals()[arg])
    except Exception:
        arg = str(arg)

    _get_implementation()(arg)
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

