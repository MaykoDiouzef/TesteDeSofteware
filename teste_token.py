def testeCriarToken(tokenGerenciador, triboGerenciador):
    """Testa a criação de um token."""
    tribo = triboGerenciador.criar("Arklândia")
    sucesso = tokenGerenciador.criar(tribo.id, "qwert")
    assert sucesso is not None


def testeBuscarToken(tokenGerenciador):
    """Testa a busca de um token existente."""
    token = tokenGerenciador.buscar(1)
    assert token is not None


def testeAtualizarToken(tokenGerenciador):
    """Testa a atualização de um token existente."""
    sucesso = tokenGerenciador.atualizar(1, "asdfg")
    assert sucesso is not None
    token = tokenGerenciador.buscar(1)
    assert token.token == "asdfg"


def testeDeleteToken(tokenGerenciador):
    """Testa a exclusão de um token existente."""
    sucesso = tokenGerenciador.deletar(1)
    assert sucesso is not None
    token = tokenGerenciador.buscar(1)
    assert token is not None
