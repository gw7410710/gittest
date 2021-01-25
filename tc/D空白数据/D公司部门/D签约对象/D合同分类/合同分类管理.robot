*** Settings ***
Library  pylib.common.Contract_classify


*** Test Cases ***
添加合同类型1-tc002001
    ${Contract_classify}  add Contract classify   宝马黑武士合同
    ${add_id}  evaluate   $Contract_classify['value'][0]['_id']

    ${list_Contract_classify}  list Contract classify

    ${list_}    evaluate  $list_Contract_classify['value']

    Contract_classify_should_contain  ${list_}   ${add_id}   宝马黑武士合同

    [Teardown]  delete Contract classify  ${Contract_classify}[value][0][_id]


修改合同类型1-tc002051

    ${Contract_classify}  add Contract classify   宝马黑武士
    ${add_id}  evaluate   $Contract_classify['value'][0]['_id']

    ${up_Contract_classify}    update Contract classify    我是修改之后的合同分类     ${add_id}

    ${list_Contract_classify}  list Contract classify

    ${list_}    evaluate  $list_Contract_classify['value']

    Contract_classify_should_contain  ${list_}   ${add_id}   我是修改之后的合同分类

    [Teardown]  delete Contract classify   ${add_id}


修改合同类型2-tc002052
    ${before}   list Contract classify

    update Contract classify  我是修改之后的合同分类    555

    ${later}   list Contract classify

    should be equal  ${before}   ${later}


删除合同类型1-tc002091
    ${before}   list Contract classify

    ${Contract_classify}  add Contract classify   宝马黑武士
    ${add_id}  evaluate   $Contract_classify['value'][0]['_id']

    ${delete}  delete Contract classify   ${add_id}
    should be true  $delete=={}

    ${later}   list Contract classify

    should be equal  ${before}   ${later}




