INSTITUTO FEDERAL GOIANO – CAMPUS CERES

BACHARELADO EM SISTEMAS DE INFORMAÇÃO

DINOSTAT: IMPLEMENTAÇÃO DE TESTES UNITÁRIOS

CERES – GO

2024

DAIANNY EVILLIN COSTA DE OLIVEIRA

EMANUEL GONÇALVES MENEZES

GEOVANA SILVA MATUZINHO

LUCAS SANTOS CARVALHO

MAYKO DIOUZEF MENDES DO AMARAL

DINOSTAT: IMPLEMENTAÇÃO DE TESTES UNITÁRIOS

Trabalho apresentado à disciplina Teste de Software  do curso de Bacharelado de sistemas de informação para obtenção de nota parcial.

Orientador(a): Prof. Isaac Mendes de Melo.

CERES – GO

2024

SUMÁRIO

# 1 DOCUMENTAÇÃO DO PROJETO

O Bot de Gerenciamento de Criaturas foi idealizado para atender às necessidades dos jogadores do jogo ARK: Survival Ascended, que frequentemente enfrentam desafios para manter as estatísticas de suas criaturas e tribos organizadas. Ao centralizar e facilitar o acesso a essas informações no Discord, o bot visa otimizar a experiência dos jogadores, eliminando a dependência de métodos manuais e dispersos, como planilhas e blocos de notas. Além de fornecer funcionalidades práticas e intuitivas, o projeto prioriza segurança, privacidade e conformidade com legislações como GDPR e LGPD.

## ESCOPO

O bot oferece uma solução organizada e segura para registro e consulta das estatísticas das criaturas e tribos, com dados inseridos manualmente pelos usuários. Ele substitui métodos convencionais por um sistema automatizado no Discord, tornando a gestão de informações mais prática e acessível.

Objetivos principais:

Fornecer um meio centralizado para registro e consulta das estatísticas de criaturas.

Promover acessibilidade e organização no gerenciamento de dados de tribos e criaturas.

Assegurar a segurança e privacidade dos dados dos usuários.

Funcionalidades principais:

Termos de Serviço e Política de Privacidade:

Exibição e solicitação de aceite antes do uso do bot.

Links e botões para consulta às políticas, promovendo transparência e conformidade com as normas.

Ajuda ao Usuário:

Comando /ajuda com informações sobre comandos disponíveis, recursos e escolha de idioma.

Consulta fácil aos Termos de Serviço e Política de Privacidade.

Ferramentas para o usuário gerenciar seus dados (como baixar informações ou solicitar exclusão, garantindo o direito ao esquecimento).

Gestão de Tribos:

Comando /tribo para criar, editar, excluir, transferir propriedade e listar informações.

Gerenciamento de membros com diferentes níveis de acesso e permissões.

Gestão de Criaturas:

Comando /criatura para inserir, editar, excluir e consultar as estatísticas das criaturas.

Segurança e Privacidade:

Proteção dos dados por meio de criptografia durante a transmissão e o armazenamento.

Estrita conformidade com legislações de privacidade.

## 1.2. REQUISITOS DE SEGURANÇA E PRIVACIDADE

Criptografia em trânsito: Certificado SSL/TLS para comunicação segura entre o bot e o banco de dados.

Criptografia em repouso: Proteção dos dados armazenados com chave configurável.

Conformidade com legislações de privacidade: Respeito ao GDPR, LGPD, CCPA e CPRA, com divulgação clara de termos e políticas.

# 2 LINGUAGEM E INFRAESTRUTURA

Infraestrutura:

Banco de Dados: MySQL com conexão segura.

Linguagem de Programação: Python, utilizando bibliotecas como discord.py e SQLAlchemy para gerenciamento do ORM.

Testes Automatizados:

Biblioteca PyTest: O framework PyTest foi escolhido para criar e executar testes automatizados, garantindo a qualidade do código do bot DinoStats. Essa ferramenta auxilia na identificação e correção de bugs, além de validar funcionalidades e assegurar o desempenho robusto do bot.

# 3 DER 

# 

## 3.1. PLANO DE TESTES

Usuário

id➔ INT

idTribo➔ INT

idDiscord➔ INT

nome➔ VARCHAR

nomeGlobal➔ VARCHAR

cango➔ ENUM

status➔ INT

language➔ VARCHAR

Ficha

id➔ INT

idTribo➔ INT

nome➔ VARCHAR

Espécie

id➔ INT

nome➔ VARCHAR

