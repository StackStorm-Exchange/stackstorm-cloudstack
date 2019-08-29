#!/usr/bin/env python

from st2common.runners.base_action import Action
from cs import CloudStack

__all__ = [
    'ForceStopVM'
]

class ForceStopVM(Action):

    def run(self, url, apikey, secretkey, vm_id):
        cs = CloudStack(endpoint=url,
                key=apikey,
                secret=secretkey,
                dangerous_no_tls_verify=True)

        return cs.stopVirtualMachine(id = vm_id, forced = True)