from lulu.base import *
from lulu.connected_region import *
import lulu.connected_region_handler

import os.path as _path
_basedir = _path.abspath(_path.join(__file__, '..'))

try:
    import functools as _functools
    import nose as _nose
    test = _functools.partial(_nose.run, 'lulu',
                argv=['', '-v', '--exe', '-w', _basedir])
except:
    raise ImportError("Could not load nose.  Please install using"
                      " `easy_install nose`.")


def _register_pickling():
    crh = connected_region_handler
    # Register picking functions for connected region
    try:
        import copy_reg as copyreg
    except:
        import copyreg

    def reduce_connected_region(obj):
        return ConnectedRegion, (crh.get_shape(obj), crh.get_value(obj),
                                 crh.get_start_row(obj), crh.get_rowptr(obj),
                                 crh.get_colptr(obj))

    copyreg.pickle(ConnectedRegion, reduce_connected_region)

_register_pickling()
