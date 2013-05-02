from miner_cgminer import cgminer as CGMiner

class MinerManager(object):
    def __init__(self):
        #populate miners from stored clients
        self._miners = [CGMiner()]
        pass