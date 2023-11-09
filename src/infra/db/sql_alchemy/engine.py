from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://secret_user:secret_password@0.0.0.0/secret_db", echo=True
)
autocommit_engine = engine.execution_options(isolation_level="AUTOCOMMIT")

with autocommit_engine.begin() as connection:
    connection.commit()
    connection.begin()
