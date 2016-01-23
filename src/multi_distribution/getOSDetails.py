from multi_distribution import get_valid_class


class OS(object):
    """
    A generic class for unix/linux operating system
    """

    vendorName = 'Generic'
    vendorURL = 'not found'

    def readFile(self, fileName):
        with open(fileName, 'r') as f:
            return f.read()

    def getOsInfo(self):
        raise NotImplementedError('getOSInfo')

    def getVendor(self):
        return self.vendorName
    
    def getVendorURL(self):
        return self.vendorURL

class Redhat(OS):
    """
    Contains Redhat linux operating system specifics
    """

    distro = 'redhat'
    osReleaseFile = '/etc/redhat-release'
    vendorName = 'REDHAT'
    vendorURL = 'www.redhat.com'

    def getOsInfo(self):
        return self.readFile(self.osReleaseFile)


class Solaris(OS):
    """
    Contains Solaris operating system specifics
    """

    distro = 'solaris'
    osReleaseFile = '/etc/release'
    vendorName = 'ORACLE'
    vendorURL = 'www.oracle.com'

    def getOsInfo(self):
        return self.readFile(self.osReleaseFile)


class Ubuntu(OS):
    """
    Contains Ubuntu operating system specifics
    """

    distro = 'ubuntu'
    osReleaseFile = '/etc/lsb-release'
    vendorName = 'UBUNTU'
    vendorURL = 'www.ubuntu.com'

    def getOsInfo(self):
        return self.readFile(self.osReleaseFile)

        
class SUSE(OS):
    """
    Contains SUSE operating system specifics
    """

    distro = 'suse'
    osReleaseFile = '/etc/SuSE-release'
    vendorName = 'SUSE'
    vendorURL = 'www.suse.com'

    def getOsInfo(self):
        return self.readFile(self.osReleaseFile)


# get a valid class with respect to the distribution using generic class
sampleOS = get_valid_class(OS)

# print OS release info
print("OS Details:\n" + sampleOS.getOsInfo())

# print OS vendor info
print("Vendor Info:\n" + sampleOS.getVendor())

# print OS vendor info
print("Vendor URL:\n" + sampleOS.getVendorURL())
