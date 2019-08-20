#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Paul Arthur <paul.arthur@flowerysong.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: sensu_go_handler_info
author: "Paul Arthur (@flowerysong)"
short_description: Lists Sensu handlers
description:
  - 'For more information, refer to the Sensu documentation: U(https://docs.sensu.io/sensu-go/latest/reference/handlers/)'
version_added: 0.1.0
extends_documentation_fragment:
  - sensu.sensu_go.base
  - sensu.sensu_go.info
'''

EXAMPLES = '''
- name: List Sensu handlers
  sensu_go_handler_info:
  register: result
'''

RETURN = '''
handlers:
  description: list of Sensu handlers
  returned: always
  type: list
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sensu.sensu_go.plugins.module_utils.base import sensu_argument_spec, AnsibleSensuClient


def main():
    argspec = sensu_argument_spec()
    argspec.update(
        dict(
            name=dict(),
        )
    )

    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=argspec,
    )

    client = AnsibleSensuClient(module)

    if module.params['name']:
        result = [client.get('/handlers/{0}'.format(module.params['name']))]
    else:
        result = client.get('/handlers')

    module.exit_json(changed=False, handlers=result)


if __name__ == '__main__':
    main()