status➔ INT

Tribo

id➔ INT

nome➔ VARCHAR

Visitante

id➔ INT

idDiscord➔ INT

nome➔ VARCHAR

nomeGlobal➔ VARCHAR

language➔ VARCHAR

Criatura

idEspecie➔ INT

idTribo➔ INT

nome➔ VARCHAR

genero➔ ENUM

hpwild➔ INT

hpmult➔ INT

stwild➔ INT

stmult➔ INT

oxwild➔ INT

oxmult➔ INT

fowild➔ INT

fomult➔ INT

wewild➔ INT

wemult➔ INT

dmwild➔ INT

dmmult➔ INT

created➔ INT

# 

# 4 TESTE UNITÁRIO - CRIATURA

### 1. Teste de Criação de Criatura

Arquivo: teste_criatura.py
Função: testeCriarCriatura
Objetivo: Verificar a funcionalidade de criação de uma nova criatura.
Descrição:

O teste cria uma nova tribo e espécie utilizando os respectivos gerenciadores.

Em seguida, utiliza o CriaturaGerenciador para criar uma criatura com os parâmetros especificados (nome, gênero, atributos de estatísticas como HP, stamina, etc.).

O teste verifica se a criação retorna um valor não nulo, indicando sucesso.

Código:

### 2. Teste de Busca de Criatura

Arquivo: teste_criatura.py
Função: testeBuscarCriatura
Objetivo: Validar a busca de uma criatura existente no banco de dados.
Descrição:

A função utiliza o CriaturaGerenciador para buscar uma criatura com um ID específico.

O teste verifica se a busca retorna um valor não nulo, indicando que a criatura foi encontrada.

Código:

### 3. Teste de Atualização de Criatura

Arquivo: teste_criatura.py
Função: testeAtualizarCriatura
Objetivo: Confirmar que é possível atualizar os dados de uma criatura existente.
Descrição:

A função atualiza as informações da criatura (nome, atributos) utilizando o método atualizar do CriaturaGerenciador.

Em seguida, realiza uma nova busca para confirmar se o nome foi modificado corretamente.

O teste verifica se a atualização foi bem-sucedida e se o nome da criatura foi alterado.

Código:

### 4. Teste de Deleção de Criatura

Arquivo: teste_criatura.py
Função: testeDeletarCriatura
Objetivo: Testar a remoção de uma criatura existente no banco de dados.
Descrição:

A função utiliza o método deletar do CriaturaGerenciador para remover uma criatura específica.

Em seguida, tenta realizar uma busca pela criatura deletada.

O teste verifica se a deleção foi bem-sucedida.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários para a classe CriaturaGerenciador validam os principais métodos: criação, busca, atualização e deleção. Todos os testes passaram com sucesso, demonstrando que as funcionalidades implementadas estão operando conforme o esperado.

Essa abordagem garante maior qualidade no código e facilita a identificação de possíveis falhas durante o desenvolvimento do sistema.

# 5 TESTE UNITÁRIO - ESPÉCIE

### 1. Teste de Criação de Espécie

Arquivo: teste_especie.py
Função: testeCriarEspecie
Objetivo: Verificar a funcionalidade de criação de uma nova espécie.
Descrição:

Utiliza o método criar do EspecieGerenciador para adicionar uma nova espécie ao banco de dados com os parâmetros fornecidos (nome e status).

O teste valida se a operação retorna um valor não nulo, indicando sucesso na criação.

Código:

### 2. Teste de Busca de Espécie

Arquivo: teste_especie.py
Função: testeBuscarEspecie
Objetivo: Testar a busca de uma espécie existente no banco de dados.
Descrição:

Utiliza o método buscar do EspecieGerenciador para localizar uma espécie específica com base no ID.

O teste valida se a espécie retornada é não nula, indicando que ela foi encontrada.

Código:

### 

### 3. Teste de Atualização de Espécie

Arquivo: teste_especie.py
Função: testeAtualizarEspecie
Objetivo: Confirmar a capacidade de atualizar os dados de uma espécie existente.
Descrição:

Utiliza o método atualizar do EspecieGerenciador para alterar o nome de uma espécie com um ID específico.

Em seguida, realiza uma busca para verificar se o nome foi atualizado corretamente.

O teste valida se a atualização foi bem-sucedida e se o campo nome reflete a nova alteração.

Código:

### 4. Teste de Deleção de Espécie

