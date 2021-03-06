"""empty message

Revision ID: 0635c6a5e230
Revises: None
Create Date: 2016-01-25 18:34:01.841154

"""

# revision identifiers, used by Alembic.
revision = '0635c6a5e230'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'blog_post', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog_post', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog_post', type_='foreignkey')
    op.drop_column(u'blog_post', 'author_id')
    op.drop_table('users')
    ### end Alembic commands ###
