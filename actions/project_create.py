#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'ProjectCreate'
]


class ProjectCreate(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, display_text, extra_parameters):
        cs = self.get_client(url, apikey, secretkey)

        return cs.createProject(name=name, displaytext=display_text, **extra_parameters)
