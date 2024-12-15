def testeCriarTribo(triboGerenciador):
    """Testa a criação de uma tribo."""
    sucesso = triboGerenciador.criar("Arklândia")
    assert sucesso is not None


def testeBuscarTribo(triboGerenciador):
    """Testa a busca de uma tribo existente."""
    tribo = triboGerenciador.buscar(1)
    assert tribo is not None


def testeAtualizarTribo(triboGerenciador):
    """Testa a atualização de uma tribo existente."""
    sucesso = triboGerenciador.atualizar(1, "G.A.B")
    assert sucesso is not None
    tribo = triboGerenciador.buscar(1)
    assert tribo.nome == "G.A.B"


def testeDeleteTribo(triboGerenciador):
    """Testa a exclusão de uma tribo existente."""
    sucesso = triboGerenciador.deletar(1)
    assert sucesso is not None
    tribo = triboGerenciador.buscar(1)
    assert tribo is not None
