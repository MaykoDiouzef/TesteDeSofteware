from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from entidades.tribo import Base

# Entidade
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    idTribo = Column(Integer, ForeignKey("tribo.id"))
    idDiscord = Column(BigInteger)
    nome = Column(String)
    nomeGlobal = Column(String)
    cargo = Column(String)
    status = Column(String)
    language = Column(String)
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    tribo = relationship("Tribo", lazy="subquery")

    def __repr__(self):
        return f"[id:{self.id}, tribo:{self.tribo}, idTribo:{self.idTribo}, idDiscord:{self.idDiscord}, nome:{self.nome}, nomeGlobal:{self.nomeGlobal}, cargo:{self.cargo}, status:{self.status}, language:{self.language}, created:{self.created}]"
    

class UsuarioGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, idTribo, idDiscord, nome, nomeGlobal, cargo, status, language):
        try:
            usuario = Usuario(idTribo=idTribo, idDiscord=idDiscord, nome=nome, nomeGlobal=nomeGlobal, cargo=cargo, status=status, language=language)
            self.session.add(usuario)
            self.session.commit()
            self.session.refresh(usuario)
            return usuario if usuario.id else False
        except SQLAlchemyError as error:
            print(f"Error criar usuário: {error}")
            self.session.rollback()
            return False


    def buscar(self, idDiscord):
        try:
            usuario = self.session.query(Usuario).filter(Usuario.idDiscord==idDiscord).first()
            return usuario if usuario else False
        except SQLAlchemyError as error:
            print(f"Error buscar usuário: {error}")
            return False


    def atualizar(self, idDiscord, nome, nomeGlobal):
        try:
            resultado = self.session.query(Usuario).filter(Usuario.idDiscord==idDiscord).update({"nome":nome, "nomeGlobal":nomeGlobal}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar usuário: {error}")
            self.session.rollback()
            return False


    def deletar(self, idDiscord):
        try:
            usuario = self.session.query(Usuario).filter(Usuario.idDiscord==idDiscord).first()
            if usuario:
                self.session.delete(usuario)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar usuário: {error}")
            self.session.rollback()
            return False