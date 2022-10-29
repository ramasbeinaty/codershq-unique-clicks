"""create models

Revision ID: 9653fa43a537
Revises: 
Create Date: 2022-10-26 12:09:21.088742

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9653fa43a537'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ambassadors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=False, server_default=sa.schema.DefaultClause("0")),
    sa.Column('is_valid', sa.Boolean(), nullable=False, server_default=sa.schema.DefaultClause("1")),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_ambassadors_id'), 'ambassadors', ['id'], unique=False)
    op.create_index(op.f('ix_ambassadors_link'), 'ambassadors', ['link'], unique=True)
    op.create_table('visitors',
    sa.Column('ip_address', postgresql.INET(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('datetime_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('ip_address', 'url'),
    )
    op.create_index(op.f('ix_visitors_ip_address'), 'visitors', ['ip_address'], unique=False)
    op.create_index(op.f('ix_visitors_url'), 'visitors', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_visitors_url'), table_name='visitors')
    op.drop_index(op.f('ix_visitors_ip_address'), table_name='visitors')
    op.drop_table('visitors')
    op.drop_index(op.f('ix_ambassadors_link'), table_name='ambassadors')
    op.drop_index(op.f('ix_ambassadors_id'), table_name='ambassadors')
    op.drop_table('ambassadors')
    # ### end Alembic commands ###
