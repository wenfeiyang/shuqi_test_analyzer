#!/usr/bin/env python
# -*- coding: utf8 -*-
# Created by YWL on 2015/2/27

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'shuqi_app_test'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {

    'device_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },

    'android_version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        #'required': True,
        #'unique': True,
    },

    'test_name': {
    	'type': 'string',
    	'minlength': 1,
        'maxlength': 200,
    },

    'status': {
    	'type': 'integer',
    	'allowed': [0, 1, 2, 3]
    },
}

test_result = {

    'item_title': 'test',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {

	'test_result': test_result,

}