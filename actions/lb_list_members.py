#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'LBListMembers'
]


class LBListMembers(CloudStackAPI):
    def run(self, url, apikey, secretkey, lb_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.listLoadBalancerRuleInstances(id=lb_id)
