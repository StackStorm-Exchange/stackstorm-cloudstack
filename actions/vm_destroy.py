#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMDestroy'
]


class VMDestroy(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id, expunge):
        cs = self.get_client(url, apikey, secretkey)

        return cs.destroyVirtualMachine(id=vm_id, expunge=expunge)
