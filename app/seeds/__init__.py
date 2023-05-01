from flask.cli import AppGroup
from .users import seed_users, undo_users
from .servers import seed_servers, undo_servers
from .channels import seed_channels, undo_channels
from .server_members import seed_members, undo_Server_Member
from .channel_messages import seed_messages, undo_channel_message
from app.models.db import db, environment, SCHEMA
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
# @seed_commands.command('all')
# def seed():
#     seed_users()
#     seed_servers()
#     seed_channels()
#     seed_members()
#     seed_messages()
#     # Add other seed functions here

@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(f"TRUNCATE table {SCHEMA}.channel_messages RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.server_members RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.servers RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.channels RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add a truncate command here for every table that will be seeded.
        db.session.commit()
        # undo_channel_message()
        # undo_Server_Member()
        # undo_servers()
        # undo_users()
        # undo_channels()
    seed_users()
    seed_servers()
    seed_channels()
    seed_members()
    seed_messages()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_channel_messages()
    undo_Server_Members()
    undo_servers()
    undo_channels()
    undo_users()
    # Add other undo functions here
