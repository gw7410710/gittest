*** Settings ***
Library  pylib.common

*** Test Cases ***
添加公司分部1-tc000001
    ${add_or}   add organize  扬州
    ${add_name}   list organize
    ${add_organize}    evaluate  $add_name['value'][1]
    should be true  $add_organize['fullname']=='扬州'
    should be true  $add_organize['_id']==$add_or['value'][0]['_id']

    [Teardown]   delete organize  ${add_or}[value][0][_id]



