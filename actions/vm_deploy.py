#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'VMDeploy'
]


class VMDeploy(CloudStackAPI):
    def run(self,
            url, apikey, secretkey, name, project_id, zone_id, template_id,
            service_offering_id, network_ids, hyper_visor, userdata):
        cs = self.get_client(url, apikey, secretkey)

        return cs.deployVirtualMachine(
            name=name,
            projectid=project_id,
            zoneid=zone_id,
            templateid=template_id,
            networkids=network_ids,
            serviceofferingid=service_offering_id,
            hypervisor=hyper_visor,
            userdata=userdata)
