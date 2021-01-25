*** Settings ***
Library  pylib.common.Contract_classify


Suite Setup   add_Contract_classify  我是套件添加的合同分类     Contract_classify_ID

Suite Teardown  delete_Contract_classify  ${Contract_classify_ID}