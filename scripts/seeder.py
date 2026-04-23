import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

from app.schemas.user import User

fake = Faker()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST', 'localhost')}:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def seed_users():
    db = SessionLocal()

    try:
        if db.query(User).count() > 0:
            print("Seed ignorado: tabela já possui dados.")
            return

        users = [
            User(
                name=fake.name(),
                email=fake.unique.email()
            )
            for _ in range(50)
        ]

        db.add_all(users)
        db.commit()

        print("Seed executado com sucesso. 50 usuários inseridos.")

    except Exception as e:
        db.rollback()
        print(f"Erro no seed: {e}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()