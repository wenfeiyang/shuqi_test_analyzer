#!/usr/bin/env python
# -*- coding: utf8 -*-
# Created by YWL on 2015/2/27

from eve import Eve
from flask import render_template

app = Eve(__name__)

@app.route("/tests/")
def tests():
    return render_template('tests.html', name='william')

if __name__ == '__main__':
	app.run(debug=True)