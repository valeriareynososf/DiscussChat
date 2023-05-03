from .db import db, environment, SCHEMA, add_prefix_for_prod

class Channel_Message(db.Model):
    __tablename__ = 'channel_messages'
    if environment == "production":
        __table_args__ = ({'schema': SCHEMA})

    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("channels.id")), nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False, unique=False)
    message = db.Column(db.String(2000), nullable=False, unique=False)
    date = db.Column(db.Date, nullable=False, unique=False)

    channels = db.relationship("Channel", back_populates="messages")
    user = db.relationship("User", back_populates="messages")

    def to_dict(self):
        return {
            'id': self.id,
            'channel_id': self.channel_id,
            'user_id': self.user_id,
            'message': self.message,
            'date': self.date,
            'user': self.user.to_dict()
        }
