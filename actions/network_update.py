#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'NetworkUpdate'
]


class NetworkUpdate(CloudStackAPI):
    def run(self, url, apikey, secretkey, network_id, name, display_text):
        cs = self.get_client(url, apikey, secretkey)

        return cs.updateNetwork(id=network_id, name=name, displaytext=display_text)
