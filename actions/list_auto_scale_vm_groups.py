#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'ListAutoScaleVmGroups'
]


class ListAutoScaleVmGroups(CloudStackAPI):
    def run(self, url, apikey, secretkey, lb_id, projectid):
        cs = self.get_client(url, apikey, secretkey)

        return cs.listAutoScaleVmGroups(lbruleid=lb_id, projectid=projectid)
