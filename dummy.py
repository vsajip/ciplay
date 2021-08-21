# A dummy package for testing out CI configurations

import logging
import os
import re
import subprocess

logger = logging.getLogger(__name__)

VERSION_RE = re.compile(r'gpg \(GnuPG(?:/MacGPG2)?\) (\d+(\.\d+)*)'.encode('ascii'), re.I)

def hello():
    logger.debug('Well, hello there.')
    return 'Hello, world!'

def gpg_version():
    gpg = os.environ.get('GPGBINARY', 'gpg')
    cmd = [gpg, '--version']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = p.communicate()
    m = VERSION_RE.match(stdout)
    if not m:  # pragma: no cover
        result = None
    else:
        result = tuple([int(s) for s in m.groups()[0].split(b'.')])
    return result
