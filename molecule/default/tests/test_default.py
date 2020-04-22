"""Role testing files using testinfra."""


def test_redirect_rule_set(host):
    command = """sudo firewall-cmd --list-all --zone=public | \
    grep 'rule family=\"ipv4\" forward-port port=\"6752\" \
    protocol=\"tcp\" to-port=\"22\" to-addr=\"192.168.1.10\"'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
