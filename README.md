# CloudStack Integration Pack

Apache CloudStack is open source software designed to deploy and manage large
networks of virtual machines, as a highly available, highly scalable
Infrastructure as a Service (IaaS) cloud computing platform. CloudStack is used
by a number of service providers to offer public cloud services, and by many
companies to provide an on-premises (private) cloud offering, or as part of a
hybrid cloud solution.

CloudStack is a turnkey solution that includes the entire "stack" of features
most organizations want with an IaaS cloud: compute orchestration,
Network-as-a-Service, user and account management, a full and open native API,
resource accounting, and a first-class User Interface (UI).

CloudStack currently supports the most popular hypervisors:
VMware vSphere, KVM, XenServer, XenProject and Hyper-V as well as
OVM and LXC containers.

Users can manage their cloud with an easy to use Web interface, command line
tools, and/or a full-featured query based API.

For more information on Apache CloudStack, please visit the [website](http://cloudstack.apache.org)

## Configuration

```yaml
url: http://localhost:8080/client/api
```

## Actions

#### VM

* `vm_deploy` - deploy a VM
* `vm_get_info` - get VM information
* `vm_reboot` - reboot a VM
* `vm_start` - start a VM
* `vm_stop` - stop a VM
* `vm_destroy` - destroy a VM
* `vm_force_destroy` - force destroy a VM

#### LoadBalancer

* `lb_list_members` - list members from a LoadBalancer

#### SSH KeyPair

* `sshkeypair_create` - create a SSH KeyPair
* `sshkeypair_delete` - delete a SSH KeyPair
* `sshkeypair_list` - list a SSH KeyPair
* `sshkeypair_register` - register a SSH KeyPair

#### Project

* `project_create` - create a Project
* `delete_create` - delete a Project

#### Network

* `network_create_globo` - create a Network GloboNetwork
* `network_delete_globo` - delete a Network GloboNetwork
* `network_restart` - restart a Network
* `network_update` - update a Network