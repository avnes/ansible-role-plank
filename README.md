# ansible-role-plank

![Ansible](https://github.com/avnes/ansible-role-plank/actions/workflows/ansible.yaml/badge.svg)

Ansible role for installing plank and performing basic setup and configuration.

## Requirements

Poetry. Install it from <https://python-poetry.org/docs/>

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

## For pip compability

```bash
poetry export --dev --output requirements.txt
```

## Test

```bash
poetry install
poetry shell
molecule test
```

## License

MIT

## Author Information

<https://github.com/avnes/>
