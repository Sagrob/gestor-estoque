from django.db import models

class Fornecedor(models.Model):
    nome_social = models.CharField(
        max_length=100,
        verbose_name='Razão Social do Fornecedor'
    )
    nome_fantasia = models.CharField(
        max_length=100,
        verbose_name='Nome Fantasia do Fornecedor'
    )
    
    produtos = models.ManyToManyField(
        'produtos.Produto',
        verbose_name='Produtos do Fornecedor',
        through='FornecedorProduto',
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data de criação do fornecedor'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='data de atualização do fornecedor'
    )
    
    class Meta:
        tb_table = 'fornecedores'

class FornecedorProduto(models.Model):
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        verbose_name='Produto do Fornecedor'
    )
    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='Produto do Fornecedor'
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço do Produto'
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data de criação'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='data de atualização'
    )
    
    class Meta:
        tb_table = 'fornecedor_produto'

class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='nome do produto'
    )
    
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='categoria do produto'
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data de criação do produto'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='data de atualização do produto'
    )
    
    class Meta:
        tb_table='produtos'


class Categoria(models.Models):
    nome = models.CharField(
        max_length=100,
        verbose_name='nome da categoria'
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data de criação da categoria'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='data de atualização da categoria'
    )

    class Meta:
        tb_table = 'categorias'