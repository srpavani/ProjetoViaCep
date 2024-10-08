from rest_framework.serializers import ModelSerializer
from ..models import ViaCepModel


class CepSerializer(ModelSerializer):
    class Meta:
        model = ViaCepModel
        fields = ["id", "cep", "bairro", "logradouro", "complemento", "localidade"]
