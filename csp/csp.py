#!/usr/bin/env python

"""
If you want to use the python-csp library then this is the file to
import. It attempts to match the best possible implementation of CSP
for your platform.

If you wish to choose to use the multiprocess (multicore) or threaded
version of the libraries explicitly then set an environment variable
in your opertaing system called "CSP". This should be either set to
"PROCESSES" or "THREADS" depending on what you want to use.


Copyright (C) Sarah Mount, 2010.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have rceeived a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
"""

from __future__ import absolute_import 

import os
import sys


__author__ = 'Sarah Mount <s.mount@wlv.ac.uk>'
__date__ = 'July 2010'


# XXX: Why don't we just try to import os_process? If we have
# the separate processing module, the import should work even
# when we're on a Python version before 2.6. By the way, the
# whole decision logic can probably be simplified.

# If multiprocessing is not available then import threads.
major, minor = sys.version_info[:2]
if major < 2 or (major == 2 and minor < 6):
    try:
        from .os_process import *
    except:
        from .os_thread import *

# If multiprocessing is likely to be available then let the user
# choose which version of the implementation they wish to use.
elif 'CSP' in os.environ:
    if os.environ['CSP'].upper() == 'PROCESSES':
        from .os_process import *
    elif os.environ['CSP'].upper() == 'THREADS':
        from .os_thread import *
    else:
        from .os_process import *

# If no useful information is available then try to import the
# multiprocessing version of the code else catch the resulting
# exception and use the threaded version.
else: 
    try:
        from .os_process import *
    except:
        from .os_thread import *

del os
del sys

### Names exported by this module
__all__ = ['set_debug', 'CSPProcess', 'CSPServer', 'Alt',
           'Par', 'Seq', 'Guard', 'Channel', 'FileChannel',
           'process', 'forever', 'Skip', '_CSPTYPES']

