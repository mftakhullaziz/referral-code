import os

import jwt
from flask import jsonify
from sqlalchemy.exc import NoResultFound

from database import db_transaction
from database.entities.account import Account
from database.entities.customer import Customer
from logger import logger
from models.web.error_response import ErrorResponse
from security import Claims, ClaimsSchema
from security.password import PasswordUtils


class LoginService:

    def login(self, email, password):
        try:
            with db_transaction() as txn:
                customer = txn.query(Customer).filter(Customer.email == email).one()

                if password != PasswordUtils().decrypt(customer.password):
                    logger.error(f'wrong password for the user email {email}')
                    return ErrorResponse('Unauthorized', error_code=401).json()

                account = txn.query(Account).filter(Account.customer == customer.id).one()
                print(account)
                claims = Claims.new(customer.name, account.number)
                token = jwt.encode(
                    ClaimsSchema().dump(claims),
                    os.environ.get('JWT_SIGNING_KEY')
                ).decode()
                # encrypt
                password = PasswordUtils().encrypt(password)

                return jsonify(id=customer.id, email=email, password=password, token=token)
        except NoResultFound as err:
            logger.error(f'failed to login because the user email {email} could not be found in the database; details: {err.__str__()}')
            return ErrorResponse('Unauthorized', error_code=401).json()
        except Exception as err:
            raise err
