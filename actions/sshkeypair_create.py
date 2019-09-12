#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'SSHKeyPairCreate'
]


class SSHKeyPairCreate(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, project_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.createSSHKeyPair(name=name, projectid=project_id)
