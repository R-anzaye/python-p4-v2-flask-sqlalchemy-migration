"""rename department

Revision ID: 52448ab592ef
Revises: 38b2462e45d6
Create Date: 2024-06-27 19:13:18.225706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52448ab592ef'
down_revision = '38b2462e45d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###