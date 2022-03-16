from locale import currency
import random
import string

from sqlalchemy.exc import IntegrityError, NoResultFound

from database import db_transaction
from database.entities.account import Account
from database.entities.customer import Customer
from database.entities.referral_code import ReferralCode
from database.entities.statement import Statement
from logger import logger
from models.web.error_response import ErrorResponse
from security.password import PasswordUtils
from flask import jsonify


class CustomerService:

    def signup(self, *args):
        name, email, password, referral_code = args
        password = PasswordUtils().encrypt(password)

        try:
            with db_transaction() as txn:
                customer = Customer(
                    name=name,
                    email=email,
                    password=password)
                txn.add(customer)
                txn.flush()

                accnum = self._create_account(txn, customer.id)
                names = customer.name
                self._create_referral_code(txn, customer.id)

                if referral_code:
                    rc = txn.query(ReferralCode).filter(ReferralCode.code == referral_code).one()
                    if rc.will_credit_in <= 1:
                        account = txn.query(Account).filter(Account.customer == rc.customer).one()
                        txn.add(Statement(
                            description='Credit due to referral code',
                            status='Contributor',
                            account=account.number,
                            name=names
                        ))
                        rc.will_credit_in = 5
                    else:
                        rc.will_credit_in -= 1

                    txn.flush()

                    txn.add(Statement(
                        # amount=10,
                        description='User signup using a referral code',
                        status='Contributor',
                        account=accnum,
                        name=names
                    ))
                    txn.flush()

                return jsonify(name=name,email=email,password=password, id=customer.id), 201
        except IntegrityError as err:
            err.hide_parameters = True 
            logger.error(f'failed to create a new user due to an IntegrityError: {err.__str__()}')
            return ErrorResponse('email must be unique', error_code=409).json()
        except NoResultFound as err:
            logger.error(f'failed to create a new user due to an NoResultsFound exception: {err.__str__()}')
            return ErrorResponse('referral code not found', error_code=422).json()

    def _create_account(self, txn, customer_id):
        while True:
            accnum = self._random_account_number()
            if not txn.query(Account).filter(Account.number == accnum).one_or_none():
                break

        txn.add(Account(
            number=accnum,
            customer=customer_id
        ))
        txn.flush()
        return accnum

    def _create_referral_code(self, txn, customer_id):
        while True:
            code = self._random_referral_code()
            if not txn.query(ReferralCode).filter(ReferralCode.code == code).one_or_none():
                break

        txn.add(ReferralCode(
            code=code,
            customer=customer_id
        ))
        txn.flush()
        return code

    def _random_account_number(self):
        return ''.join([str(random.randrange(0, 9, 1)) for _ in range(10)])

    def _random_referral_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
