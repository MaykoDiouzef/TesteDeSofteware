from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.exc import SQLAlchemyError
from entidades.tribo import Base

# Entidades
class Especie(Base):
    __tablename__ = "especie"

    id = Column(Integer, primary_key=True)
    nome = Column(String, default="Tipo de especie não informado")
    status = Column(Integer, default=0)
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"[id:{self.id}, nome:{self.nome}, status:{self.status}, created:{self.created}]"
    

class EspecieGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, nome, status):
        try:
            especie = Especie(nome=nome, status=status)
            self.session.add(especie)
            self.session.commit()
            self.session.refresh(especie)
            return especie if especie.id else False
        except SQLAlchemyError as error:
            print(f"Error criar especie: {error}")
            self.session.rollback()
            return False


    def buscar(self, id):
        try:
            especie = self.session.query(Especie).filter(Especie.id==id, Especie.status==1).first()
            return especie if especie else False
        except SQLAlchemyError as error:
            print(f"Error buscar especie: {error}")
            return False


    def atualizar(self, id, nome):
        try:
            resultado = self.session.query(Especie).filter(Especie.id==id).update({"nome":nome}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar especie: {error}")
            self.session.rollback()
            return False


    def deletar(self, id):
        try:
            especie = self.session.query(Especie).filter(Especie.id==id).first()
            if especie:
                self.session.delete(especie)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar especie: {error}")
            self.session.rollback()
            return False
        