def testeCriarEspecie(especieGerenciador):
    """Testa a criação de uma especie."""
    sucesso = especieGerenciador.criar("Rex", 1)
    assert sucesso is not None


def testeBuscarEspecie(especieGerenciador):
    """Testa a busca de uma especie existente."""
    especie = especieGerenciador.buscar(1)
    assert especie is not None


def testeAtualizarEspecie(especieGerenciador):
    """Testa a atualização de uma especie existente."""
    sucesso = especieGerenciador.atualizar(1, "Dodô")
    assert sucesso is not None
    especie = especieGerenciador.buscar(1)
    assert especie.nome == "Dodô"


def testeDeleteEspecie(especieGerenciador):
    """Testa a exclusão de uma especie existente."""
    sucesso = especieGerenciador.deletar(1)
    assert sucesso is not None
    especie = especieGerenciador.buscar(1)
    assert especie is not None
