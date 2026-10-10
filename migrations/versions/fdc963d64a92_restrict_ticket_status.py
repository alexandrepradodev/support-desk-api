"""restrict ticket status

Revision ID: fdc963d64a92
Revises: 8cfb80de78b6
Create Date: 2026-10-10 14:21:03.033307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdc963d64a92'
down_revision: Union[str, Sequence[str], None] = '8cfb80de78b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "ck_tickets_status",
        "tickets",
        "status IN ('open', 'in_progress', 'closed')",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "ck_tickets_status",
        "tickets",
        type_="check"
    )
   
