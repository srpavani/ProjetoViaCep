from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from  ..models import ViaCepModel
from .serializers import CepSerializer
import requests



class ViaCepViewSet(ModelViewSet):
    queryset = ViaCepModel.objects.all()
    serializer_class = CepSerializer

    def create(self, request):
    # Use request.data para obter os dados da solicitação HTTP
        cep = request.data.get('cep', '00000000')
        site = (f'https://viacep.com.br//ws/{cep}/json/')
        requisicao = requests.get(site)
        json = requisicao.json()

        cep = json.get('cep', '')
        logradouro = json.get('logradouro', '')
        complemento = json.get('complemento', '')  # Adicione uma vírgula aqui
        bairro = json.get('bairro', '')
        localidade = json.get('localidade', '')
        uf = json.get('uf', '')

        dadosrecebidos = {
            "cep": f"{cep}",
            "logradouro": f"{logradouro}",
            "complemento": f"{complemento}",
            "bairro": f"{bairro}",
            "localidade": f"{localidade}",
            "uf": f"{uf}" 
        }
        

        meuserializer = CepSerializer(data=dadosrecebidos)
        if meuserializer.is_valid():

            cep_pesquisado = ViaCepModel.objects.filter(cep=cep)
            cep_pesquisado_existe = cep_pesquisado.exists()

            if cep_pesquisado_existe:
                return Response({"aviso": "seu cep ja existe no bd"})
            meuserializer.save()
            return Response(meuserializer.data)
        else:
            return Response({"aviso": "erro da um jeito"})
