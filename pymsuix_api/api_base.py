
class Pool(object):
    def __init__(self):
        self.connection = {'name':'',
                           'url':'',
                           'username':'',
                           'password':''}
        self.status = {
            'id' : 0,
            'status' : '',
            'getworks': 0,
            'accepts' : 0,
            'rejects' : 0,
            'discards': 0,
            'stales': 0,
            'getfails': 0,
            'remfails': 0
        }

class GPU(object):
    def __init__(self):
        self.id = 0
        self.statistics = {
            'accepted': 0,
            'rejected': 0,
            'discarded': 0,
            'hashrateavg': 0,
            'intensity': 0,
            'last-share-time': 0,
            'last-share-pool': 0,
            'last-valid-work': 0
        }
        self.status = {'state': '',
                       'core-clock': 0,
                       'mem-clock': 0,
                       'fanrpm': 0,
                       'fanspeed': 0,
                       'voltage' : 0,
                       'temperature': 0}
        
class CPU(object):
    def __init__(self):
        self.statistics = {
            'accepted': 0,
            'rejected': 0,
            'discarded': 0,
            'hashrateavg': 0,
            'intensity': 0,
            'last-share-time': 0,
            'last-share-pool': 0,
            'last-valid-work': 0
        }
        self.status = {'state': '',
                       'core-clock': 0,
                       'mem-clock': 0,
                       'fanrpm': 0,
                       'fanspeed': 0,
                       'voltage' : 0,
                       'temperature': 0}
        
class FPGA(object):
    def __init__(self):
        self.statistics = {
            'accepted': 0,
            'rejected': 0,
            'discarded': 0,
            'hashrateavg': 0,
            'intensity': 0,
            'last-share-time': 0,
            'last-share-pool': 0,
            'last-valid-work': 0
        }
        self.status = {'state': '',
                       'core-clock': 0,
                       'mem-clock': 0,
                       'fanrpm': 0,
                       'fanspeed': 0,
                       'voltage' : 0,
                       'temperature': 0}

class miner(object):
    def __init__(self):
        self.connection = {
            'name': '',
            'ipaddress':'',
            'port':'',
            'version':''}
        self.configuration = {
            'gpucount': 0,
            'fpgacount': 0,
            'cpucount' : 0,
            'poolcount': 0,
            'adl' : '',
            'adl-inuse': '',
            'pool-strategy': '',
            'log-interval': 0,
            'devicecode': '',
            'operating-system': '',
            'failover-only': False,
            'scantime': 0,
            'queue': 0,
            'expiry': 0}
        self.status = {
            'elapsed': 0,
            'found-blocks': 0,
            'get-works': 0,
            
        }
        self.pools = []
        self.GPUs = []
        self.FPGAs = []
        self.CPUs = []