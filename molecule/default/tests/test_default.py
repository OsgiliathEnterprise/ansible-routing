"""Role testing files using testinfra."""


def test_masquerade_enabled(host):
    with host.sudo():
        command = """firewall-cmd --zone=public --query-masquerade | \
        grep -c yes"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_redirect_rule_set(host):
    with host.sudo():
        command = """firewall-cmd --query-rich-rule=\"rule family=\"ipv4\" \
        forward-port port=\"6752\" \
        protocol=\"tcp\" to-port=\"22\" to-addr=\"192.168.1.10\" \
        log prefix=\"ssh-to-guest\"\" | \
        grep -c yes"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_port_is_opened(host):
    with host.sudo():
        command = """firewall-cmd --zone=public --query-port=\"6753/tcp\" \
        | grep -c yes"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_docker_is_installed(host):
    with host.sudo():
        command = """systemctl status docker.service | \
        grep -c 'active (running)'"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_is_installed(host):
    with host.sudo():
        command = """docker ps | \
        grep -c nginx-proxy"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_port_is_opened(host):
    with host.sudo():
        command = """docker ps | \
        grep -c '80/tcp'"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_port2_is_opened(host):
    with host.sudo():
        command = """docker ps | \
        grep -c '443/tcp'"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_vhost_files_are_present(host):
    with host.sudo():
        command = """ls /usr/share/dockerdata/nginx/vhost.d | \
        grep -c 'idm.'"""
        cmd = host.run(command)
    assert '2' in cmd.stdout
