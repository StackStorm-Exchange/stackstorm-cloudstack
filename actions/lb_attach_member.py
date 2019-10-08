#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'LBAttachhMember'
]


class LBAttachhMember(CloudStackAPI):
    def run(self, url, apikey, secretkey, lb_id, virtualmachineids, virtualmachineids):
        cs = self.get_client(url, apikey, secretkey)

        return cs.assignToLoadBalancerRule(id=lb_id, virtualmachineids=virtualmachineids)
