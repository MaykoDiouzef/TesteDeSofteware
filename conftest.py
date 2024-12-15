import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from entidades.tribo import TriboGerenciador, Base
from entidades.usuario import UsuarioGerenciador
from entidades.token import TokenGerenciador
from entidades.especie import EspecieGerenciador
from entidades.visitante import VisitanteGerenciador
from entidades.criatura import CriaturaGerenciador

@pytest.fixture(scope="module")
def engine():
    """Configura o banco de dados em memória"""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture
def session(engine):
    """Cria uma nova sessão para cada teste."""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture
def triboGerenciador(session):
    """Instancia o TriboGerenciador."""
    return TriboGerenciador(session)


@pytest.fixture
def usuarioGerenciador(session):
    """Instancia o UsuarioGerenciador."""
    return UsuarioGerenciador(session)


@pytest.fixture
def tokenGerenciador(session):
    """Instancia o TokenGerenciador."""
    return TokenGerenciador(session)


@pytest.fixture
def especieGerenciador(session):
    """Instancia o EspecieGerenciador."""
    return EspecieGerenciador(session)


@pytest.fixture
def visitanteGerenciador(session):
    """Instancia o VisitanteGerenciador."""
    return VisitanteGerenciador(session)


@pytest.fixture
def criaturaGerenciador(session):
    """Instancia o CriaturaGerenciador."""
    return CriaturaGerenciador(session)
