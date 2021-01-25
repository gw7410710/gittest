*** Settings ***
Library  pylib.common

Suite Setup   add_organize    我是测试套件添加的部门   suite_org_id
Suite Teardown   delete_organize     ${suite_org_id}