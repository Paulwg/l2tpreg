# -*- coding: utf-8 -*-
"""The definitions."""

from __future__ import unicode_literals


REGISTRY_FILE_TYPE_NTUSER = 'NTUSER'
REGISTRY_FILE_TYPE_SAM = 'SAM'
REGISTRY_FILE_TYPE_SECURITY = 'SECURITY'
REGISTRY_FILE_TYPE_SOFTWARE = 'SOFTWARE'
REGISTRY_FILE_TYPE_SYSTEM = 'SYSTEM'
REGISTRY_FILE_TYPE_UNKNOWN = 'UNKNOWN'
REGISTRY_FILE_TYPE_USRCLASS = 'USRCLASS'

REGISTRY_FILE_TYPES = frozenset([
    REGISTRY_FILE_TYPE_NTUSER,
    REGISTRY_FILE_TYPE_SAM,
    REGISTRY_FILE_TYPE_SECURITY,
    REGISTRY_FILE_TYPE_SOFTWARE,
    REGISTRY_FILE_TYPE_SYSTEM,
    REGISTRY_FILE_TYPE_USRCLASS])
