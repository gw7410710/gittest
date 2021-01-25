# -*- coding: utf-8 -*-
import requests
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

url = 'http://devops.sqtest.online:6007'


# 管理员登陆
def admin_login(email,password):
    global space

    payload = {"user": {"email": email}, "password": password, "code": "", "locale": "zhcn"}
    re = requests.post(url=url + '/accounts/password/authenticate', json=payload)
    space = re.cookies['X-Space-Id']

    # pprint(re.cookies)
    return re.cookies
# admin_login('747370289@qq.com','111111')

# admin_login()
# 添加部门
def add_organize(name, save_id_Name=None):
    payload = {
        "name": name,
        "parent": "k3cR79DWPGDbYbS3q",
        "sort_no": 100,
        "hidden": False,
        "space": space
    }

    re = requests.post(url=url + '/api/v4/organizations', json=payload, cookies=admin_login('747370289@qq.com','111111'))
    body = re.json()

    pprint(body)

    if save_id_Name:
        BuiltIn().set_global_variable('${%s}' % save_id_Name, body['value'][0]['_id'])

    return body


# 列出部门
def list_organize():
    re = requests.get(url=url + '/api/v4/organizations', cookies=admin_login('747370289@qq.com','111111'))
    pprint(re.json())
    return re.json()


# list_organize()

# 删除部门
def delete_organize(organization_id):
    re = requests.delete(url=url + f'/api/v4/organizations/{organization_id}', cookies=admin_login('747370289@qq.com','111111'))
    # pprint(re.json())
    return re.json()


# delete_organize('v5kTNAj6Lc8aeQ5wG')


# 删除所有部门
def delete_All_organize():
    all_or = list_organize()['value'][1:]
    for i in all_or:
        delete_organize(i['_id'])


# 修改部门
def update_organize(name, organization_id):
    payload = {
        "$set": {
            "name": name,
            "parent": "k3cR79DWPGDbYbS3q",
            "sort_no": 100,
            "hidden": False,
            "space": space
        }
    }
    re = requests.put(url=url + f'/api/v4/organizations/{organization_id}', json=payload, cookies=admin_login('747370289@qq.com','111111'))
    pprint(re.json())
    return re.json()


def organize_should_contain(organize_list, _id, created, name):
    add_list = {'@odata.context': 'http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/$metadata#organizations',
                '@odata.count': 1,
                'value': [{
                    '@odata.editLink': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/organizations('%s')" % _id,
                    '@odata.etag': 'W/"08D589720BBB3DB1"',
                    '@odata.id': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/organizations('%s')" % _id,
                    '_id': str(_id),
                    'company_id': 'k3cR79DWPGDbYbS3q',
                    'created': created,
                    'created_by': '5fd7112fb428030012f26138',
                    'fullname': name,
                    'hidden': False,
                    'modified': created,
                    'modified_by': '5fd7112fb428030012f26138',
                    'name': name,
                    'owner': '5fd7112fb428030012f26138',
                    'parent': 'k3cR79DWPGDbYbS3q',
                    'parents': ['k3cR79DWPGDbYbS3q'],
                    'sort_no': 100,
                    'space': space, }]}
    pprint(add_list['value'][0])
    pprint('==========================================================')
    pprint(organize_list)

    if add_list['value'][0] not in organize_list:
        raise Exception('新增的公司部门不在所有部门列表中')
    else:
        print('新增的部门在所有部门列表中')


# -------------------------------------签约对象---------------------------------------------------------------

def add_object(name, object_id=None):
    payload = {
        "name": name,
        "category": 1,
        "company_ids": ["k3cR79DWPGDbYbS3q"],
        "status": 1,
        "space": space
    }

    re = requests.post(f'{url}/api/v4/accounts', json=payload, cookies=admin_login('747370289@qq.com','111111'))
    body = re.json()
    pprint(body)

    if object_id:
        BuiltIn().set_global_variable('${%s}' % object_id, body['value'][0]['_id'])

    return body


# for i in range(1,50):
# add_object('我是签约对象222')


def update_object(name, account_id):
    payload = {
        "$set": {
            "name": name,
            "category": "1",
            "company_ids": ["k3cR79DWPGDbYbS3q"],
            "status": "2",
            "space": space
        }
    }
    re = requests.put(f'{url}/api/v4/accounts/{account_id}', json=payload, cookies=admin_login('747370289@qq.com','111111'))

    pprint(re.json())
    return re.json()


# update_object('开发部门','1999999999','南京市鼓楼区敏梅保险','GyPR98N5x2JroRSbt')


def list_object():
    re = requests.get(
        f'{url}/api/v4/accounts?%24top=50&%24select=name%2Cphone%2Caddress%2Cregistered_capital%2Ccategory%2Ccredit_code%2Cowner%2Ccompany_id%2Ccompany_ids%2Clocked&%24count=true',cookies=admin_login('747370289@qq.com','111111'))
    pprint(re.json())
    return re.json()


# list_object()

