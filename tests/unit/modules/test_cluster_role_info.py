from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible_collections.sensu.sensu_go.plugins.module_utils import (
    errors, utils,
)
from ansible_collections.sensu.sensu_go.plugins.modules import cluster_role_info

from .common.utils import (
    AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args,
)


class TestClusterRoleInfo(ModuleTestCase):
    def test_get_all_cluster_roles(self, mocker):
        get_mock = mocker.patch.object(utils, "get")
        get_mock.return_value = [1, 2, 3]
        set_module_args()

        with pytest.raises(AnsibleExitJson) as context:
            cluster_role_info.main()

        _client, path = get_mock.call_args[0]
        assert path == "/clusterroles"
        assert context.value.args[0]["objects"] == [1, 2, 3]

    def test_get_single_cluster_role(self, mocker):
        get_mock = mocker.patch.object(utils, "get")
        get_mock.return_value = 1
        set_module_args(name="test-cluster-role")

        with pytest.raises(AnsibleExitJson) as context:
            cluster_role_info.main()

        _client, path = get_mock.call_args[0]
        assert path == "/clusterroles/test-cluster-role"
        assert context.value.args[0]["objects"] == [1]

    def test_failure(self, mocker):
        get_mock = mocker.patch.object(utils, "get")
        get_mock.side_effect = errors.Error("Bad error")
        set_module_args(name="sample-cluster-role")

        with pytest.raises(AnsibleFailJson):
            cluster_role_info.main()
