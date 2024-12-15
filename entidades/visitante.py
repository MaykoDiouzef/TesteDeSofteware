from datetime import datetime
from sqlalchemy import Column, String, Integer, BigInteger, TIMESTAMP
from sqlalchemy.exc import SQLAlchemyError
from conftest import Base

# Entidade
class Visitante(Base):
    __tablename__ = "visitante"

    id = Column(Integer, primary_key=True)
    idDiscord = Column(BigInteger)
    nome = Column(String)
    nomeGlobal = Column(String)
    language = Column(String)
    created = Column(TIMESTAMP, default=datetime.now()) #timezone.utc

    def __repr__(self):
        return f"[id:{self.id}, idDiscord:{self.idDiscord}, nome:{self.nome}, nomeGlobal:{self.nomeGlobal}, language:{self.language}, created:{self.created}]"


class VisitanteGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, idDiscord, nome, nomeGlobal, language):
        try:
            visitante = Visitante(idDiscord=idDiscord, nome=nome, nomeGlobal=nomeGlobal, language=language)
            self.session.add(visitante)
            self.session.commit()
            self.session.refresh(visitante)
            return visitante if visitante.id else False
        except SQLAlchemyError as error:
            print(f"Error criar visitante: {error}")
            self.session.rollback()
            return False


    def buscar(self, idDiscord):
        try:
            visitante = self.session.query(Visitante).filter(Visitante.idDiscord==idDiscord).first()
            return visitante if visitante else False
        except SQLAlchemyError as error:
            print(f"Error buscar visitante: {error}")
            return False


    def atualizar(self, idDiscord, nome, nomeGlobal):
        try:
            resultado = self.session.query(Visitante).filter(Visitante.idDiscord==idDiscord).update({"nome":nome, "nomeGlobal":nomeGlobal}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar visitante: {error}")
            self.session.rollback()
            return False


    def deletar(self, idDiscord):
        try:
            visitante = self.session.query(Visitante).filter(Visitante.idDiscord==idDiscord).first()
            if visitante:
                self.session.delete(visitante)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar visitante: {error}")
            self.session.rollback()
            return False