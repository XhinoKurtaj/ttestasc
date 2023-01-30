import sqlalchemy

metadata = sqlalchemy.MetaData()

posts = sqlalchemy.Table(
    'time_log',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('date', sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column('start_time', sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column('end_time', sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.Text(), nullable=False),
    sqlalchemy.Column('project', sqlalchemy.Text(), nullable=False),
    sqlalchemy.Column('tags', sqlalchemy.Text(), nullable=False),
)

