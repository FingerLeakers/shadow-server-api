#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh Maine'

from shadowserver.shadow_server_api import ShadowServerApi
import json

myteam = ShadowServerApi()
print 'Get list of Anti-Virus Vendors'
print json.dumps(myteam.list_av_engines, sort_keys=False, indent=4)
print 'Get AV Results for NOT FOUND {}'.format('039ea049f6d0f36f55ec064b3b371c4A')
print json.dumps(myteam.get_av('039ea049f6d0f36f55ec064b3b371c4A'), sort_keys=False, indent=4)
print 'Get AV Results for NOT FOUND {}'.format('039ea049f6d0f36f55ec064b3b371c46')
print json.dumps(myteam.get_av('039ea049f6d0f36f55ec064b3b371c46'), sort_keys=False, indent=4)
print 'Get AV Results for {}'.format('5e28284f9b5f9097640d58a73d38ad4c')
print json.dumps(myteam.get_av('5e28284f9b5f9097640d58a73d38ad4c'), sort_keys=False, indent=4)
print 'Get Binary Whitelist Test Results for NOT FOUND {}'.format('039ea049f6d0f36f55ec064b3b371c4A')
print json.dumps(myteam.get_bintest('039ea049f6d0f36f55ec064b3b371c4A'), sort_keys=False, indent=4)
print 'Get Binary Whitelist Test Results for {}'.format('039ea049f6d0f36f55ec064b3b371c46')
print json.dumps(myteam.get_bintest('039ea049f6d0f36f55ec064b3b371c46'), sort_keys=False, indent=4)
print 'Get Binary Whitelist Test Results for {}'.format('5e28284f9b5f9097640d58a73d38ad4c')
print json.dumps(myteam.get_bintest('5e28284f9b5f9097640d58a73d38ad4c'), sort_keys=False, indent=4)
