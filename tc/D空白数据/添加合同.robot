*** Settings ***
Library  pylib.common.Contract
Library  pylib.common
Library  pylib.common.Contract_classify


*** Test Cases ***
添加合同1-tc003001
    add object  测试用例签约对象   object_id
    add_Contract_classify    测试用例合同分类   Contract_classify_id

    ${add_}  add contract  00  ${object_id}   ${Contract_classify_id}   我是3001用例添加的合同   contract_id
    ${add_info}  evaluate  $add_['value'][0]

    ${list}   list contract
    ${list_info}  evaluate  $list['value']

    contract_should_contain   ${list_info}   ${add_info}[_id]   ${Contract_classify_id}
    ...  ${add_info}[created]   我是3001用例添加的合同    ${add_info}[no]    ${object_id}           ${add_info}[serial_number]


    [Teardown]   RUN KEYWORDS  delete_contract  ${contract_id}  AND  delete object   ${object_id}  AND  delete Contract classify  ${Contract_classify_id}


测试--9999
      ${list}    create list    [1,2,3]
      LOG TO CONSOLE  @{list}
