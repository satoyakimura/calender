from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bonus = Column(Integer)
    login = Column(DateTime, default=datetime.utcnow)
    logout = Column(DateTime, default=datetime.utcnow)

    # Scheduleとのリレーションシップを追加
    schedules = relationship("Schedule", back_populates="user")
    friends = relationship("Friend", back_populates="user")

class Schedule(Base):
    __tablename__ = "schedules"

    schedule_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    title = Column(String)
    content = Column(String)

    # Userとのリレーションシップを追加
    user = relationship("User", back_populates="schedules")

class Friend(Base):
    __tablename__ = "friends"

    friend_id = Column(Integer, primary_key=True, index=True)
    user_id_1 = Column(Integer, ForeignKey('users.user_id'))
    user_id_2 = Column(Integer, ForeignKey('users.user_id'))

    user1 = relationship("User", foreign_keys=[user_id_1])
    user2 = relationship("User", foreign_keys=[user_id_2])

    __table_args__ = (UniqueConstraint('user_id_1', 'user_id_2', name='_user_relation_uc'))

class Message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    receiver_id = Column(Integer, ForeignKey('users.user_id'))
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])


