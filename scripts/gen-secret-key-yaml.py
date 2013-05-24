#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import exists
from base64 import b64encode
import yaml

secret_key_yaml_path = 'secret-key.yaml'

if exists(secret_key_yaml_path):
    if raw_input("override existent '%s'? [Y/n]" % secret_key_yaml_path) not in 'Yy':
        print 'donoting.'
        sys.exit()

with open(secret_key_yaml_path, 'w') as f:
    yaml.dump({'SECRET_KEY': os.urandom(48)}, f)
print "writed to '%s'." % secret_key_yaml_path