Arquivo: teste_especie.py
Função: testeDeleteEspecie
Objetivo: Validar a funcionalidade de remoção de uma espécie existente no banco de dados.
Descrição:

Utiliza o método deletar do EspecieGerenciador para excluir uma espécie com um ID específico.

Após a deleção, realiza uma tentativa de busca pela espécie removida.

O teste verifica se a deleção foi realizada com sucesso.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários verificaram com sucesso as operações CRUD (Create, Read, Update, Delete) relacionadas à entidade Espécie. Todas as funcionalidades implementadas na classe EspecieGerenciador passaram nos testes, garantindo que o comportamento esperado foi alcançado e que a lógica do código está correta e estável.

# 6 TESTE UNITÁRIO - TOKEN

### 1. Teste de Criação de Token

Arquivo: teste_token.py
Função: testeCriarToken
Objetivo: Verificar a funcionalidade de criação de um novo token.
Descrição:

Utiliza o método criar do TokenGerenciador para adicionar um novo token ao banco de dados.

O teste depende da criação de uma tribo, necessária para referenciar o idTribo.

Valida se o retorno não é nulo, indicando sucesso na criação.

Código:

### 2. Teste de Busca de Token

Arquivo: teste_token.py
Função: testeBuscarToken
Objetivo: Testar a busca de um token existente no banco de dados.
Descrição:

Utiliza o método buscar do TokenGerenciador para localizar um token específico por seu ID.

Verifica se o retorno não é nulo, confirmando que o token foi encontrado.

Código:

### 3. Teste de Atualização de Token

Arquivo: teste_token.py
Função: testeAtualizarToken
Objetivo: Validar a atualização do valor de um token existente.
Descrição:

Utiliza o método atualizar do TokenGerenciador para modificar o valor do token.

Em seguida, realiza uma busca para verificar se o valor foi atualizado corretamente.

Valida se o campo token reflete a nova alteração.

Código:

### 4. Teste de Deleção de Token

Arquivo: teste_token.py
Função: testeDeleteToken
Objetivo: Testar a funcionalidade de remoção de um token existente.
Descrição:

Utiliza o método deletar do TokenGerenciador para remover um token específico pelo ID.

Após a deleção, tenta buscar o token para verificar se ele foi removido com sucesso.

Valida se a deleção ocorreu corretamente.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários verificaram com sucesso as operações CRUD (Create, Read, Update, Delete) relacionadas à entidade Token. Todos os métodos da classe TokenGerenciador passaram nos testes, garantindo o correto funcionamento e estabilidade das funcionalidades implementadas.

# 7 TESTE UNITÁRIO - TRIBO

### 1. Teste de Criação de Tribo

Arquivo: teste_tribo.py
Função: testeCriarTribo
Objetivo: Verificar a funcionalidade de criação de uma nova tribo.
Descrição:

Utiliza o método criar do TriboGerenciador para adicionar uma nova tribo com o nome fornecido.

O teste valida se o retorno não é nulo, indicando sucesso na criação da tribo.

Código:

### 2. Teste de Busca de Tribo

Arquivo: teste_tribo.py
Função: testeBuscarTribo
Objetivo: Testar a busca de uma tribo existente no banco de dados.
Descrição:

Utiliza o método buscar do TriboGerenciador para localizar uma tribo com base em seu ID.

O teste verifica se o retorno não é nulo, indicando que a tribo foi encontrada com sucesso.

Código:

### 3. Teste de Atualização de Tribo

Arquivo: teste_tribo.py
Função: testeAtualizarTribo
Objetivo: Validar a atualização do nome de uma tribo existente.
Descrição:

Utiliza o método atualizar do TriboGerenciador para modificar o nome de uma tribo com um ID específico.

Em seguida, realiza uma busca para confirmar se o campo nome foi atualizado corretamente.

O teste valida se o valor do nome reflete a nova alteração.

Código:

### 4. Teste de Deleção de Tribo

Arquivo: teste_tribo.py
Função: testeDeleteTribo
Objetivo: Testar a remoção de uma tribo existente no banco de dados.
Descrição:

Utiliza o método deletar do TriboGerenciador para remover uma tribo pelo ID.

Após a deleção, tenta buscar a tribo para confirmar que ela foi removida com sucesso.

O teste valida se a remoção ocorreu corretamente.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários validaram com sucesso as operações CRUD (Create, Read, Update, Delete) para a entidade Tribo. Todas as funcionalidades implementadas na classe TriboGerenciador foram testadas e aprovadas, garantindo estabilidade e confiabilidade do código.

