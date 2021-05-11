Routing
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_routing-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_routing)
* Lint: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-routing/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-routing.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-routing)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role let you configure simple port or port/IP redirections using firewalld masquerade

Also, it configures nginx using docker, the goal being to configure virtualhost in the mid term

Requirements
------------

Ansible :-), but also some [collections](./requirements-collections.yml) and some [roles](./requirements.yml)

Role Variables
--------------

```
firewalld_zones:
  - name: public # optional
    nics: # optional, will take all the network interfaces of the machine by default
      - eth0 # optional
    masquerade: true
    port_forward_rules:
      - port_forward_rule: ssh-to-guest
        family: ipv4 # optional
        from_port: 6752
        protocol: tcp # optional
        to_address: 192.168.1.10
        to_port: 22
    enabled_services:
      - service: ssh
    enabled_ports:
      - port: 6753
        protocol: tcp 
    letsencrypt_default_email: toto@mymail # for letencrypt
    virtual_hosts:
      - name: idm.osgiliath.net # Virual host
        upstream: "idm.internal.osgiliath.net" # upstream server to proxy
        referer_suffix: "/ipa/ui" # referer header suffix
        proto: https # upstream proto
        container: False # proxy container or real VM/bare metal
        gen_certs: True # use letsencrypt to generate frontend certificate
        volumes:
          - "/etc/ipa:/etc/ipa:ro" # additional volumes to mount in proxy
        additional_nginx_headers:
          - "proxy_ssl_trusted_certificate /etc/ipa/ca.crt" # Additional nginx headers
        ports_binding:
          - "80:80" # mandatory for letsencrypt
          - "443:443"
      - name: idm.osgiliath.test
        ports_binding:
          - "80:80" # mandatory for letsencrypt
          - "443:443"
        gen_certs: yes # lets encrypt will take care of certificates
        

```

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
