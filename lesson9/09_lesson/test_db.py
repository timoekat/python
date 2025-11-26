from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:america@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Subject(Base):

    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)

    subject_title = Column(String)


def test_add_subject():
    session = Session()

    subject = Subject(subject_id=100, subject_title="Mathematics")

    session.add(subject)

    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "Mathematics"

    session.delete(saved)

    session.commit()

    session.close()


def test_edit_subject():

    session = Session()

    subject = Subject(subject_id=100, subject_title="Mathematics")

    session.add(subject)

    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "Mathematics"

    subject.subject_title = "Algebra"
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "Algebra"

    session.delete(saved)

    session.commit()

    session.close()


def test_delete_subject():

    session = Session()

    subject = Subject(subject_id=100, subject_title="Mathematics")

    session.add(subject)

    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()

    assert saved.subject_title == "Mathematics"

    session.delete(saved)

    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()

    assert saved is None

    session.close()
