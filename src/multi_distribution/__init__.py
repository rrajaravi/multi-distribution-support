import os
import collections

Distro = collections.namedtuple('Distro', 'name releaseFile') 

# List to hold supported operating system distribution
supported_distros = [
    Distro('redhat', '/etc/redhat-release'),
    Distro('solaris', '/etc/release'),
    Distro('ubuntu', '/etc/lsb-release'),
    Distro('suse', '/etc/SuSE-release'),
]


def get_valid_class(aclass, param=None, value=None):
    """ 
    Check all the subclasses of a provided
    class to see if the provided parameter 
    and value exist in any of the subclass.
  
    Return the subclass if the parameter 
    and value matches, else return the 
    provided class itself.
    """
    
    param = param is None and 'distro' or param
    value = value is None and get_distro() or value
    _result = aclass
    subclasses = aclass.__subclasses__()

    for _aclass in subclasses:
        if getattr(_aclass, param, None) == value:
            _result = _aclass

    return _result()


def checkFile_and_return(adistro):
    """
    Check the provided distro to see
    if the release file of the distro
    exist in the system.

    if release file exist, return the
    distro, else return None
    """
    try:
        if os.path.isfile(adistro.releaseFile):
            return adistro
    except IOError:
         return None
        
    
def get_distro():
    """
    Using the list of supported distributions, check which
    one matches with the current system.

    Return the name of the matched distribution, else
    return False
    """

    valid_distro = filter(checkFile_and_return, supported_distros)
    return len(valid_distro) > 0 and valid_distro[0].name
