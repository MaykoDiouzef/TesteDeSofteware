from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Entidade
class Tribo(Base):
    __tablename__ = "tribo"

    id = Column(Integer, primary_key=True)
    nome = Column(String, default="Nome da tribo não informado")
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"[id:{self.id}, nome: {self.nome}, created: {self.created}]"


class TriboGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, nome):
        try:
            tribo = Tribo(nome=nome)
            self.session.add(tribo)
            self.session.commit()
            self.session.refresh(tribo)
            return tribo if tribo.id else False
        except SQLAlchemyError as error:
            print(f"Error criar tribo: {error}")
            self.session.rollback()
            return False
        

    def buscar(self, idTribo):
        try:
            tribo = self.session.query(Tribo).filter(Tribo.id==idTribo).first()
            return tribo if tribo else False
        except SQLAlchemyError as error:
            print(f"Error buscar tribo: {error}")
            return False


    def atualizar(self, idTribo, novoNome):
        try:
            resultado = self.session.query(Tribo).filter(Tribo.id==idTribo).update({"nome":novoNome}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar tribo: {error}")
            self.session.rollback()
            return False
        

    def deletar(self, idTribo):
        try:
            tribo = self.session.query(Tribo).filter(Tribo.id==idTribo).first()
            if tribo:
                self.session.delete(tribo)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar tribo: {error}")
            self.session.rollback()
            return False