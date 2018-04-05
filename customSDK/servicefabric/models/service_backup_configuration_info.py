# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .backup_configuration_info import BackupConfigurationInfo


class ServiceBackupConfigurationInfo(BackupConfigurationInfo):
    """Backup configuration information for a specific Service Fabric service
    specifying what backup policy is being applied and suspend description, if
    any.

    :param policy_name: The name of the backup policy which is applicable to
     this Service Fabric application or service or partition.
    :type policy_name: str
    :param policy_inherited_from: Specifies the scope at which the backup
     policy is applied.
     . Possible values include: 'Invalid', 'Partition', 'Service',
     'Application'
    :type policy_inherited_from: str or
     ~azure.servicefabric.models.BackupPolicyScope
    :param suspension_info: Describes the backup suspension details.
    :type suspension_info: ~azure.servicefabric.models.BackupSuspensionInfo
    :param kind: Constant filled by server.
    :type kind: str
    :param service_name: The full name of the service with 'fabric:' URI
     scheme.
    :type service_name: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'policy_name': {'key': 'PolicyName', 'type': 'str'},
        'policy_inherited_from': {'key': 'PolicyInheritedFrom', 'type': 'str'},
        'suspension_info': {'key': 'SuspensionInfo', 'type': 'BackupSuspensionInfo'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
    }

    def __init__(self, policy_name=None, policy_inherited_from=None, suspension_info=None, service_name=None):
        super(ServiceBackupConfigurationInfo, self).__init__(policy_name=policy_name, policy_inherited_from=policy_inherited_from, suspension_info=suspension_info)
        self.service_name = service_name
        self.kind = 'Service'