import enum


class RoleType(enum.Enum):
    regular = 'regular'
    admin = 'admin'


class Status(enum.Enum):
    pending = 'pending'
    completed = 'completed'
