from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:america@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
