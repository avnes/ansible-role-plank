master: [![Build Status](https://travis-ci.org/avnes/ansible-role-plank.png?branch=master)](https://travis-ci.org/avnes/ansible-role-plank) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-plank.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-plank)

# ansible-role-plank

Ansible role for installing plank and performing basic setup and configuration.

## Requirements

None for running the role.

In order to continuously develop and test this role, you will need docker, pip, molecule, testinfra and python-docker-py installed.

Install docker, pip and python-docker-py with your distributions package manager. Then install molecule and tesinfra with pip:

```
pip install molecule
pip install testinfra
```

## Role Variables

```
config_owner:
  String (mandatory) to specify the Linux user that should have plank setup for them.

plank_dock_items:
  List (mandatory) to specify which applications to add to the plank launcher.
```

More variables (optional) are found in defaults/main.yml, and the rest of them are used with the plankrc.j2 template.

## Dependencies

None

## Example Playbook

```
- hosts: all
  vars:
    owner: 'maya'
    app_list:
      - {name: 'atom', path: '/usr/share/applications/atom.desktop'}
      - {name: 'chromium-browser', path: '/usr/share/applications/chromium-browser.desktop'}
      - {name: 'keepassx2', path: '/usr/share/applications/keepassx2.desktop'}
      - {name: 'lxterminal', path: '/usr/share/applications/lxterminal.desktop'}
      - {name: 'nm-connection-editor', path: '/usr/share/applications/nm-connection-editor.desktop'}
      - {name: 'pcmanfm', path: '/usr/share/applications/pcmanfm.desktop'}
  roles:
     - { role: avnes.ansible-role-plank, config_owner: "{{ owner }}", plank_dock_items: "{{ app_list }}" }
```

## Test

```
ANSIBLE_CONFIG=./role.cfg; export ANSIBLE_CONFIG
ansible-playbook -i tests/inventory --syntax-check tests/test.yml
ansible-playbook -i tests/inventory --check --connection=local --sudo -vvvv tests/test.yml -K
```

## Molecule test

```
molecule create
molecule test
```

## Run

```
ANSIBLE_CONFIG=./role.cfg; export ANSIBLE_CONFIG
ansible-playbook -i tests/inventory --connection=local --sudo -vvvv tests/test.yml -K
```

## License

MIT

## Author Information

<https://github.com/avnes>
