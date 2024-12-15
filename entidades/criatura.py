from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from entidades.tribo import Base

# Entidades
class Criatura(Base):
    __tablename__ = "criatura"

    id = Column(Integer, primary_key=True)
    idEspecie = Column(Integer, ForeignKey("especie.id"))
    idTribo = Column(Integer, ForeignKey("tribo.id"))
    nome = Column(String)
    genero = Column(String)
    hpwild = Column(Integer, default=0)
    hpmult = Column(Integer, default=0)
    stwild = Column(Integer, default=0)
    stmult = Column(Integer, default=0)
    oxwild = Column(Integer, default=0)
    oxmult = Column(Integer, default=0)
    fowild = Column(Integer, default=0)
    fomult = Column(Integer, default=0)
    wewild = Column(Integer, default=0)
    wemult = Column(Integer, default=0)
    dmwild = Column(Integer, default=0)
    dmmult = Column(Integer, default=0)
    especie = relationship("Especie", lazy="subquery")
    tribo = relationship("Tribo", lazy="subquery")
    
    def __repr__(self):
        return f"[id:{self.id}, especie:{self.especie}, idEspecie:{self.idEspecie}, tribo:{self.tribo}, idTribo:{self.idTribo}, nome:'{self.nome}', genero:'{self.genero}', hpwild:{self.hpwild}, hpmult:{self.hpmult}, stwild:{self.stwild}, stmult:{self.stmult}, oxwild:{self.oxwild}, oxmult:{self.oxmult}, fowild:{self.fowild}, fomult:{self.fomult}, wewild:{self.wewild}, wemult:{self.wemult}, dmwild:{self.dmwild}, dmmult:{self.dmmult}]"
    

class CriaturaGerenciador:
    def __init__(self, session):
        self.session = session

    def criar(self, idEspecie, idTribo, nome, genero, hpwild, hpmult, stwild, stmult, oxwild, oxmult, fowild, fomult, wewild, wemult, dmwild, dmmult):
        try:
            criatura = Criatura(idEspecie=idEspecie, idTribo=idTribo, nome=nome, genero=genero, hpwild=hpwild, hpmult=hpmult, stwild=stwild, stmult=stmult, oxwild=oxwild, oxmult=oxmult, fowild=fowild, fomult=fomult, wewild=wewild, wemult=wemult, dmwild=dmwild, dmmult=dmmult)
            self.session.add(criatura)
            self.session.commit()
            self.session.refresh(criatura)
            return criatura if criatura.id else False
        except SQLAlchemyError as error:
            print(f"Error criar criatura: {error}")
            self.session.rollback()
            return False


    def buscar(self, id):
        try:
            criatura = self.session.query(Criatura).filter(Criatura.id==id).first()
            return criatura if criatura else False
        except SQLAlchemyError as error:
            print(f"Error buscar criatura: {error}")
            return False


    def atualizar(self, id, idEspecie, idTribo, nome, hpwild, hpmult, stwild, stmult, oxwild, oxmult, fowild, fomult, wewild, wemult, dmwild, dmmult):
        try:
            resultado = self.session.query(Criatura).filter(Criatura.id==id).update({"idEspecie":idEspecie, "idTribo":idTribo, "nome":nome, "hpwild":hpwild, "hpmult":hpmult, "stwild":stwild, "stmult":stmult, "oxwild":oxwild, "oxmult":oxmult, "fowild":fowild, "fomult":fomult, "wewild":wewild, "wemult":wemult, "dmwild":dmwild, "dmmult":dmmult}, synchronize_session="evaluate")
            self.session.commit()
            return resultado if resultado else False
        except SQLAlchemyError as error:
            print(f"Error atualizar criatura: {error}")
            self.session.rollback()
            return False


    def deletar(self, id):
        try:
            criatura = self.session.query(Criatura).filter(Criatura.id==id).first()
            if criatura:
                self.session.delete(criatura)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as error:
            print(f"Error deletar criatura: {error}")
            self.session.rollback()
            return False