from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING,
                       echo=True,
                       pool_size=8,
                       pool_recycle=60 * 30
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     service = SessionLocal()
#     try:
#         yield service
#     finally:
#         service.close()


