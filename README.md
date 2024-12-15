# DINOSTAT: IMPLEMENTAÇÃO DE TESTES UNITÁRIOS

## INSTITUTO FEDERAL GOIANO – CAMPUS CERES  
**BACHARELADO EM SISTEMAS DE INFORMAÇÃO**

**Autores**:  
- Daianny Evillin Costa de Oliveira  
- Emanuel Gonçalves Menezes  
- Geovana Silva Matuzinho  
- Lucas Santos Carvalho  
- Mayko Diouze Mendes do Amaral  

**Orientador**: Prof. Isaac Mendes de Melo  

---

## SUMÁRIO  

1. [DOCUMENTAÇÃO DO PROJETO](#documentação-do-projeto)  
    1.1. [ESCOPO](#escopo)  
    1.2. [REQUISITOS DE SEGURANÇA E PRIVACIDADE](#requisitos-de-segurança-e-privacidade)  
2. [LINGUAGEM E INFRAESTRUTURA](#linguagem-e-infraestrutura)  
3. [DER (Diagrama Entidade-Relacionamento)](#der-diagrama-entidade-relacionamento)  
4. [PLANO DE TESTES](#plano-de-testes)  
5. [TESTES UNITÁRIOS](#testes-unitários)  

---

## DOCUMENTAÇÃO DO PROJETO

O **Bot de Gerenciamento de Criaturas** foi desenvolvido para jogadores do jogo **ARK: Survival Ascended**, que enfrentam dificuldades em organizar as estatísticas de suas criaturas e tribos. O bot centraliza essas informações diretamente no **Discord**, eliminando métodos manuais como planilhas e blocos de notas.

### ESCOPO

**Objetivos principais:**  
- Fornecer um meio centralizado para registro e consulta de estatísticas.  
- Promover a organização e acessibilidade no gerenciamento de dados.  
- Assegurar a segurança e privacidade dos dados dos usuários.  

**Funcionalidades principais:**  
- **Termos de Serviço e Política de Privacidade:** Exibição e aceite obrigatório.  
- **Ajuda ao Usuário:** Comando `/ajuda` com instruções sobre os recursos.  
- **Gestão de Tribos:** Comandos para criação, edição, exclusão e listagem de tribos.  
- **Gestão de Criaturas:** Comandos para inserir, editar, excluir e consultar estatísticas das criaturas.  

### REQUISITOS DE SEGURANÇA E PRIVACIDADE

- **Criptografia em Trânsito:** SSL/TLS para comunicação segura.  
- **Criptografia em Repouso:** Dados protegidos com chave configurável.  
- **Conformidade Legal:** GDPR, LGPD, CCPA e CPRA.  

---

## LINGUAGEM E INFRAESTRUTURA

- **Banco de Dados:** MySQL com conexão segura.  
- **Linguagem de Programação:** Python.  
- **ORM:** SQLAlchemy.  
- **Bibliotecas de Teste:** PyTest para testes unitários automatizados.  

---

## DER (Diagrama Entidade-Relacionamento)

### Entidades

**Usuário**  
- `id` INT  
- `idTribo` INT  
- `idDiscord` INT  
- `nome` VARCHAR  
- `nomeGlobal` VARCHAR  
- `cargo` ENUM  
- `status` INT  
- `language` VARCHAR  

**Espécie**  
- `id` INT  
- `nome` VARCHAR  
- `status` INT  

**Tribo**  
- `id` INT  
- `nome` VARCHAR  

**Visitante**  
- `id` INT  
- `idDiscord` INT  
- `nome` VARCHAR  
- `nomeGlobal` VARCHAR  
- `language` VARCHAR  

**Criatura**  
- `idEspecie` INT  
- `idTribo` INT  
- `nome` VARCHAR  
- `genero` ENUM  
- `hpwild`, `hpmult` INT  
- `stwild`, `stmult` INT  
- `created` TIMESTAMP  

---

## PLANO DE TESTES

Os testes são aplicados às seguintes classes:  
- Criatura  
- Espécie  
- Token  
- Tribo  
- Usuário  
- Visitante  

Os testes validam as operações **CRUD** (Create, Read, Update, Delete).  

---

## TESTES UNITÁRIOS

### Teste Unitário - Criatura
1. **Criação de Criatura**: Verifica a criação bem-sucedida de uma criatura.  
2. **Busca de Criatura**: Valida a busca por ID da criatura.  
3. **Atualização de Criatura**: Confirma a atualização dos dados.  
4. **Deleção de Criatura**: Testa a remoção do banco de dados.  

---

### Teste Unitário - Espécie
1. **Criação de Espécie**: Valida o método de criação.  
2. **Busca de Espécie**: Valida o método de busca.  
3. **Atualização de Espécie**: Confirma alterações nos dados.  
4. **Deleção de Espécie**: Testa a remoção de espécies.  

---

### Teste Unitário - Token
1. **Criação de Token**: Verifica a funcionalidade de criação.  
2. **Busca de Token**: Valida o método de busca.  
3. **Atualização de Token**: Testa modificações no valor do token.  
4. **Deleção de Token**: Valida a exclusão.  

---

### Teste Unitário - Tribo
1. **Criação de Tribo**: Testa a criação de uma nova tribo.  
2. **Busca de Tribo**: Valida buscas por ID.  
3. **Atualização de Tribo**: Confirma alterações no nome.  
4. **Deleção de Tribo**: Testa exclusão de tribos.  

---

### Teste Unitário - Usuário
1. **Criação de Usuário**: Valida a criação de usuários.  
2. **Busca de Usuário**: Testa buscas por ID.  
3. **Atualização de Usuário**: Verifica mudanças de dados.  
4. **Deleção de Usuário**: Testa remoção do banco.  

---

### Teste Unitário - Visitante
1. **Criação de Visitante**: Verifica a criação de visitantes.  
2. **Busca de Visitante**: Valida o método de busca.  
3. **Atualização de Visitante**: Testa alterações de dados.  
4. **Deleção de Visitante**: Confirma remoções.  

---

## RESULTADOS DA EXECUÇÃO

Os testes unitários foram executados com sucesso utilizando o comando:  
```bash
pytest -v
```bash

### Saída esperada:

Todos os testes PASSARAM com sucesso.
Operações CRUD validadas para cada entidade.

## CONCLUSÃO
Os testes unitários garantem a estabilidade e funcionalidade do DinoStat. O uso de PyTest assegura a robustez e qualidade do sistema, cumprindo os requisitos de segurança e privacidade.
