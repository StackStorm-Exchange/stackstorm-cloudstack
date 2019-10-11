#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'EnableAutoScaleVmGroups'
]


class EnableAutoScaleVmGroups(CloudStackAPI):
    def run(self, url, apikey, secretkey, id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.enableAutoScaleVmGroup(id=id)
