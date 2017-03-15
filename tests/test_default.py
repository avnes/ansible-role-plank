import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_dockitem_files(File):
    names = ['atom', 'chromium-browser', 'keepassx2', 'lxterminal', 'trash',
             'nm-connection-editor', 'pcmanfm', 'clippy', 'clock', 'desktop']
    directory = '/home/ansible-test-user/.config/plank/dock1/launchers/'
    for name in names:
        f = File(directory + name + '.dockitem')

        assert f.exists
        assert f.user == 'ansible-test-user'
        assert f.group == 'ansible-test-user'
        assert f.mode == 0o700
