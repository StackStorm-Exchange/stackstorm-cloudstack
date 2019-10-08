# Change Log

## 0.5.15

- Add attach and dettach lb member

## 0.5.14

- Add missing project_id at vm_get_info action

## 0.5.13

- Fix sshkeypair_register name and entry_point

## 0.5.12

- Fix parameters properties

## 0.5.11

- Fix `network_delete_globo` lib action

## 0.5.10

- Fix network_update name and entry_point

## 0.5.9

- Remove enum properties for `subnet`

## 0.5.8

- Remove required from boolean field `is_ipv6`
- Change to string type at `subnet`

## 0.5.7

- Add default value at project_create `extra_parameters`
- Remove immutable properties from `acl_type` and `subnet`

## 0.5.6

- Add extra_parameters at project create action

## 0.5.5

- Using POST method at CloudStack client

## 0.5.4

- Fix unused variable at vm deploy action

## 0.5.3

- Fix variables name

## 0.5.2

- Fix enum at network_create_globo.yaml

## 0.5.1

- Fix missing returns

## 0.5.0

- Add Network create Globo command
- Add Network delete Globo command
- Add Network restart command
- Add Network update command

## 0.4.0

- Add Project create command
- Add Project delete command

## 0.3.0

- Add SSHKeyPair create command
- Add SSHKeyPair delete command
- Add SSHKeyPair list command
- Add SSHKeyPair register command

## 0.2.0

- Add VM destroy command
- Add VM stop command
- Add VM start command
- Add VM deploy command
- Add VM reboot command

## 0.1.0

- Initial pack integration