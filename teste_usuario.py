def testeCriarUsuario(usuarioGerenciador, triboGerenciador):
    """Testa a criação de um usuário."""
    tribo = triboGerenciador.criar("Arklândia")
    sucesso = usuarioGerenciador.criar(tribo.id, "123", "isaac", "Isaac Mendes", "proprietario", 1, "pt-BR")
    assert sucesso is not None


def testeBuscarUsuario(usuarioGerenciador):
    """Testa a busca de um usuário existente."""
    usuario = usuarioGerenciador.buscar(123)
    assert usuario is not None


def testeAtualizarUsuario(usuarioGerenciador):
    """Testa a atualização de um usuário existente."""
    sucesso = usuarioGerenciador.atualizar(123, "isaacmendes", "Isaac")
    assert sucesso is not None
    usuario = usuarioGerenciador.buscar(123)
    assert usuario.nome == "isaacmendes" and usuario.nomeGlobal == "Isaac"


def testeDeletarUsuario(usuarioGerenciador):
    """Testa a exclusão de um usuário existente."""
    sucesso = usuarioGerenciador.deletar(123)
    assert sucesso is not None
    usuario = usuarioGerenciador.buscar(123)
    assert usuario is not None
