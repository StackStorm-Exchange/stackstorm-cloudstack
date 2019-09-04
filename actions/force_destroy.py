#!/usr/bin/env python

from st2common.runners.base_action import Action
from cs import CloudStack

__all__ = [
    'ForceStopVM'
]


class ForceStopVM(Action):
    def __init__(self, config):
        super(ForceStopVM, self).__init__(config=config)

    def run(self, url, apikey, secretkey, vm_id):
        url_temp = self.config.get('url')

        if url != "" and url is not None:
            url_temp = url

        cs = CloudStack(endpoint=url_temp,
                        key=apikey,
                        secret=secretkey,
                        dangerous_no_tls_verify=True,
                        fetch_result=True)

        if cs.stopVirtualMachine(id=vm_id, forced=True):
            return cs.destroyVirtualMachine(id=vm_id)

        return False
