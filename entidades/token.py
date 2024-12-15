from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from entidades.tribo import Base

# Entidade
class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    idTribo = Column(Integer, ForeignKey("tribo.id"))
    token = Column(String)
    expira = Column(DateTime)
    tribo = relationship("Tribo", lazy="subquery")

    def __repr__(self):
        return f"[id:{self.id}, idTribo:{self.idTribo}, tribo:{self.tribo}, token:{self.token}, expira:{self.expira}]"
    

class TokenGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, idTribo, token):
        try:
            token = Token(idTribo=idTribo, token=token, expira=datetime.now())
            self.session.add(token)
            self.session.commit()
            self.session.refresh(token)
            return token if token.id else False
        except SQLAlchemyError as error:
            print(f"Error criar token: {error}")
            self.session.rollback()
            return False


    def buscar(self, id):
        try:
            token = self.session.query(Token).filter(Token.id==id).first()
            return token if token else False
        except SQLAlchemyError as error:
            print(f"Error buscar token: {error}")
            return False


    def atualizar(self, id, token):
        try:
            resultado = self.session.query(Token).filter(Token.id==id).update({"token":token}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar token: {error}")
            self.session.rollback()
            return False


    def deletar(self, id):
        try:
            token = self.session.query(Token).filter(Token.id==id).first()
            if token:
                self.session.delete(token)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar token: {error}")
            self.session.rollback()
            return False