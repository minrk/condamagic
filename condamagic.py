"""%conda magic for IPython

ensures the current conda env is active for things like installing, etc.

Use:

    %load_ext condamagic

    %conda install packages
"""

import os
import pipes
import shlex
import sys

# conda commands that should run in the env
ENV_COMMANDS = {
    'install',
    'list',
    'remove',
    'uninstall',
    'update',
    'upgrade',
}

YES_COMMANDS = ENV_COMMANDS.difference({'list'})

ENV_FLAGS = {'-p', '--prefix', '-n', '--name'}

def _is_conda_env(prefix):
    """Is the given prefix a conda env?"""
    return os.path.exists(os.path.join(prefix, 'conda-meta'))

def conda(line):
    """Call conda with the current environment

    Adds a `-p{sys.prefix}` argument to ensure the current environment is
    the default, unless another env is specified.

    No different than !conda if the environment is fully activated.
    """
    prefix = sys.prefix
    args = shlex.split(line)
    split_line = line.split(None, 1)
    cmd = split_line[0]
    rest = split_line[1:]

    if cmd not in ENV_COMMANDS:
        # not one of our env-specific commands
        _ip.system('conda ' + line)
        return
    inserts = []
    # add `-p ${sys.prefix}` if no `--path` or `--name` arg present
    # AND current sys.prefix is a conda env
    if _is_conda_env(prefix) and not set(args).intersection(ENV_FLAGS):
        inserts.append('-p %s' % pipes.quote(prefix))
    # add `-y` if in a kernel, where subprocesses can't ask for confirmation
    if cmd in YES_COMMANDS and getattr(_ip, 'kernel', None) is not None:
        inserts.append('-y')
    line = ' '.join(['conda', cmd] + inserts + rest)
    # print(line)
    _ip.system(line)

def load_ipython_extension(ip):
    global _ip
    _ip = ip
    ip.register_magic_function(conda)