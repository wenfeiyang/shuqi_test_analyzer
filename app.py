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
    appium = request.args.get('appium')
    if appium:
        criteria.update(appium_version=appium)
    collection = app.data.driver.db["test_result"]
    tests = collection.distinct("test_name")
    print tests
    result = {}
    overall = {}
    for test in tests:
        print test
        m = re.match(r'.*\((.*)\)', test)
        name = m.group(1).rsplit('.', 1)[0] if m else test
        sta_dict = {"name": name, "pass": 0, "fail": 0, "error": 0}
        if name in result:
            sta_dict = result[name]
        else:
            result[name] = sta_dict
        query = criteria
        query.update(test_name=test)
        query.update(status=0)
        sta_dict["pass"] += collection.find(query).count()
        query.update(status=1)
        sta_dict["fail"] += collection.find(query).count()
        query.update(status=2)
        sta_dict["error"] += collection.find(query).count()
        overall["name"] = "overall"
        query = criteria
        query.update(status=0)
        overall["pass"] =  collection.find(query).count()
        query.update(status=1)
        overall["fail"] =  collection.find(query).count()
        query.update(status=2)
        overall["error"] =  collection.find(query).count()
        return render_template("test_statistic.html", result=result, overall=overall)


@app.route("/tests/failure")
def failure_tests():
    records =  app.data.driver.db["test_result"].find(
        {"status": {"$gt": 0}, "msg": {"$regex": ".+"}}
    )
    return render_template("failure_tests.html", records=records)

@app.route("/tests/statistic")
def tests_statistic():
	test_set = app.data.driver.db["test_result"].distinct("test_name")
	result = {}
	overall = {}
	find_func = app.data.driver.db["test_result"].find
	for test in test_set:
		m = re.match(r'.*\((.*)\)', test)
		name = m.group(1).rsplit('.',1)[0] if m else test
		sta_dict = {"name": name, "pass": 0, "fail": 0, "error": 0}
		if name in result:
			sta_dict = result[name]
		else:
			result[name] = sta_dict
		sta_dict["pass"] += find_func(
			{"test_name": test, "status": 0}
		).count()
		sta_dict["fail"] += find_func(
			{"test_name": test, "status": 1}
		).count()
		sta_dict["error"] += find_func(
			{"test_name": test, "status": 2}
		).count()
	overall["name"] = "overall"
	overall["pass"] = find_func({"status": 0}).count()
	overall["fail"] = find_func({"status": 1}).count()
	overall["error"] = find_func({"status": 2}).count()
 	return render_template("test_statistic.html", result=result, overall=overall)

if __name__ == '__main__':
	app.run(debug=True)