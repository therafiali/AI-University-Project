from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy engine
# engine = create_engine('postgresql://rafialiofficial810:bU5rHGyJpj6M@ep-orange-night-18398430.ap-southeast-1.aws.neon.tech/neondb?sslmode=require', echo=True)
engine = create_engine('postgresql://postgres:rootadmin@localhost:5432/QuizApplication', echo=True)

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the SQLAlchemy session factory
Session = sessionmaker(bind=engine)