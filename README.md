master: [![Build Status](https://travis-ci.org/avnes/ansible-role-plank.png?branch=master)](https://travis-ci.org/avnes/ansible-role-plank) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-plank.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-plank)

# ansible-role-plank

Ansible role for installing plank and performing basic setup and configuration.

## Requirements

None.

## Role Variables

```yaml
config_owner:
  String (mandatory) to specify the Linux user that should have plank setup for them.
  Default: "{{ ansible_user_id }}"

config_owner_primary_group:
  String (optional) to specify the group ownership for the plank setup.
  Default: "{{ config_owner }}"

plank_dock_items:
  List (mandatory) to specify which applications to add to the plank launcher.
```

More variables (optional) are found in defaults/main.yml, and the rest of them are used with the plankrc.j2 template.

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  vars:
    config_owner: 'maya'
    plank_dock_items:
      - {name: 'atom', path: '/usr/share/applications/atom.desktop'}
      - {name: 'chromium-browser', path: '/usr/share/applications/chromium-browser.desktop'}
      - {name: 'keepassx2', path: '/usr/share/applications/keepassx2.desktop'}
      - {name: 'lxterminal', path: '/usr/share/applications/lxterminal.desktop'}
      - {name: 'nm-connection-editor', path: '/usr/share/applications/nm-connection-editor.desktop'}
      - {name: 'pcmanfm', path: '/usr/share/applications/pcmanfm.desktop'}
  roles:
     - { role: avnes.ansible-role-plank }
```

## Molecule test

```bash
virtualenv ~/.virtualenv/ansible-role-plank
source ~/.virtualenv/ansible-role-plank/bin/activate
pip install -r requirements.txt
molecule test
```

## License

MIT

## Author Information

<https://github.com/avnes>
