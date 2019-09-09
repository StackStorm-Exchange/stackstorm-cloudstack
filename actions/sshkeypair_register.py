#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'SSHKeyPairRegister'
]


class SSHKeyPairRegister(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, public_key, project_id):
        cs = self.get_client(url, apikey, secretkey)

        cs.registerSSHKeyPair(name=name, publickey=public_key, projectid=project_id)
