# CloudStack Integration Pack

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