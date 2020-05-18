"""Role testing files using testinfra."""


def test_masquerade_enabled(host):
    command = """sudo firewall-cmd --zone=public --query-masquerade | \
    grep -c no"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
