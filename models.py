from sqlalchemy import Column,Integer,String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class TaskItem(Base):
    __tablename__ = "task_items"

    task_item_id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)
    assigned_to = Column(String)
    start_date = Column(String)
    due_date = Column(String)
    status = Column(String)


class TaskStage(Base):
    __tablename__ = "task_stages"

    stage_id = Column(Integer, primary_key=True)
    task_item_id = Column(Integer)
    stage_name = Column(String)
    stage_status = Column(String)
    last_updated_date = Column(String)
    status = Column(String)