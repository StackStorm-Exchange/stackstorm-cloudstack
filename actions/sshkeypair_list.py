#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'SSHKeyPairList'
]


class SSHKeyPairList(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, project_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.listSSHKeyPairs(name=name, projectid=project_id)
