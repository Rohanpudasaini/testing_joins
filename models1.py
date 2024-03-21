from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.orm import registry
from sqlalchemy import ForeignKey, String, Select
from database_connection import engine


str_30 = Annotated[str,30]

registry_mapped = registry(
    type_annotation_map={
            str_30: String(30)
        }
)


# class Base(DeclarativeBase):
#     registry= registry(
#         type_annotation_map={
#             str_30: String(30)
#         }
#     )
    

# class Company(Base):
#     __tablename__="company"
#     id:Mapped[int] = mapped_column(primary_key=True)
#     name:Mapped[str_30]


@registry_mapped.mapped
class Company:
    __tablename__="company"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str_30]


@registry_mapped.mapped    
class Department:
    __tablename__="department"
    id:Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    name:Mapped[str_30]
    
@registry_mapped.mapped
class Employee:
    __tablename__ = 'employee'
    id:Mapped[int] = mapped_column(primary_key=True)
    department_id:Mapped[int] = mapped_column(ForeignKey("department.id"))
    name:Mapped[str_30]
    salary:Mapped[int]
    
@registry_mapped.mapped
class Employee2:
    __tablename__ = 'employee2'
    id:Mapped[int] = mapped_column(primary_key=True)
    department_id:Mapped[int]
    address:Mapped[str_30]
# Base.metadata.create_all(engine)

# base2 = registry_mapped.generate_base()
# base2.metadata.create_all(engine)