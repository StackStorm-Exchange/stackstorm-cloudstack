#!/usr/bin/env python

from lib.cloudstack import CloudStackAPI

__all__ = [
    'LBGloboCreate'
]


class LBGloboCreate(CloudStackAPI):
    def run(self, url, apikey, secretkey, name, algorithm, publicport,
            privateport, projectid, openfirewall, networkid,
            additionalportmap, healthchecktype, healthcheckrequest,
            expectedhealthcheck, lbenvironmentid, timeoutrequest):

        cs = self.get_client(url, apikey, secretkey, timeout=timeoutrequest)

        return cs.createGloboLoadBalancer(
            algorithm=algorithm,
            name=name,
            publicport=publicport,
            projectid=projectid,
            privateport=privateport,
            openfirewall=str(openfirewall),
            networkid=networkid,
            additionalportmap=additionalportmap,
            healthcheckType=healthchecktype,
            healthchecktype=healthcheckrequest,
            expectedhealthcheck=expectedhealthcheck,
            lbenvironmentid=str(lbenvironmentid)
        )
