#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'LBDettachhMember'
]


class LBDettachhMember(CloudStackAPI):
    def run(self, url, apikey, secretkey, lb_id, vm_ids):
        cs = self.get_client(url, apikey, secretkey)

        return cs.removeFromLoadBalancerRule(id=lb_id, virtualmachineids=vm_ids)
