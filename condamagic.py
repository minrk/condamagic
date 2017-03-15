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
    # add `-p ${sys.prefix}` if no `--path` or `--name` arg present
    prefix_arg = ''
    if not any(env_arg in args for env_arg in ['-p', '--prefix', '-n', '--name']):
        prefix_arg = '-p %s' % pipes.quote(prefix)
    print(' '.join(['conda', cmd, prefix_arg] + rest))
    _ip.system(' '.join(['conda', cmd, prefix_arg] + rest))

def load_ipython_extension(ip):
    global _ip
    _ip = ip
    ip.register_magic_function(conda)