import os

supported_distros = [dict(name='redhat', rfile='/etc/redhat-release'),
                         dict(name='solaris', rfile='/etc/release'),
                         dict(name='ubuntu', rfile='/etc/lsb-release'),
                         dict(name='suse', rfile='/etc/SuSE-release'),
                    ]


def get_valid_class(aclass, param='', value=''):
    param = param == '' and 'distro' or param
    value = value == '' and get_distro() or value
    _result = aclass
    subclasses = aclass.__subclasses__()

    for _aclass in subclasses:
        if getattr(_aclass, param, None) == value:
            _result = _aclass

    return _result()


def checkFile_and_return(adistro):
    try:
        if os.path.isfile(adistro['rfile']):
            return adistro
    except IOError:
         return None
        
    
def get_distro():
    valid_distro = filter(checkFile_and_return, supported_distros)
    return len(valid_distro) > 0 and valid_distro[0]['name']
