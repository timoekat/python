from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from db_config import Session

Base = declarative_base()


TEST_SUBJECT_ID = 100
TEST_SUBJECT_TITLE = "Mathematics"
UPDATED_SUBJECT_TITLE = "Algebra"


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)


def get_subject_by_id(session, subject_id):
    return (
        session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )


def test_add_subject():
    session = Session()

    subject = Subject(
        subject_id=TEST_SUBJECT_ID,
        subject_title=TEST_SUBJECT_TITLE
    )
    session.add(subject)
    session.commit()

    saved = get_subject_by_id(session, TEST_SUBJECT_ID)
    assert saved.subject_title == TEST_SUBJECT_TITLE

    session.delete(saved)
    session.commit()
    session.close()


def test_edit_subject():
    session = Session()

    subject = Subject(
        subject_id=TEST_SUBJECT_ID,
        subject_title=TEST_SUBJECT_TITLE
    )
    session.add(subject)
    session.commit()

    saved = get_subject_by_id(session, TEST_SUBJECT_ID)
    assert saved.subject_title == TEST_SUBJECT_TITLE

    saved.subject_title = UPDATED_SUBJECT_TITLE
    session.commit()

    saved = get_subject_by_id(session, TEST_SUBJECT_ID)
    assert saved.subject_title == UPDATED_SUBJECT_TITLE

    session.delete(saved)
    session.commit()
    session.close()


def test_delete_subject():
    session = Session()

    subject = Subject(
        subject_id=TEST_SUBJECT_ID,
        subject_title=TEST_SUBJECT_TITLE
    )
    session.add(subject)
    session.commit()

    saved = get_subject_by_id(session, TEST_SUBJECT_ID)
    assert saved.subject_title == TEST_SUBJECT_TITLE

    session.delete(saved)
    session.commit()

    saved = get_subject_by_id(session, TEST_SUBJECT_ID)
    assert saved is None

    session.close()
