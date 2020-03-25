#!/usr/bin/env python

from cs import CloudStack
from st2common.runners.base_action import Action

__all__ = [
    'CloudStackAPI'
]


class CloudStackAPI(Action):
    def __init__(self, config):
        super(CloudStackAPI, self).__init__(config=config)

    def get_client(self, url, apikey, secretkey, timeout=10):
        url_temp = self.config.get('url')

        if url != "" and url is not None:
            url_temp = url

        cs = CloudStack(endpoint=url_temp,
                        key=apikey,
                        secret=secretkey,
                        dangerous_no_tls_verify=True,
                        fetch_result=True,
                        method='POST',
                        timeout=timeout)
        return cs
