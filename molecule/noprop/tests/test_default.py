"""Role testing files using testinfra."""


def test_masquerade_enabled(host):
    command = """sudo firewall-cmd --list-all --zone=public | \
    grep -c 'interfaces: eth0'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
