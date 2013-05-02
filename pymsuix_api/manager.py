from mining.miner_manager import MinerManager
from exchanges.exchange_manager import ExchangeManager

class MsuixManager(object):
    def __init__(self):
        self.Miners = MinerManager()
        self.Exchanges = ExchangeManager()