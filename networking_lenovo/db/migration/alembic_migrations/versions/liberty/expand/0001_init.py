# Copyright (c) 2017, Lenovo. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Initial Liberty no-op expand script.

Revision ID: 0001
Revises: None
Create Date: 2015-10-28 17:38:34.209525

"""

from neutron.db.migration import cli


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
#down_revision = 'kilo'
branch_labels = (cli.EXPAND_BRANCH,)

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'lenovo_ml2_nosport_bindings',
        sa.Column('binding_id', sa.Integer(), nullable=False),
        sa.Column('port_id', sa.String(length=255), nullable=True),
        sa.Column('vlan_id', sa.Integer(), autoincrement=False,
                  nullable=False),
        sa.Column('switch_ip', sa.String(length=255), nullable=True),
        sa.Column('instance_id', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('binding_id'),
    )