# 8 TESTE UNITÁRIO - USUÁRIO

### 1. Teste de Criação de Usuário

Arquivo: teste_usuario.py
Função: testeCriarUsuario
Objetivo: Verificar a funcionalidade de criação de um novo usuário.
Descrição:

Utiliza o método criar do UsuarioGerenciador para adicionar um novo usuário com atributos específicos, como idDiscord, nome, nomeGlobal, cargo, etc.

O teste depende da criação de uma tribo para associar o idTribo.

Valida se o retorno não é nulo, indicando sucesso na criação do usuário.

Código:

### 2. Teste de Busca de Usuário

Arquivo: teste_usuario.py
Função: testeBuscarUsuario
Objetivo: Testar a busca de um usuário existente no banco de dados.
Descrição:

Utiliza o método buscar do UsuarioGerenciador para localizar um usuário com base no idDiscord.

Verifica se o retorno não é nulo, indicando que o usuário foi encontrado.

Código:

### 3. Teste de Atualização de Usuário

Arquivo: teste_usuario.py
Função: testeAtualizarUsuario
Objetivo: Validar a atualização dos dados de um usuário existente.
Descrição:

Utiliza o método atualizar do UsuarioGerenciador para modificar os campos nome e nomeGlobal de um usuário com base no idDiscord.

Em seguida, realiza uma busca para verificar se os campos foram atualizados corretamente.

Valida se o retorno é consistente com as alterações realizadas.

Código:

### 4. Teste de Deleção de Usuário

Arquivo: teste_usuario.py
Função: testeDeletarUsuario
Objetivo: Testar a remoção de um usuário existente no banco de dados.
Descrição:

Utiliza o método deletar do UsuarioGerenciador para excluir um usuário com base no idDiscord.

Após a remoção, tenta buscar o usuário para confirmar que ele foi deletado com sucesso.

Valida se a exclusão foi realizada corretamente.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários validaram com sucesso as operações CRUD (Create, Read, Update, Delete) relacionadas à entidade Usuário. As funcionalidades implementadas na classe UsuarioGerenciador foram testadas e aprovadas, assegurando que o comportamento esperado foi alcançado e a integridade do sistema está garantida.

# 9 TESTE UNITÁRIO - VISITANTE

### 1. Teste de Criação de Visitante

Arquivo: teste_visitante.py
Função: testeCriarVisitante
Objetivo: Verificar a funcionalidade de criação de um novo visitante.
Descrição:

Utiliza o método criar do VisitanteGerenciador para adicionar um novo visitante com os atributos idDiscord, nome, nomeGlobal e language.

O teste valida se o retorno não é nulo, indicando sucesso na criação do visitante.

Código:

### 2. Teste de Busca de Visitante

Arquivo: teste_visitante.py
Função: testeBuscarVisitante
Objetivo: Testar a busca de um visitante existente no banco de dados.
Descrição:

Utiliza o método buscar do VisitanteGerenciador para localizar um visitante com base no idDiscord.

O teste verifica se o retorno não é nulo, indicando que o visitante foi encontrado.

Código:

### 

### 3. Teste de Atualização de Visitante

Arquivo: teste_visitante.py
Função: testeAtualizarVisitante
Objetivo: Validar a atualização dos dados de um visitante existente.
Descrição:

Utiliza o método atualizar do VisitanteGerenciador para modificar os campos nome e nomeGlobal de um visitante com base no idDiscord.

Em seguida, realiza uma busca para verificar se os campos foram atualizados corretamente.

O teste valida se os valores dos campos nome e nomeGlobal refletem as alterações.

Código:

### 4. Teste de Deleção de Visitante

Arquivo: teste_visitante.py
Função: testeDeletarVisitante
Objetivo: Testar a remoção de um visitante existente no banco de dados.
Descrição:

Utiliza o método deletar do VisitanteGerenciador para excluir um visitante com base no idDiscord.

Após a remoção, tenta buscar o visitante para confirmar que ele foi deletado com sucesso.

Valida se a remoção foi realizada corretamente.

Código:

### Resultados da Execução

Comando utilizado:

Saída no terminal:

### Conclusão

Os testes unitários validaram com sucesso as operações CRUD (Create, Read, Update, Delete) para a entidade Visitante. Todas as funcionalidades implementadas na classe VisitanteGerenciador foram testadas e aprovadas, garantindo estabilidade, precisão e confiabilidade do código.

