#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMStart'
]


class VMStart(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id):
        cs = self.get_client(url, apikey, secretkey)

        cs.startVirtualMachine(id=vm_id)
