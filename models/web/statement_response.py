from database.entities import account
from marshmallow import Schema, fields


class StatementSchema(Schema):
    amount = fields.Float(required=True)
    description = fields.String()
    status = fields.String()
    account = fields.String()
    name = fields.String()
    date = fields.DateTime(required=True)
