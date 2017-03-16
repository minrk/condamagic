"""%conda magic for IPython

ensures the current conda env is active for things like installing, etc.

Use:

    %load_ext condamagic

    %conda install packages
"""

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

def conda(line):
    """Call conda with the current environment

    Adds a `-p{sys.prefix}` argument to ensure the current environment is
    the default, unless another env is specified.

    No different than !conda if the environment is fully activated.
    """
    prefix = sys.prefix
    args = shlex.split(line)
    cmd, *rest = line.split(None, 1)
    
    if cmd not in ENV_COMMANDS:
        # not one of our env-specific commands
        _ip.system('conda ' + line)
        return
    inserts = []
    # add `-p ${sys.prefix}` if no `--path` or `--name` arg present
    if not any(env_arg in args for env_arg in ['-p', '--prefix', '-n', '--name']):
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