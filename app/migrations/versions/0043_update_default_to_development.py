"""update default to development

Revision ID: 0043
Revises: 0042
Create Date: 2025-06-25 14:55:53.160125

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0043"
down_revision: str | None = "0042"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("environments", schema=None) as batch_op:
        batch_op.add_column(sa.Column("is_development", sa.Boolean(), nullable=True))
        batch_op.drop_index(
            "ux_default_environment", postgresql_where="(is_default = true)"
        )
        batch_op.drop_column("is_default")

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("environments", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("is_default", sa.BOOLEAN(), autoincrement=False, nullable=False)
        )
        batch_op.create_index(
            "ux_default_environment",
            ["organization_uuid"],
            unique=True,
            postgresql_where="(is_default = true)",
        )
        batch_op.drop_column("is_development")

    # ### end Alembic commands ###
