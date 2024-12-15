
# DinoStat: Implementação de Testes Unitários

## Instituição

**INSTITUTO FEDERAL GOIANO – CAMPUS CERES**

**Bacharelado em Sistemas de Informação**

### Alunos Envolvidos

- Daianny Evillin Costa de Oliveira
- Emanuel Gonçalves Menezes
- Geovana Silva Matuzinho
- Lucas Santos Carvalho
- Mayko Diouzef Mendes do Amaral

**Local e Data:**
Ceres - GO, 2024

---

## Escopo do Projeto

O **Bot de Gerenciamento de Criaturas** foi desenvolvido para ajudar jogadores a organizar e monitorar as estatísticas das criaturas do jogo **ARK: Survival Ascended**. Ele substitui métodos manuais e dispersos, como blocos de notas e planilhas, oferecendo uma solução centralizada, prática e segura diretamente no Discord.

Todos os dados são inseridos manualmente pelos usuários, garantindo privacidade e praticidade. O bot respeita normas de privacidade e transparência em sua interação com os usuários.

### Funcionalidades Principais

- **Termos de Serviço e Política de Privacidade:**
  - Exibe e solicita aceitação antes do uso.
  - Links e botões para consulta das políticas.

- **Ajuda ao Usuário:**
  - Comando `/ajuda` com informações sobre uso, comandos e recursos.
  - Escolha de idioma.
  - Opções para consultar termos e políticas.

- **Gestão de Tribos:**
  - Comandos para criar, editar, excluir, transferir propriedade e listar tribos.
  - Diferentes níveis de permissão para proprietários e membros.

- **Gestão de Criaturas:**
  - Inserção manual de estatísticas e gerenciamento de dados das criaturas.

- **Segurança e Privacidade:**
  - Criptografia em trânsito (SSL/TLS) e em repouso.
  - Conformidade com leis de privacidade (GDPR, LGPD, CCPA, CPRA).

---

## Infraestrutura e Linguagem

### Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Banco de Dados:** MySQL (conexão segura)
- **Framework de Testes:** PyTest

### Detalhes do PyTest

O PyTest foi escolhido como framework de testes para garantir a qualidade do código e facilitar a identificação de bugs. Com ele, as funcionalidades do bot são validadas, assegurando um desempenho robusto e confiável.

---

## Diagrama Entidade-Relacionamento (DER)

### Principais Entidades do Banco de Dados

#### Usuário
- `id` ➔ INT
- `idTribo` ➔ INT
- `idDiscord` ➔ INT
- `nome` ➔ VARCHAR
- `nomeGlobal` ➔ VARCHAR
- `cango` ➔ ENUM
- `status` ➔ INT
- `language` ➔ VARCHAR

#### Token
- `id` ➔ INT
- `idTribo` ➔ INT
- `nome` ➔ VARCHAR

#### Espécie
- `id` ➔ INT
- `nome` ➔ VARCHAR
- `status` ➔ INT

#### Tribo
- `id` ➔ INT
- `nome` ➔ VARCHAR

#### Visitante
- `id` ➔ INT
- `idDiscord` ➔ INT
- `nome` ➔ VARCHAR
- `nomeGlobal` ➔ VARCHAR
- `language` ➔ VARCHAR

#### Criatura
- `idEspecie` ➔ INT
- `idTribo` ➔ INT
- `nome` ➔ VARCHAR
- `genero` ➔ ENUM
- `hpwild` ➔ INT
- `hpmult` ➔ INT
- `stwild` ➔ INT
- `stmult` ➔ INT
- `oxwild` ➔ INT
- `oxmult` ➔ INT
- `fowild` ➔ INT
- `fomult` ➔ INT
- `wewild` ➔ INT
- `wemult` ➔ INT
- `dmwild` ➔ INT
- `dmmult` ➔ INT
- `created` ➔ INT

---

## Plano de Testes

### Teste Unitário
Os testes unitários foram planejados para validar as entidades e funções do bot DinoStat, garantindo que cada componente funcione de forma correta e independente.

### Executando os Testes
1. Certifique-se de ter o **Python** e o **PyTest** instalados.
2. Navegue até o diretório raiz do projeto.
3. Execute o comando:

   ```bash
   pytest
   ```

4. Analise o relatório gerado para verificar os resultados.

---

## Requisitos de Segurança e Privacidade

- **Criptografia em Trânsito:** Certificado SSL/TLS ativo em todas as comunicações entre o bot e o banco de dados.
- **Criptografia em Repouso:** Dados armazenados com chave de segurança configurável.
- **Conformidade com Leis de Privacidade:** GDPR, LGPD, CCPA e CPRA, com termos claros e acessíveis aos usuários.

---

## Licença

Este projeto está licenciado sob a **Licença MIT**.
