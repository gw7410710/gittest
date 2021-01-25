*** Settings ***
Library  pylib.common.Contract
Library  pylib.common
Library  pylib.common.Contract_classify



Suite Setup   add_contract   1    ${ojbect_id}      ${Contract_classify_ID}   我是测试套件添加的合同     add_contract_id
Suite Teardown     delete_contract   ${add_contract_id}