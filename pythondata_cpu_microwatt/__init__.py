import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post479"
version_tuple = (0, 0, 479)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post479")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post431"
data_version_tuple = (0, 0, 431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post431")
except ImportError:
    pass
data_git_hash = "d3291dbdf01960e900e1d863f02f35a45a611454"
data_git_describe = "v0.0-431-gd3291db"
data_git_msg = """\
commit d3291dbdf01960e900e1d863f02f35a45a611454
Merge: 8bee4ae 9d7df2d
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Fri Apr 3 10:36:36 2020 +1100

    Merge pull request #155 from mikey/exceptions
    
    Add decrementer, illegal and system call exceptions

"""

# Tool version info
tool_version_str = "0.0.post48"
tool_version_tuple = (0, 0, 48)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post48")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
