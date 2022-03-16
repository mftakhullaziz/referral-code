import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a3041816ecaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False)
    )

    op.create_table(
        'referral_code',
        sa.Column('code', sa.String, primary_key=True),
        sa.Column('customer', sa.Integer, sa.ForeignKey('customer.id')),
        sa.Column('will_credit_in', sa.Integer, nullable=False)
    )

    op.create_table(
        'account',
        sa.Column('number', sa.String, primary_key=True),
        sa.Column('customer', sa.Integer, sa.ForeignKey('customer.id'))
    )

    op.create_table(
        'statement',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('account', sa.String, sa.ForeignKey('account.number')),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('status', sa.String, nullable=True),
        sa.Column('date', sa.DateTime),
    )

def downgrade():
    op.drop_table('referral_code')
    op.drop_table('statement')
    op.drop_table('account')
    op.drop_table('customer')