def delete_object(account_id):
    re = requests.delete(f'{url}/api/v4/accounts/{account_id}',cookies=admin_login('747370289@qq.com','111111'))
    pprint(re.json())

    return re.json()


# delete_object('RNmf67qLYXDzWEcjj')


def delete_ALL_object():
    objects = list_object()['value']

    for i in objects:
        delete_object(i['_id'])


# delete_ALL_object()


def add_object_should_contain(list_object, _id, name):
    value = {'@odata.editLink': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/accounts('%s')" % _id,
             '@odata.etag': 'W/"08D589720BBB3DB1"',
             '@odata.id': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/accounts('%s')" % _id,
             '_id': _id,
             'category': '1',
             'company_id': 'k3cR79DWPGDbYbS3q',
             'company_ids': ['k3cR79DWPGDbYbS3q'],
             'name': name,
             'owner': '5fd7112fb428030012f26138'}

    pprint(value)
    pprint('------------------------------------------------------')
    pprint(list_object)

    if value not in list_object:
        raise Exception('新添加的签约对象不在列表中')
# admin_login()
# add_object('对象')
# list_object()


# --------------------------合同分类-----------------------------------------------------------

class Contract_classify:

    def add_Contract_classify(self, name, Contract_classify_ID=None):
        payload = {'name': name,
                   'code': "2020-001",
                   'space': "PZnFm79o6ezgmKDMt"
                   }

        re = requests.post(f'{url}/api/v4/contract_types', json=payload, cookies=admin_login('747370289@qq.com','111111'))
        body = re.json()
        pprint(body)

        if Contract_classify_ID:
            BuiltIn().set_global_variable('${%s}' % Contract_classify_ID, body['value'][0]['_id'])

        return body

    def list_Contract_classify(self):
        re = requests.get(
            f'{url}/api/v4/contract_types?%24top=50&%24select=name%2Cowner%2Ccompany_id%2Ccompany_ids%2Clocked&%24count=true',cookies=admin_login('747370289@qq.com','111111'))
        pprint(re.json())

        return re.json()

    def update_Contract_classify(self, name, contract_id):
        payload = {
            '$set':
                {
                    'name': name,
                    'code': "2020-001",
                    'space': space
                }
        }

        re = requests.put(f'{url}/api/v4/contract_types/{contract_id}', json=payload, cookies=admin_login('747370289@qq.com','111111'))

        pprint(re.json())
        return re.json()

    def delete_Contract_classify(self, contract_id):
        re = requests.delete(f'{url}/api/v4/contract_types/{contract_id}', cookies=admin_login('747370289@qq.com','111111'))
        pprint(re.json())
        return re.json()

    def delete_ALL_Contract_classify(self):
        ALL = Contract_classify().list_Contract_classify()['value']
        for i in ALL:
            Contract_classify().delete_Contract_classify(i['_id'])

    def Contract_classify_should_contain(self, Contract_classify_list, _id, name):

        list = {'@odata.editLink': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contract_types('%s')" % _id,
                '@odata.etag': 'W/"08D589720BBB3DB1"',
                '@odata.id': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contract_types('%s')" % _id,
                '_id': _id,
                'company_id': 'k3cR79DWPGDbYbS3q',
                'company_ids': ['k3cR79DWPGDbYbS3q'],
                'name': name,
                'owner': '5fd7112fb428030012f26138'}

        pprint(list)
        pprint('----------------------------------------------------------')
        pprint(Contract_classify_list)

        if list not in Contract_classify_list:
            raise Exception('新增的分类不在列表中')


# Contract_classify().Contract_classify_should_contain(Contract_classify().list_Contract_classify(),'inY5puWX9933qZSQc','分类')
# Contract_classify().list_Contract_classify()
# Contract_classify().add_Contract_classify('分类')

# Contract_classify().delete_ALL_Contract_classify()
# Contract_classify().add_Contract_classify('我是合同分类13')
# Contract_classify().list_Contract_classify()


# Contract_classify().update_Contract_classify('我是修改之后的合同分类','kPAKTKQuHFWhCZfz5')
# Contract_classify().delete_Contract_classify('B2yfE7RmQyctvwRSo')


