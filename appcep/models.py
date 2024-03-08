from django.db import models


class ViaCepModel(models.Model):
    cep = models.CharField(verbose_name="cep", max_length=20)
    logradouro = models.CharField(verbose_name="rua", max_length=35,  blank=True, null=True)
    complemento = models.CharField(verbose_name="complemento", max_length=20, blank=True, null=True)
    bairro = models.CharField(verbose_name="bairro", max_length=20,  blank=True, null=True)
    localidade = models.CharField(verbose_name="localidade", max_length=20,  blank=True, null=True)
    uf = models.CharField(verbose_name="uf", max_length=20,  blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.cep} {self.logradouro} {self.complemento} {self.bairro} {self.localidade} {self.uf}"