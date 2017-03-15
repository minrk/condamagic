# conda magic

`%conda` magic for IPython (and @jakevdp).

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Is there any way to run
``conda install`` within a Jupyter notebook, to install packages to the conda env used by the
*current kernel*?</p>&mdash; Jake VanderPlas (@jakevdp) <a
href="https://twitter.com/jakevdp/status/841777088088559616">March 14, 2017</a></blockquote>

All it does is ensure that the current conda env is active when you run `%conda`,
so that `%conda install packages` should always go in the kernel envs.

Install:

    pip install condamagic
    
Load:

    %load_ext condamagic

Use:

    %conda install packages

