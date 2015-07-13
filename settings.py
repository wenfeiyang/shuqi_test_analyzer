#!/usr/bin/env python
# -*- coding: utf8 -*-
# Created by YWL on 2015/2/27

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
# MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'shuqi')
# MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'shuqi')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'shuqi_android_test')

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

commits = {

    'item_title': 'commits',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'commit'
    },

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string',
            'maxlength': 50,
        },

        'branch': {
            'type': 'string',
            'maxlength': 10,
        },

        'committer': {
            'type': 'string',
            'maxlength': 50,
        },
        'lint': {
            'type': 'dict',
            'schema': {
                'fatal': {'type': 'integer'},
                'error': {'type': 'integer'},
                'warn': {'type': 'integer'},
            },
        },
        'findbugs': {
            'type': 'dict',
            'schema': {
                'fatal': {'type': 'integer'},
                'error': {'type': 'integer'},
                'warn': {'type': 'integer'},
            },
        }
    }
}

monkey_result = {
    'item_title': 'monkey result',

    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string'
        },
        'version_name': {
            'type': 'string',
            'maxlength': 10,
        },
        'tag': {
            'type': 'string',
            'maxlength': 10,
        },
        'device': {
            'type': 'string'
        },
        'android_version': {
            'type': 'string'
        },
        'domain': {
            'type': 'integer', 
            'allowed': [0, 1]
        },
        'anr': {
            'type': 'float'
        },
        'crash': {
            'type': 'float'
        },
    }
}

oom_result = {
    'item_title': 'oom result',

    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string'
        },
        'version_name': {
            'type': 'string',
            'maxlength': 10,
        },
        'tag': {
            'type': 'string',
            'maxlength': 10,
        },
        'device': {'type': 'string'},
        'android_version': {'type': 'string'},
        'domain': {'type': 'integer', 'allowed': [0, 1]},
        'scenario': {'type': 'string'},
        'pss_increase': {'type': 'float'},
        'heap_increase': {'type': 'float'},
    }
}

performance_result = {
    'item_title': 'performance result',

    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string'
        },
        'version_name': {
            'type': 'string',
            'maxlength': 10,
        },
        'tag': {
            'type': 'string',
            'maxlength': 10,
        },
        'device': {'type': 'string'},
        'android_version': {'type': 'string'},
        'domain': {'type': 'integer', 'allowed': [0, 1]},
        'scenario': {'type': 'string'},
        'cpu': {'type': 'float'},
        'pss': {'type': 'float'},
        'heap': {'type': 'float'},
        'traffic': {'type': 'float'},
        'jiffies': {'type': 'float'},
    }
}

render_result = {
    'item_title': 'render result',

    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string'
        },
        'version_name': {
            'type': 'string',
            'maxlength': 10,
        },
        'tag': {
            'type': 'string',
            'maxlength': 10,
        },  
        'device': {'type': 'string'},
        'android_version': {'type': 'string'},
        'domain': {'type': 'integer', 'allowed': [0, 1]},
        'activity': {'type': 'string'},
        'fps': {'type': 'integer'},
    } 
}

regression_result = {
    'item_title': 'regression result',

    'resource_methods': ['GET', 'POST'],

    'schema': {
        'commit': {
            'type': 'string'
        },
        'version_name': {
            'type': 'string',
            'maxlength': 10,
        },
        'tag': {
            'type': 'string',
            'maxlength': 10,
        }, 
        'device': {'type': 'string'},
        'android_version': {'type': 'string'},
        'domain': {'type': 'integer', 'allowed': [0, 1]},
        'pass': {'type': 'integer'},
        'fail': {'type': 'integer'},
        'error': {'type': 'integer'},
    }
}

DOMAIN = {
	'ci': commits,
    'ci/regression': regression_result,
    'ci/performance': performance_result,
    'ci/render': render_result,
    'ci/oom': oom_result,
    'ci/monkey': monkey_result,
}