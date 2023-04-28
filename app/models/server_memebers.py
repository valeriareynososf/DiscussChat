from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import UniqueConstraint

class Server_Member(db.Model):
    __tablename__ = 'server_members'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("servers.id")), nullable=False)
    user = db.relationship("User", back_populates="server_members")
    server = db.relationship("Server", back_populates="server_members_2")
    __table_args__ = (UniqueConstraint('user_id', 'server_id', name='server_join'),
                    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'server_id': self.server_id
        }
