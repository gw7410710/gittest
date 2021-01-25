*** Settings ***
Library  pylib.common

*** Variables ***
${AA}   SET GLOBAL VARIABLE   11

*** Test Cases ***
添加签约对象1-tc001001


    ${add_object}  add object  我是添加的签约对象
    ${object_info}  evaluate  $add_object['value'][0]
    should be true  $object_info['name']=='我是添加的签约对象'

    ${list_all_object}  list object
    ${object}  evaluate  $list_all_object['value']

    add_object_should_contain  ${object}   ${object_info}[_id]    我是添加的签约对象

    [Teardown]  delete object  ${object_info}[_id]


修改签约对象1-tc001051
    ${add_object}  add object  我是添加的签约对象
    ${add_id}  evaluate  $add_object['value'][0]['_id']

    update object   我是修改之后的签约对象         ${add_id}

    ${all_object}  list object
    ${object}  evaluate   $all_object['value']


    add_object_should_contain  ${object}   ${add_id}    我是修改之后的签约对象


    [Teardown]   delete object  ${add_id}

修改签约对象2-tc001052
    ${before_object}  list object

    update object   签约对象          555555

    ${after_object}  list object

    should be equal  ${before_object}  ${after_object}

删除签约对象1-tc001091
    ${before_object}  list object

    ${add_object}  add object  我是添加的签约对象
    ${object_info}  evaluate  $add_object['value'][0]

    ${delete_ob}  delete object  ${object_info}[_id]
    should be true  $delete_ob=={}


    ${after_object}  list object

    should be equal  ${before_object}  ${after_object}






