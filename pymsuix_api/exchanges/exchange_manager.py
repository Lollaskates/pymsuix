from exchange_vircurex import vircurex as Vircurex

class ExchangeManager(object):
    def __init__(self):
        #populate miners from stored clients
        self._exchanges = [Vircurex()]
        pass