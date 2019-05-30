#!/usr/bin/env python
#
# Copyright: (c) 2019, Peter Sprygada (psprygad@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
import sys
import json
import traceback

from argparse import ArgumentParser
from getpass import getpass

from six import iteritems
from six.moves import input

from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import connection_loader


def get_connection(args):
    """ Create an instance of connection based on the command line arguments

    :param args: an instance of argparse.Namespace

    :returns: an instance of ansible.plugins.connection.Connection
    """
    play_context = PlayContext()
    play_context.connection = 'network_cli'
    play_context.network_os = args.network_os
    play_context.remote_addr = args.host
    play_context.port = args.port
    play_context.timeout = args.timeout
    play_context.remote_user = args.username or input('Username: ')
    play_context.password = args.password or getpass('Password: ')


    conn = connection_loader.get('network_cli', play_context, '/dev/null')
    conn._connect()

    return conn


def run():
    parser = ArgumentParser()

    parser.add_argument('command', nargs='*',
                        help='Command(s) to send to the remote device')

    parser.add_argument('host',
                        help='Hostname or IP address of the remote host')

    parser.add_argument('-p', '--port', default=22,
                        help='The SSH port to connect the to (default=22)')

    parser.add_argument('-u', '--username',
                        help='The username used to authenticate with')

    parser.add_argument('-P', '--password',
                        help='The password used to authenticate with')

    parser.add_argument('-t', '--timeout', default=30,
                        help='The timeout value for the connection (default=30)')

    parser.add_argument('-n', '--network-os', default='linux',
                        help='The network-os plugin to load')

    parser.add_argument('--json', action='store_true',
                       help='Return the output as a JSON')

    args = parser.parse_args()

    conn = None
    rc = 255

    try:
        conn = get_connection(args)

        output = {}

        for command in args.command:
            output[command] = conn.cliconf.get(command)

        for key, value in iteritems(output):
            if not args.json:
                print('{}\n'.format(value))
            else:
                print(json.dumps(output, indent=4))

        conn.close()
        rc = 0

    except Exception as exc:
        traceback.print_exc()

    finally:
        sys.exit(rc)

