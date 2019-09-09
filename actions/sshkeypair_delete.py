#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'SSHKeyPairDelete'
]


class SSHKeyPairDelete(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, project_id):
        cs = self.get_client(url, apikey, secretkey)

        cs.deleteSSHKeyPair(name=name, projectid=project_id)
