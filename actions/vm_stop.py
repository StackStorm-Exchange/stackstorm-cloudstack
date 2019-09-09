#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMStop'
]


class VMStop(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id, forced):
        cs = self.get_client(url, apikey, secretkey)

        cs.stopVirtualMachine(id=vm_id, forced=forced)
