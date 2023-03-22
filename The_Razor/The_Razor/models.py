from django.db import models

# Create your models here.

# Dados Pessoais
#
# - CPF
# - Nome
# - Email
# - Telefone
# - Senha
# - Data de Nascimento
# - Foto


class DadosPessoais(models.Model):
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    nome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=30,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=12,
        null=False,
        blank=False,
    )

    senha = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to='fotos_dados_pessoais'
    )


# ESTABELECIMENTO
#
# - Nome
# - Endereço
# - Informação
# - Foto
# - Localização


class Estabelecimento(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to='fotos_estabelecimentos'
    )

    localizacao = models.ImageField(
        null=True,
        blank=True,
        upload_to='imagens_locais'
    )

# ADMINISTRADOR
#
# - Dados Pessoais
# - Estabelecimento gerenciado


class Administrador(models.Model):
    dados_pessoais = models.ForeignKey(
        'DadosPessoais',
        on_delete=models.CASCADE
    )

    estabelecimento = models.ForeignKey(
        'Estabelecimento',
        on_delete=models.CASCADE
    )

# GERENTE
#
# - Dados Pessoais
# - Estabelecimento de trabalho
# - Salário


class Gerente(models.Model):
    dados_pessoais = models.ForeignKey(
        'DadosPessoais',
        on_delete=models.CASCADE
    )

    estabelecimento = models.ForeignKey(
        'Estabelecimento',
        on_delete=models.CASCADE
    )

    salario = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False
    )

# FUNÇÕES
#
# - Especificação


class Funcoes(models.Model):
    especificacao = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
# PRODUTOS
#
# - NOME
# - QUANTIDADE
# - PREÇO


class Produtos(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    quantidade = models.IntegerField(
        null=False,
        blank=False
    )

    preco = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
# PROFISSIONAL
#
# - Dados Pessoais
# - Biografia
# - Salário
# - Gastos
# - Funções
# - Estabelecimento de trabalho
# - Gerente


class Profissional(models.Model):
    dados_pessoais = models.ForeignKey(
        'DadosPessoais',
        on_delete=models.CASCADE
    )

    biografia = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    salario = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )

    gastos = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )

    funcoes = models.ForeignKey(
        'Funcoes',
        on_delete=models.CASCADE
    )

    estabelecimento_trabalho = models.ForeignKey(
        'Estabelecimento',
        on_delete=models.CASCADE
    )

    gerente = models.ForeignKey(
        'Gerente',
        on_delete=models.CASCADE
    )

# FUNÇÕES DO PROFISSIONAL
#
# - Profissional
# - Função


class FuncoesProfissional(models.Model):
    profissional = models.ForeignKey(
        'Profissional',
        on_delete=models.CASCADE
    )

    funcoes = models.ForeignKey(
        'Funcoes',
        on_delete=models.CASCADE
    )


# PRODUTOS DE TRABALHO
#
# - Profissional
# - Produto utilizado
# - Quantidade Cedida


class ProdutosTrabalho(models.Model):
    profissional = models.ForeignKey(
        'Profissional',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        'Produtos',
        on_delete=models.CASCADE
    )

    quantidade_cedida = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

# VENDA PARA O PROFISSIONAL
#
# - Profissional
# - Produto
# - Quantidade Vendida


class VendaProfissional(models.Model):
    profissional = models.ForeignKey(
        'Profissional',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        'Produtos',
        on_delete=models.CASCADE
    )

    quantidade_vendida = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
# CLIENTE
#
# - Dados Pessoais
# - Interesses do Cliente
# - Data de Cadastro
# - Quantidade de atendimentos


class Cliente(models.Model):
    dados_pessoais = models.ForeignKey(
        'DadosPessoais',
        on_delete=models.CASCADE
    )

    interesses = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    qtd_atendimento = models.IntegerField(
        null=False,
        blank=True
    )


# ATENDIMENTO
#
# - Profissional
# - Cliente
# - Data do Atendimento


class Atendimento(models.Model):

    profissional = models.ForeignKey(
        'Profissional',
        on_delete=models.CASCADE
    )

    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE
    )

# VENDAS PARA O CLIENTE
#
# - Cliente
# - Produto
# - Quantidade Vendida


class VendasCliente(models.Model):
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        'Produtos',
        on_delete=models.CASCADE
    )

    quantidade_vendida = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

