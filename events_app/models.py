"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

class EventType(enum.Enum):
    """Event type enum"""
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    CONFERENCE = 4

class Guest(db.Model):
    """Guest Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests_attending')

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

class Event(db.Model):
    """Event Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.Enum(EventType))
    guests_attending = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'

guest_event_table = db.Table('guest_event_table',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)
