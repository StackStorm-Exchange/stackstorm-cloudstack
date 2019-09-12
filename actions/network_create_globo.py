#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'NetworkCreateGlobo'
]


class NetworkCreateGlobo(CloudStackAPI):
    def run(self,
            url, apikey, secretkey, zone_id, network_offering_id, napi_environment_id,
            name, display_text, is_ipv6, project_id, subnet, acl_type):
        cs = self.get_client(url, apikey, secretkey)

        return cs.addNetworkViaGloboNetwork(
            zoneId=zone_id,
            networkofferingid=network_offering_id,
            napienvironmentid=napi_environment_id,
            name=name,
            displaytext=display_text,
            isipv6=is_ipv6,
            projectid=project_id,
            subnet=subnet,
            acltype=acl_type
        )
