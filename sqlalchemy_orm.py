from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declative import declarative_base

engine = create_engine("msql + mysqlconnector: // root:password@localhost:3306/household", echo=True)
# echo = True makes sqlalchemy print out sql statement that it executes

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema':'household'} # this will include the schema and the fact that it is in the household database

    project_id = Column(Integer, primary_key = True) # primary_key
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title='{}', description='{}'".format(self.title, self.description)

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'household'}

    task_id = Column(Integer, primary_key = True)
    project_id = Column(Integer, ForeignKey('household.projects.project_id')) # ForeignKey references db, tables in syntax
    description = Column(String(length = 50))

    project = relationship("Project") # we use name of the class and not the name of the table here
    # relationship are important. They complement foreign keys. They tell us they are building relationship with the 2 model rather than the database.

    def __repr__(self):
        return "<Task(title='{}', description='{}'".format(self.task_id, self.description)

Base.metadata.create_all(engine)

#create table


