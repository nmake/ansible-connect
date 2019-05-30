# ansible-connect

This project provides a direcl way to consume the `network_cli` connection
plugin that ships with Ansible.  It provides a command line executable for
sending a command to a remote device and returning its output.

This script has been tested to work with Ansible 2.8 or later and Python 3.6

This script is made available for free as-is for testing only and is not
maintaned or supported


## Example usage

```
$ ansible-connect --help
usage: ansible-connect [-h] [-p PORT] [-u USERNAME] [-P PASSWORD] [-t TIMEOUT]
                       [-n NETWORK_OS] [--json]
                       [command [command ...]] host

positional arguments:
  command               Command(s) to send to the remote device
  host                  Hostname or IP address of the remote host

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  The SSH port to connect the to (default=22)
  -u USERNAME, --username USERNAME
                        The username used to authenticate with
  -P PASSWORD, --password PASSWORD
                        The password used to authenticate with
  -t TIMEOUT, --timeout TIMEOUT
                        The timeout value for the connection (default=30)
  -n NETWORK_OS, --network-os NETWORK_OS
                        The network-os plugin to load
  --json                Return the output as a JSON


$ ansible-connect -u bob -n vyos "show config" vyos101
Password:

interfaces {
    ethernet eth0 {
        address dhcp
        hw-id 52:54:00:eb:f9:25
        smp-affinity auto
    }
    loopback lo {
    }
}
service {
    lldp {
    }
    ssh {
    }
}
system {
    config-management {
        commit-revisions 100
    }
    console {
        device ttyS0 {
            speed 9600
        }
    }
    host-name vyos101
    login {
        user vyos {
            authentication {
                encrypted-password ****************
                plaintext-password ****************
            }
            level admin
        }
    }
    ntp {
        server 0.pool.ntp.org {
        }
        server 1.pool.ntp.org {
        }
        server 2.pool.ntp.org {
        }
    }
    syslog {
        global {
            facility all {
                level info
            }
            facility protocols {
                level debug
            }
        }
    }
    time-zone UTC
}

```
