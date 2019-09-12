#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMGetInfo'
]


class VMGetInfo(CloudStackAPI):
    def run(self, url, apikey, secretkey, vm_id, project_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.listVirtualMachines(id=vm_id, projectid=project_id)
