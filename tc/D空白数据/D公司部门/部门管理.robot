*** Settings ***
Library  pylib.common

*** Test Cases ***
添加公司分部2-tc000002
    ${add_or}   add organize  我是B公司
    ${add_name}   list organize
    ${add_organize}    evaluate  $add_name['value']

    organize_should_contain  ${add_organize}    ${add_or}[value][0][_id]  ${add_or}[value][0][created]  我是B公司

    [Teardown]   delete organize  ${add_or}[value][0][_id]



修改公司分部1-tc000051
    ${before_org}  add organize  我是之前的公司
    ${need_mod_org}  evaluate   $before_org['value'][0]['_id']
    ${update_org}  update_organize  我是修改之后的公司  ${need_mod_org}

    ${after_org}  list organize
    ${after_org}  evaluate  $after_org['value'][2]['fullname']
    should be true  $after_org=='我是修改之后的公司'

    [Teardown]   delete organize   ${need_mod_org}



修改公司分部2-tc000052
    ${before_org}  add organize  我是之前的公司
    ${need_mod_org}  evaluate   $before_org['value'][0]['_id']
    ${update_org}  update_organize  我是修改之后的公司  9999
    should be true  $update_org['error']['code']==500

    [Teardown]   delete organize   ${need_mod_org}


删除公司分部1-tc000091
    ${all_org1}   list organize
    ${before_org}  add organize  我是之前的公司
    ${need_mod_org}  evaluate   $before_org['value'][0]['_id']

    ${del_org}  delete organize  ${need_mod_org}
    should be true  $del_org=={}

    ${all_org2}   list organize

    should be equal  ${all_org1}  ${all_org2}

删除公司分部2-tc000092
   ${all_org1}   list organize

   ${del_org}  delete organize  0000


   ${all_org2}   list organize

   should be equal  ${all_org1}  ${all_org2}


