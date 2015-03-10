#!/usr/bin/env python
# -*- coding: utf8 -*-
# Created by YWL on 2015/2/27

from eve import Eve
from flask import render_template
from flask import request
import re

app = Eve(__name__)


@app.route("/tests")
def get_test_result():
    criteria = {}
    status = request.args.get('status')
    if status:
        criteria.update(status=int(status))
    records = app.data.driver.db["test_result"].find(criteria)
    return render_template("test_result.html", records=records)

@app.route("/statistic")
def get_test_statistic():
    criteria = {}
    device = request.args.get('device')
    if device:
        criteria.update(device_name=device)
    else:
        device = "All devices"
    version = request.args.get('ver')
    if version:
        criteria.update(app_version=version)
    else:
        version = "All versions"

    test_set = app.data.driver.db["test_map"].find()
    find_func = app.data.driver.db["test_result"].find
    result = {}
    overall = {}
    for test in test_set:
        id = test['test_id']
        test_id = int(id)
        sta_dict = {"id": test_id, "description": test['test_description'], "pass": 0, "fail": 0, "error": 0}
        query = criteria.copy()
        query.update(test_id=id, status=0)
        sta_dict["pass"] = find_func(query).count()
        query.update(test_id=id, status=1)
        sta_dict["fail"] = find_func(query).count()
        query.update(test_id=id, status=2)
        sta_dict["error"] = find_func(query).count()
        result[test_id] = sta_dict
    overall["description"] = u"总体结果"
    query = criteria.copy()
    query.update(status=0)
    overall["pass"] = find_func(query).count()
    query.update(status=1)
    overall["fail"] = find_func(query).count()
    query.update(status=2)
    overall["error"] = find_func(query).count()
    return render_template("test_statistic.html", device=device, version=version, result=result, overall=overall)


@app.route("/tests/failure")
def failure_tests():
    records =  app.data.driver.db["test_result"].find(
        {"status": {"$gt": 0}, "msg": {"$regex": ".+"}}
    )
    return render_template("failure_tests.html", records=records)


if __name__ == '__main__':
	app.run(host='10.3.86.107')