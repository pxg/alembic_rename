"""Rename DB table to snickers

Revision ID: 2ab3b89ffc6
Revises: c17a94a547
Create Date: 2015-11-30 10:51:52.149330

"""

# revision identifiers, used by Alembic.
revision = '2ab3b89ffc6'
down_revision = 'c17a94a547'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    op.rename_table('marathon', 'snickers')
    op.execute('ALTER SEQUENCE marathon_id_seq RENAME TO snickers_id_seq')
    op.execute('ALTER INDEX marathon_pkey RENAME TO snickers_pkey')


def downgrade():
    op.rename_table('snickers', 'marathon')
    op.execute('ALTER SEQUENCE snickers_id_seq RENAME TO marathon_id_seq')
    op.execute('ALTER INDEX snickers_pkey RENAME TO marathon_pkey')
