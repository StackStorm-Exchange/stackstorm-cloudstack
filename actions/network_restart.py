#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'NetworkRestart'
]


class NetworkRestart(CloudStackAPI):
    def run(self, url, apikey, secretkey, network_id, cleanup, make_redundant):
        cs = self.get_client(url, apikey, secretkey)

        return cs.restartNetwork(id=network_id, cleanup=cleanup, makeredundant=make_redundant)
