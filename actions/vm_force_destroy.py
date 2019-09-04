#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMForceDestroy'
]


class VMForceDestroy(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id):
        cs = self.get_client(url, apikey, secretkey)

        if cs.stopVirtualMachine(id=vm_id, forced=True):
            return cs.destroyVirtualMachine(id=vm_id)

        return False
