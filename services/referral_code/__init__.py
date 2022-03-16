import flask
from sqlalchemy.exc import NoResultFound

from database import db_transaction
from database.entities.account import Account
from database.entities.customer import Customer
from database.entities.referral_code import ReferralCode
from logger import logger
from models.web.error_response import ErrorResponse
from models.web.share_referral_code_response import ShareReferralCodeSchema


class ReferralCodeService:
    def share(self, accnum):
        try:
            with db_transaction() as txn:
                rc = txn.query(ReferralCode).join(Customer).join(Account) \
                    .filter(ReferralCode.customer == Customer.id) \
                    .filter(Customer.id == Account.customer) \
                    .filter(Account.number == accnum) \
                    .one()

                return flask.jsonify(ShareReferralCodeSchema().dump({
                    'code': rc.code,
                    'link': f'{flask.request.host_url}signup?code={rc.code}'
                }))
        except NoResultFound as err:
            logger.error(
                f'failed to share referral code because no referral code was found which relates to the account number {accnum}; details: {err.__str__()}')
            return ErrorResponse('referral code not found').json()
        except Exception as err:
            raise err
