from django.test import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import *
from rest_framework import status
import json
import requests

# python manage.py dumpdata -o fixtures.json --exclude=contenttypes
# python manage.py test aluguel.tests
class APITest(TestCase):

  fixtures = ['fixtures.json']

  # def setUp(self):
  #     self.token = self.get_token()

  def test_token(self, username='luiza', password='l12345678'):
      request_data = {'username': username, 'password': password}
      response = self.client.post(reverse('api-token-auth'), data=request_data)
      print ('Token %s' % response.data['token'])
      self.assertEqual(response.status_code, 200)
      return 'Token %s' % response.data['token']

  def test_user_list(self):
    response = self.client.get(reverse('user-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_user_detail(self):
    response = self.client.get(reverse('user-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_funcionario_list(self):
    response = self.client.get(reverse('funcionario-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_funcionario_detail(self):
    resultado = requests.get('http://127.0.0.1:8000/funcionario/1')
    self.assertEqual(resultado.status_code, status.HTTP_200_OK)

  def test_genero_list(self):
    response = self.client.get(reverse('genero-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_genero_detail(self):
    response = self.client.get(reverse('genero-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_filme_list(self):
    response = self.client.get(reverse('filme-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_filme_detail(self):
    response = self.client.get(reverse('filme-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_cliente_list_not_auth(self):
      resultado = requests.get('http://127.0.0.1:8000/clientes/')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_cliente_list_auth(self):
    resultado = requests.get('http://127.0.0.1:8000/clientes/', auth=('maria', 'm12345678'))
    self.assertEqual(resultado.status_code, status.HTTP_200_OK)

  def test_cliente_detail_list_not_auth(self):
      resultado = requests.get('http://127.0.0.1:8000/cliente/1')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_cliente_detail_list_auth(self):
    resultado = requests.get('http://127.0.0.1:8000/cliente/1', auth=('maria', 'm12345678'))
    self.assertEqual(resultado.status_code, status.HTTP_200_OK)

  def test_aluguel_detail_list_not_auth(self):
      resultado = requests.get('http://127.0.0.1:8000/aluguel/1')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_aluguel_detail_list_auth(self):
    resultado = requests.get('http://127.0.0.1:8000/aluguel/1', auth=('maria', 'm12345678'))
    self.assertEqual(resultado.status_code, status.HTTP_200_OK)

  def test_new_genero_not_auth(self):
    response = json.dumps({"descricao": "comédia"})
    resultado = requests.post('http://127.0.0.1:8000/generos/',
                              data=response,
                              headers={'content-type': 'application/json'})

    self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # def test_new_genero_auth(self):
  #   response = json.dumps({"descricao": "Comédia"})
  #   resultado = requests.post('http://127.0.0.1:8000/generos/',
  #                             data=response,
  #                             headers={'content-type': 'application/json'},
  #                             auth=('maria', 'm12345678'))
  #
  #   self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_new_genero_not_auth(self):
    response = json.dumps({"descricao": "Comédia"})
    resultado = requests.post('http://127.0.0.1:8000/generos/',
                              data=response,
                              headers={'content-type': 'application/json'})

    self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # def test_delete_genero_auth(self):
  #     resultado = requests.delete('http://127.0.0.1:8000/genero/4/', auth=('maria', 'm12345678'))
  #     self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_genero_not_auth(self):
      resultado = requests.delete('http://127.0.0.1:8000/genero/3/')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_update_genero_auth(self):
      response = json.dumps({"descricao": "Aventura"})
      resultado = requests.patch('http://127.0.0.1:8000/genero/4/',
                               data=response,
                               headers={'content-type': 'application/json'},
                               auth=('maria', 'm12345678'))
      self.assertEqual(resultado.status_code, status.HTTP_200_OK)

  def test_update_genero_not_auth(self):
      response = json.dumps({"descricao": "Aventura"})
      resultado = requests.patch('http://127.0.0.1:8000/genero/8/',
                                 data=response,
                                 headers={'content-type': 'application/json'})
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # def test_new_aluguel_auth(self):
  #     response = json.dumps({"dataPrevistaDevolucao": "2017-09-12",
  #                            "filme": 'http://127.0.0.1:8000/filme/1/',
  #                            "cliente": 'http://127.0.0.1:8000/cliente/1/'})
  #     resultado = requests.post('http://127.0.0.1:8000/alugueis/',
  #                               data=response,
  #                               headers={'content-type': 'application/json'},
  #                               auth=('maria', 'm12345678'))
  #     # print('status_code: '+str(resultado.status_code)+'\n'+resultado.text)
  #
  #     self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_new_aluguel_not_auth(self):
      response = json.dumps({"dataPrevistaDevolucao": "2017-02-03",
                             "filme": 'http://127.0.0.1:8000/filme/2/',
                             "cliente": 'http://127.0.0.1:8000/cliente/1/'})
      resultado = requests.post('http://127.0.0.1:8000/alugueis/',
                                data=response,
                                headers={'content-type': 'application/json'})

      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_aluguel_not_auth(self):
      resultado = requests.delete('http://127.0.0.1:8000/aluguel/1/')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # def test_delete_aluguel_auth(self):
  #     resultado = requests.delete('http://127.0.0.1:8000/aluguel/2/', auth=('maria', 'm12345678'))
  #     self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)

  # def test_new_cliente_auth(self):
  #     response = json.dumps({"nome": "Florentina Carla",
  #                            "dataNasc": '2000-05-04',
  #                            'cpf': '00.000.000-00'})
  #     resultado = requests.post('http://127.0.0.1:8000/clientes/',
  #                               data=response,
  #                               headers={'content-type': 'application/json'},
  #                               auth=('maria', 'm12345678'))
  #
  #     self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_new_cliente_not_auth(self):
      response = json.dumps({"nome": "Florentina Carla",
                             "dataNasc": '2000-05-04',
                             'cpf': '00.000.000-00'})
      resultado = requests.post('http://127.0.0.1:8000/clientes/',
                                data=response,
                                headers={'content-type': 'application/json'})

      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)



  def test_delete_cliente_not_auth(self):
      resultado = requests.delete('http://127.0.0.1:8000/cliente/1/')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)


  # def test_delete_cliente_auth(self):
  #     resultado = requests.delete('http://127.0.0.1:8000/cliente/1/', auth=('maria', 'm12345678'))
  #     self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)

  # def test_new_filme_auth(self):
  #     response = json.dumps({"nome": "Minha mãe é uma peça",
  #                            "valor": '5.0',
  #                            'categoria': "http://127.0.0.1:8000/genero/2/"})
  #     resultado = requests.post('http://127.0.0.1:8000/filmes/',
  #                               data=response,
  #                               headers={'content-type': 'application/json'},
  #                               auth=('maria', 'm12345678'))
  #
  #     self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_new_filme_not_auth(self):
      response = json.dumps({"nome": "Minha mãe é uma peça",
                             "valor": '5.0',
                             'categoria': "http://127.0.0.1:8000/genero/5/"})
      resultado = requests.post('http://127.0.0.1:8000/filmes/',
                                data=response,
                                headers={'content-type': 'application/json'})

      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_filme_not_auth(self):
      resultado = requests.delete('http://127.0.0.1:8000/filme/1/')
      self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # def test_delete_filme_not_auth(self):
  #     resultado = requests.delete('http://127.0.0.1:8000/filme/1/', auth=('maria', 'm12345678'))
  #     self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)



      # def test_new_funcionario_auth(self):
      #     response = json.dumps({"nome": "André",
      #                            "salario": '1000.000'})
      #     resultado = requests.post('http://127.0.0.1:8000/funcionarios/',
      #                               data=response,
      #                               headers={'content-type': 'application/json'},
      #                               auth=('maria', 'm11111111'))
      #
      #     self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)


      # def test_new_funcionario_not_auth(self):
      #     response = json.dumps({"nome": "André",
       #                            "salario": '1000.000'})
      #     resultado = requests.post('http://127.0.0.1:8000/funcionarios/',
      #                               data=response,
      #                               headers={'content-type': 'application/json'})
      #
      #     self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)
      #
      # def test_delete_funcionario_not_auth(self):
      #     resultado = requests.delete('http://127.0.0.1:8000/aluguel/2/')
      #     self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

      # def test_delete_funcionario_auth(self):
      #     resultado = requests.delete('http://127.0.0.1:8000/aluguel/2/', auth=('maria', 'm11111111'))
      #     self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)

      # #PROBLEMAAAAAAAAAAAAAAAAAAAAAA
  # def test_update_aluguel_not_auth(self):
  #     response = json.dumps({"filme": 'http://127.0.0.1:8000/filme/2/'})
  #     resultado = requests.patch('http://127.0.0.1:8000/aluguel/4',
  #                               data={"filme": 'htt/p://127.0.0.1:8000/filme/2/'})
  #     print('status_code: '+str(resultado.status_code)+'\n'+resultado.text)
  #
  #     self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  # # def test_update_aluguel_auth(self):
  # #     response = json.dumps({"filme": 'http://127.0.0.1:8000/filme/1/'})
  # #     resultado = requests.patch('http://127.0.0.1:8000/aluguel/4',
  # #                                data=response,
  # #                                headers={'content-type': 'application/json'},
  # #                                auth=('maria', 'm11111111'))
  # #     self.assertEqual(resultado.status_code, status.HTTP_200_OK)
  #
  #
  # #problemaaaaa
  # # def test_update_funcionario_not_auth(self):
  # #     response = json.dumps({"nome": "André"})
  # #     resultado = requests.put('http://127.0.0.1:8000/funcionario/4',
  # #                               data=response,
  # #                               headers={'content-type': 'application/json'})
  # #
  # #     self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)
  #
  #
  # CLIENTE E FILME