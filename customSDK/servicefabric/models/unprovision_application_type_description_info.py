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

from msrest.serialization import Model


class UnprovisionApplicationTypeDescriptionInfo(Model):
    """Describes the operation to unregister or unprovision an application type
    and its version that was registered with the Service Fabric.

    :param application_type_version: The version of the application type as
     defined in the application manifest.
    :type application_type_version: str
    :param async_property: The flag indicating whether or not unprovision
     should occur asynchronously. When set to true, the unprovision operation
     returns when the request is accepted by the system, and the unprovision
     operation continues without any timeout limit. The default value is false.
     However, we recommend setting it to true for large application packages
     that were provisioned.
    :type async_property: bool
    """

    _validation = {
        'application_type_version': {'required': True},
    }

    _attribute_map = {
        'application_type_version': {'key': 'ApplicationTypeVersion', 'type': 'str'},
        'async_property': {'key': 'Async', 'type': 'bool'},
    }

    def __init__(self, application_type_version, async_property=None):
        super(UnprovisionApplicationTypeDescriptionInfo, self).__init__()
        self.application_type_version = application_type_version
        self.async_property = async_property
