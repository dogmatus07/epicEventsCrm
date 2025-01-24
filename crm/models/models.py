import uuid
from sqlalchemy import (
create_engine,
Column,
Integer,
String,
DateTime,
Boolean,
ForeignKey,
Float,
Date
)
from passlib.hash import bcrypt
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    """
    User model
    """
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True, default=lambda : str(uuid.uuid4()))
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_number = Column(String(255), unique=True, nullable=True)
    is_active = Column(Boolean, default=True)
    role_name = Column(String, ForeignKey('roles.role_name'), index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    role = relationship('Role', back_populates='users')
    clients = relationship('Client', back_populates='commercial')
    contracts = relationship('Contract', back_populates='commercial')
    events = relationship('Event', back_populates='support_contact')

    def set_password(self, password):
        """
        Set password for the user
        :param password:
        :return: hashed password
        """
        self.hashed_password = bcrypt.hash(password)

    def verify_password(self, password):
        """
        Verify the password
        :param password:
        :return: boolean
        """
        return bcrypt.verify(password, self.hashed_password)


class Role(Base):
    """
    Role model
    """
    __tablename__ = 'roles'

    role_name = Column(String, primary_key=True)

    users = relationship('User', back_populates='role')


class Client(Base):
    """
    Client model
    """
    __tablename__ = 'clients'

    id = Column(TEXT, primary_key=True, default=lambda : str(uuid.uuid4()))
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(50), nullable=True, index=True)
    company_name = Column(String(255), nullable=False, index=True)
    first_contact_date = Column(Date, nullable=False)
    last_update_date = Column(Date, nullable=False)

    commercial_id = Column(TEXT, ForeignKey('users.id'), index=True)
    commercial = relationship('User', back_populates='clients')
    contracts = relationship('Contract', back_populates='client')


class Contract(Base):
    """
    Contract model
    """
    __tablename__ = 'contracts'
    id = Column(TEXT, primary_key=True, default=lambda : str(uuid.uuid4()))
    client_id = Column(TEXT, ForeignKey('clients.id'), index=True)
    total_amount = Column(Float, nullable=False)
    amount_due = Column(Float, nullable=False)
    signed = Column(Boolean, default=False)

    commercial_id = Column(TEXT, ForeignKey('users.id'),index=True)
    commercial = relationship('User', back_populates='contracts')
    client = relationship('Client', back_populates='contracts')
    events = relationship('Event', back_populates='contract')


class Event(Base):
    """
    Event model
    """
    __tablename__ = 'events'
    id = Column(TEXT, primary_key=True, default=lambda : str(uuid.uuid4()))
    contract_id = Column(String, ForeignKey('contracts.id'), index=True)
    event_date_start = Column(Date, nullable=False, index=True)
    event_date_end = Column(Date, nullable=False, index=True)
    location = Column(String(255), nullable=False)
    attendees = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)

    support_id = Column(String, ForeignKey('users.id'), index=True)
    support_contact = relationship('User', back_populates='events')
    contract = relationship('Contract', back_populates='events')
