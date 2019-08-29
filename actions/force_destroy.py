#!/usr/bin/env python

from st2common.runners.base_action import Action
from cs import CloudStack

__all__ = [
    'ForceStopVM'
]

class ForceStopVM(Action):

    def run(self, acs_url, apikey, secretkey, vm_id):
        cs = CloudStack(endpoint=acs_url,
                key=apikey,
                secret=secretkey)

        return True, cs.stopVirtualMachine(id = vm_id, forced = True)