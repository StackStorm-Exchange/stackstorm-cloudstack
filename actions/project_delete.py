#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'ProjectDelete'
]


class ProjectDelete(CloudStackAPI):
    def run(self, url, apikey, secretkey, project_id):
        cs = self.get_client(url, apikey, secretkey)

        return cs.deleteProject(id=project_id)
