#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMReboot'
]


class VMReboot(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id):
        cs = self.get_client(url, apikey, secretkey)

        cs.rebootVirtualMachine(id=vm_id)
