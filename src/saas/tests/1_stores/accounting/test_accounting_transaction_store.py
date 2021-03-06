import unittest

from pyramid import testing

import string
import random
import uuid

from saas.app.modules.accounting.models.account_types import AccountTypes


class TestTransactionStore(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

        from saas.app.core.services.connection import ConnectionManager
        from saas.app.core.stores.client import ClientStore
        from saas.app.modules.accounting.stores.accounts import AccountsStore
        from saas.app.modules.accounting.stores.groups import GroupStore
        from saas.app.modules.accounting.stores.transactions import TransactionStore

        self.mgr = ConnectionManager({
            'app.config': '../../etc'
        })
        self.clientStore = ClientStore(self.mgr, 'default')
        self.groupStore = GroupStore(self.mgr, 'default')
        self.accountsStore = AccountsStore(self.mgr, 'default', self.groupStore)
        self.transactionStore = TransactionStore(self.mgr, 'default')

        self.defaultClient = self.clientStore.getDefaultClient()
    
    def generate_random_str(self, length: int):
        allowed = string.ascii_lowercase + string.digits
        return ''.join(random.choice(allowed) for i in range(length))

    def test_transaction_add(self):
        client_id = self.defaultClient[0]
        transaction_id = str(uuid.uuid4())
        currency_id = self.defaultClient[5]
        description = self.generate_random_str(10)

        account_id_1 = str(uuid.uuid4())
        account_id_2 = str(uuid.uuid4())

        account_name_1 = self.generate_random_str(10)
        account_name_2 = self.generate_random_str(10)

        self.accountsStore.add(client_id, account_id_1, AccountTypes.ASSETS, account_name_1, account_name_1)
        self.accountsStore.add(client_id, account_id_2, AccountTypes.ASSETS, account_name_2, account_name_2)

        transaction = {
            'clientId': client_id,
            'transactionId': transaction_id,
            'description': description,
            'currencyId': currency_id,
            'entries': [
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_1,
                    'debit': 100,
                    'credit': 0
                },
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_2,
                    'debit': 0,
                    'credit': 100
                }
            ],
            'attachments': [
                {
                    'id': str(uuid.uuid4()),
                    'filename': f'{account_name_1}.pdf',
                    'type': 'document/pdf',
                    'size': '100',
                    'data': '1234567890'
                }
            ]
        }

        try:
            self.transactionStore.add(transaction)
        except Exception as e:
            self.fail(e)

    def test_transaction_update(self):
        client_id = self.defaultClient[0]
        transaction_id = str(uuid.uuid4())
        currency_id = self.defaultClient[5]
        description = self.generate_random_str(10)

        account_id_1 = str(uuid.uuid4())
        account_id_2 = str(uuid.uuid4())

        account_name_1 = self.generate_random_str(10)
        account_name_2 = self.generate_random_str(10)

        self.accountsStore.add(client_id, account_id_1, AccountTypes.ASSETS, account_name_1, account_name_1)
        self.accountsStore.add(client_id, account_id_2, AccountTypes.ASSETS, account_name_2, account_name_2)

        transaction = {
            'clientId': client_id,
            'transactionId': transaction_id,
            'description': description,
            'currencyId': currency_id,
            'entries': [
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_1,
                    'debit': 100,
                    'credit': 0,
                    'status': 'update'
                },
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_2,
                    'debit': 0,
                    'credit': 100,
                    'status': 'update'
                }
            ],
            'attachments': [
                {
                    'id': str(uuid.uuid4()),
                    'filename': f'{account_name_1}.pdf',
                    'type': 'document/pdf',
                    'size': '100',
                    'data': '1234567890',
                    'status': 'update'
                }
            ]
        }


        self.transactionStore.add(transaction)
        transaction['description'] = self.generate_random_str(10)

        try:
            self.transactionStore.update(transaction)
        except Exception as e:
            self.fail(e)

    def test_transaction_get(self):
        client_id = self.defaultClient[0]
        transaction_id = str(uuid.uuid4())
        currency_id = self.defaultClient[5]
        description = self.generate_random_str(10)

        account_id_1 = str(uuid.uuid4())
        account_id_2 = str(uuid.uuid4())

        account_name_1 = self.generate_random_str(10)
        account_name_2 = self.generate_random_str(10)

        self.accountsStore.add(client_id, account_id_1, AccountTypes.ASSETS, account_name_1, account_name_1)
        self.accountsStore.add(client_id, account_id_2, AccountTypes.ASSETS, account_name_2, account_name_2)

        transaction = {
            'clientId': client_id,
            'transactionId': transaction_id,
            'description': description,
            'currencyId': currency_id,
            'entries': [
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_1,
                    'debit': 100,
                    'credit': 0,
                    'status': 'update'
                },
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_2,
                    'debit': 0,
                    'credit': 100,
                    'status': 'update'
                }
            ],
            'attachments': [
                {
                    'id': str(uuid.uuid4()),
                    'filename': f'{account_name_1}.pdf',
                    'type': 'document/pdf',
                    'size': '100',
                    'data': '1234567890',
                    'status': 'update'
                }
            ]
        }

        self.transactionStore.add(transaction)

        try:
            result = self.transactionStore.get(client_id, transaction_id)

            self.assertEqual(result['transactionId'], transaction_id, '{0}'.format(result))
        except Exception as e:
            self.fail(e)

    def test_transaction_filter(self):
        client_id = self.defaultClient[0]
        try:
            result = self.transactionStore.filter(client_id, '')
            self.assertGreater(len(result), 0, '{0}'.format(result))
        except Exception as e:
            self.fail(e)

    def test_transaction_post(self):
        client_id = self.defaultClient[0]
        transaction_id = str(uuid.uuid4())
        currency_id = self.defaultClient[5]
        description = self.generate_random_str(10)

        account_id_1 = str(uuid.uuid4())
        account_id_2 = str(uuid.uuid4())

        account_name_1 = self.generate_random_str(10)
        account_name_2 = self.generate_random_str(10)

        self.accountsStore.add(client_id, account_id_1, AccountTypes.ASSETS, account_name_1, account_name_1)
        self.accountsStore.add(client_id, account_id_2, AccountTypes.ASSETS, account_name_2, account_name_2)

        transaction = {
            'clientId': client_id,
            'transactionId': transaction_id,
            'description': description,
            'currencyId': currency_id,
            'entries': [
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_1,
                    'debit': 100,
                    'credit': 0,
                    'status': 'update'
                },
                {
                    'id': str(uuid.uuid4()),
                    'accountId': account_id_2,
                    'debit': 0,
                    'credit': 100,
                    'status': 'update'
                }
            ],
            'attachments': [
                {
                    'id': str(uuid.uuid4()),
                    'filename': f'{account_name_1}.pdf',
                    'type': 'document/pdf',
                    'size': '100',
                    'data': '1234567890',
                    'status': 'update'
                }
            ]
        }

        self.transactionStore.add(transaction)

        try:
            self.transactionStore.post(client_id, transaction_id)
        except Exception as e:
            self.fail(e)