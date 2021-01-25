*** Settings ***
Library  pylib.common.Contract
Library  pylib.common
Library  pylib.common.Contract_classify


*** Test Cases ***
添加合同2-tc003002

    add object  测试用例签约对象   object_id
    add_Contract_classify    测试用例合同分类   Contract_classify_id

    ${add_}  add contract  00  ${object_id}   ${Contract_classify_id}   3002测试用例合同名称   contract_id
    ${add_info}  evaluate  $add_['value'][0]

    ${list}   list contract
    ${list_info}  evaluate  $list['value'][1]

    should be true  $list_info['name']=='3002测试用例合同名称'
    should be true  $list_info['_id']==$add_info['_id']

    [Teardown]   RUN KEYWORDS  delete_contract  ${contract_id}  AND  delete object   ${object_id}  AND  delete Contract classify  ${Contract_classify_id}


修改合同1-tc003051
    add object  测试用例签约对象   object_id
    add_Contract_classify    测试用例合同分类   Contract_classify_id

    ${add_}  add contract  00  ${object_id}   ${Contract_classify_id}   3051测试用例合同名称   contract_id
    ${add_info}  evaluate  $add_['value'][0]

    update contract   ${contract_id}  00    我是修改之后的合同名称

    ${list}   list contract
    ${list_info}  evaluate  $list['value']
    ${modified}  evaluate   $list_info[1]['modified']

   contract_should_contain222   ${list_info}   ${add_info}[_id]   ${Contract_classify_id}
    ...  ${add_info}[created]   ${modified}   我是修改之后的合同名称    00    ${object_id}           ${add_info}[serial_number]

    [Teardown]   RUN KEYWORDS  delete_contract  ${contract_id}  AND  delete object   ${object_id}  AND  delete Contract classify  ${Contract_classify_id}

修改合同2-tc003052
    ${before}  list contract

    update contract   999  00    我是修改之后的合同名称

    ${last}  list contract

    should be equal  ${before}   ${last}

删除合同1-tc003091
    ${before}  list contract

    add object  测试用例签约对象   object_id
    add_Contract_classify    测试用例合同分类   Contract_classify_id

    ${add_}  add contract  00  ${object_id}   ${Contract_classify_id}   3091测试用例合同名称   contract_id
    ${add_info}  evaluate  $add_['value'][0]

    ${del}  delete contract   ${contract_id}
    should be true  $del=={}

    ${last}  list contract

    should be equal  ${before}   ${last}

