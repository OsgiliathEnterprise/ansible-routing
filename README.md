Routing
=========

This role let you configure simple port or port/IP redirections using firewalld masquerade

Requirements
------------

Ansible :-)

Role Variables
--------------

```
firewalld_zones:
  - name: public # optional
    nics:
      - eth0 # optional
    masquerade: true
    port_forward_rules:
      - port_forward_rule: ssh-to-guest
        family: ipv4 # optional
        from_port: 6752
        protocol: tcp # optional
        to_address: 192.168.1.10
        to_port: 22

```

License
-------


[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
