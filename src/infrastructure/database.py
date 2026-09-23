from typing import Annotated

from sqlalchemy import Integer, MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

from config import DATABASE_URL


engine = create_async_engine(
    DATABASE_URL,
)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
intpk = Annotated[int, mapped_column(Integer, primary_key=True)]


class Base(DeclarativeBase):
    type_annotation_map = {intpk: Integer}

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = [
            f"{col} = {getattr(self, col)}"
            for idx, col in enumerate(self.__table__.columns.keys())
            if col in self.repr_cols or idx < self.repr_cols_num
        ]
        return f"<{self.__class__.__name__} {', '.join(cols)}>"


def _import_all_models() -> None:
    import task.models


_import_all_models()
