def testeCriarVisitante(visitanteGerenciador):
    """Testa a criação de um visitante."""
    sucesso = visitanteGerenciador.criar("456", "mendes", "Isaac Mendes", "pt-BR")
    assert sucesso is not None


def testeBuscarVisitante(visitanteGerenciador):
    """Testa a busca de um visitante existente."""
    visitante = visitanteGerenciador.buscar(456)
    assert visitante is not None


def testeAtualizarVisitante(visitanteGerenciador):
    """Testa a atualização de um visitante existente."""
    sucesso = visitanteGerenciador.atualizar(456, "isaacmendes", "Isaac")
    assert sucesso is not None
    visitante = visitanteGerenciador.buscar(456)
    assert visitante.nome == "isaacmendes" and visitante.nomeGlobal == "Isaac"


def testeDeletarVisitante(visitanteGerenciador):
    """Testa a exclusão de um visitante existente."""
    sucesso = visitanteGerenciador.deletar(456)
    assert sucesso is not None
    visitante = visitanteGerenciador.buscar(456)
    assert visitante is not None
