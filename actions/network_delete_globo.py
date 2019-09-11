#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'NetworkDeleteGlobo'
]


class NetworkDeleteGlobo(CloudStackAPI):
    def run(self, url, apikey, secretkey, network_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.deleteNetworkInGloboNetwork(id=network_id)