# -------------------------------合同-------------------------------------------------------
class Contract:

    def add_contract(self, no, othercompany, contract_type, name, contract_id=None):
        payload = {
            "no": no,
            "create_date": "2020-07-07T07:31:06.754Z",
            # 签约对象ID othercompany
            "othercompany": othercompany,
            "project": "jgrJCeMttzD8pHZhy",
            # 合同类型ID contract_type
            "contract_type": contract_type,
            "name": name,
            "bop": "付款合同",
            "applicant": "5efae24570ff1b0012038be1",
            "virtual_contract": "合同",
            "paid_amount": 0,
            "unpaid_amount": 0,
            "receipted_amount": 0,
            "unclaimed_votes_amount": 0,
            "received_amount": 0,
            "unreceived_amount": 0,
            "for_invoicing_amount": 0,
            "unfor_invoicing_amount": 0,
            "space": space
        }

        re = requests.post(f'{url}/api/v4/contracts', json=payload, cookies=admin_login('747370289@qq.com','111111'))
        body = re.json()

        pprint(body)

        if contract_id:
            BuiltIn().set_global_variable('${%s}' % contract_id, body['value'][0]['_id'])

        return body

    def update_contract(self, contracts_id, no, name):
        payload = {"$set": {"no": no, 'name': name}}
        re = requests.put(f'{url}/api/v4/contracts/{contracts_id}', json=payload, cookies=admin_login('747370289@qq.com','111111'))

        pprint(re.json())
        return re.json()

    def list_contract(self):
        re = requests.get(f'{url}/api/v4/contracts', cookies=admin_login('747370289@qq.com','111111'))

        pprint(re.json())
        return re.json()

    def delete_contract(self, contracts_id):
        re = requests.delete(f'{url}/api/v4/contracts/{contracts_id}', cookies=admin_login('747370289@qq.com','111111'))

        pprint(re.json())
        return re.json()

    def delete_ALL_contract(self):
        all_contract = Contract().list_contract()['value']
        for i in all_contract:
            Contract().delete_contract(i['_id'])

    # 添加的合同是否在合同列表中
    def contract_should_contain(self, info_list, _id, contract_type, created, name, no, othercompany, serial_number):
        add_list = {
            '@odata.editLink': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contracts('%s')" % _id,
            '@odata.etag': 'W/"08D589720BBB3DB1"',
            '@odata.id': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contracts('%s')" % _id,
            '_id': _id,
            'amount_type': '固定',
            'applicant': '5efae24570ff1b0012038be1',
            'bop': '付款合同',
            'company_id': 'k3cR79DWPGDbYbS3q',
            'company_ids': ['k3cR79DWPGDbYbS3q'],
            'contract_type': contract_type,
            'create_date': '2020-07-07T07:31:06.754Z',
            'created': created,
            'created_by': '5fd7112fb428030012f26138',
            'for_invoicing_amount': 0,
            'modified': created,
            'modified_by': '5fd7112fb428030012f26138',
            'name': name,
            'no': no,
            'othercompany': othercompany,
            'owner': '5fd7112fb428030012f26138',
            'paid_amount': 0,
            'project': 'jgrJCeMttzD8pHZhy',
            'receipted_amount': 0,
            'receive_payment_type': '一次性',
            'received_amount': 0,
            'serial_number': serial_number,
            'space': space,
            'unclaimed_votes_amount': 0,
            'unfor_invoicing_amount': 0,
            'unpaid_amount': 0,
            'unreceived_amount': 0,
            'virtual_contract': '合同'}

        pprint(add_list)
        pprint('---------------------------------------------------------')
        pprint(info_list)

        if add_list not in info_list:
            raise Exception('添加的合同信息不在列表中')

    # 添加的合同是否在合同列表中（修改之后）
    def contract_should_contain222(self, info_list, _id, contract_type, created, modified, name, no, othercompany,
                                   serial_number):
        add_list = {
            '@odata.editLink': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contracts('%s')" % _id,
            '@odata.etag': 'W/"08D589720BBB3DB1"',
            '@odata.id': "http://127.0.0.1:5040/api/odata/v4/PZnFm79o6ezgmKDMt/contracts('%s')" % _id,
            '_id': _id,
            'amount_type': '固定',
            'applicant': '5efae24570ff1b0012038be1',
            'bop': '付款合同',
            'company_id': 'k3cR79DWPGDbYbS3q',
            'company_ids': ['k3cR79DWPGDbYbS3q'],
            'contract_type': contract_type,
            'create_date': '2020-07-07T07:31:06.754Z',
            'created': created,
            'created_by': '5fd7112fb428030012f26138',
            'for_invoicing_amount': 0,
            'modified': modified,
            'modified_by': '5fd7112fb428030012f26138',
            'name': name,
            'no': no,
            'othercompany': othercompany,
            'owner': '5fd7112fb428030012f26138',
            'paid_amount': 0,
            'project': 'jgrJCeMttzD8pHZhy',
            'receipted_amount': 0,
            'receive_payment_type': '一次性',
            'received_amount': 0,
            'serial_number': serial_number,
            'space': space,
            'unclaimed_votes_amount': 0,
            'unfor_invoicing_amount': 0,
            'unpaid_amount': 0,
            'unreceived_amount': 0,
            'virtual_contract': '合同'}

        pprint(add_list)
        pprint('---------------------------------------------------------')
        pprint(info_list)

        if add_list not in info_list:
            raise Exception('添加的合同信息不在列表中')

# Contract().delete_contract('KaHHXGzmT5dH72z9e')

# Contract().list_contract()
# Contract().update_contract('Gufrt6ACLXmWSuNu8','1','我是修改之后的合同')

# Contract().add_contract('2','gzmd5YrrPGFEdsA87','9FFwDAGWDyoz65WLf','奔驰C260L购车合同')

# add_object('死一样的痛过')
# Contract_classify().add_Contract_classify('合同分类')


# Contract().delete_ALL_contract()

# list_object()
