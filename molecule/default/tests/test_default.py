import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_goofys_binary_exists(host):
    assert host.file('/usr/local/bin/goofys').exists


def test_goofys_binary_file(host):
    assert host.file('/usr/local/bin/goofys').is_file


def test_goofys_binary_which(host):
    assert host.check_output('which goofys') == '/usr/local/bin/goofys'
