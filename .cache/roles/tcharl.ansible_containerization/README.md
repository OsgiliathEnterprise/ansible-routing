Containerization OverlayFS
=========


* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_containerization-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_containerization)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-containerization/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-containerization.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-containerization)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role enriches the original [geerlinguy docker role](https://github.com/geerlingguy/ansible-role-docker) and use the [Ansible volumes plus](https://github.com/OsgiliathEnterprise/ansible-volumes) role in order to add overlayfs driver support configuration for docker

Requirements
------------

You should first execute `./configure` first, which will download the requirements in siblings folders.
roles_path = ./roles:./roles/community


Molecule tests
--------------

To execute test, build your own Fedora-33 Packer image enabling cgroup V1 and call it yourpseudo/fedora-33.
Procedure:

```shell script
git clone git@github.com:chef/bento.git
cd "$(dirname ${BASH_SOURCE[0]})/bento/packer_templates/fedora"
sed -i -e "s/dnf -y install \(.*\)/dnf -y install \1 grubby \&\& grubby --update-kernel=ALL --args=\"systemd.unified_cgroup_hierarchy=0\" --make-default/" bento/packer_templates/fedora/scripts/install-supporting-packages.sh
packer build -var "box_basename=$distroversion" -only=$PACKER_VM_DRIVER $distroversion.json

cd "$(dirname ${BASH_SOURCE[0]})/bento/builds
vagrant box add $distroversion.virtualbox.box --name platform/$distroshortversion
```

However, a base image (tcharl/fedora-33-cgroupv1) with these properties has been published to vagrant cloud so executin `molecule test` will suffice!

Role Variables
--------------

Only [dependencies variables](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/molecule.yml) at all but those of the dependencies, see [molecule tests](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/tests/test_default.py) for more info.

Dependencies
------------

As said
 * [geerlinguy docker role](https://github.com/geerlingguy/ansible-role-docker)
 * [Ansible volumes](https://galaxy.ansible.com/tcharl/ansible_volumes)

Example Playbook
----------------

See the [vars declared](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/molecule.yml) on the molecule test, as well as [their impact](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/tests/test_default.py) 


License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
