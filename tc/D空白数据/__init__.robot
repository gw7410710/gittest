*** Settings ***
Library  pylib.common
Library  pylib.common.Contract_classify
Library  pylib.common.Contract

Suite Setup  Run Keywords  delete_All_organize  AND  delete_ALL_object  AND   delete_ALL_Contract_classify  AND  delete_ALL_contract

