*** Settings ***
Library  pylib.common

Suite Setup  add_object  我是测试套件添加的签约对象  ojbect_id
Suite Teardown  delete_object  ${ojbect_id}


