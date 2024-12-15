def testeCriarCriatura(criaturaGerenciador, triboGerenciador, especieGerenciador):
    """Testa a criação de uma criatura."""
    tribo = triboGerenciador.criar("Arklândia")
    especie = especieGerenciador.criar("Rex", 1)
    sucesso = criaturaGerenciador.criar(especie.id, tribo.id, "Banguelo", "Macho", 14, 74, 78, 87, 54, 45, 12, 21, 36, 63, 1, 2)
    assert sucesso is not None


def testeBuscarCriatura(criaturaGerenciador):
    """Testa a busca de uma criatura existente."""
    criatura = criaturaGerenciador.buscar(1)
    assert criatura is not None


def testeAtualizarCriatura(criaturaGerenciador):
    """Testa a atualização de uma criatura existente."""
    sucesso = criaturaGerenciador.atualizar(1, 1, 1, "Dentuço", 85, 58, 74, 47, 96, 36, 25, 52, 41, 14, 98, 89)
    assert sucesso is not None
    criatura = criaturaGerenciador.buscar(1)
    assert criatura.nome == "Dentuço"


def testeDeletarCriatura(criaturaGerenciador):
    """Testa a exclusão de uma criatura existente."""
    sucesso = criaturaGerenciador.deletar(1)
    assert sucesso is not None
    criatura = criaturaGerenciador.buscar(1)
    assert criatura is not None
