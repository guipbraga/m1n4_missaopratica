from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa1 = Pessoa(nome='João', numeroConta='556677', dataAberturaConta='2024-08-01',status=True)

attrs = vars(pessoa1)
print('Instancia da classe Pessoa: ')
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa_fisica1 = PessoaFisica(nome='João', numeroConta='556677', dataAberturaConta='2024-08-01',status=True, dataNascimento='2000-01-01', cpf='123.456.789.10', rg='987456-1')
attrs = vars(pessoa_fisica1)
print('Instancia da classe PessoaFisica: ')
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa_juridica1 = PessoaJuridica(nome='João', numeroConta='556677', dataAberturaConta='2024-08-01',status=True, dataAberturaEmpresa= '2020-05-05', cnpj= '12.345.567/0001-89')
attrs = vars(pessoa_juridica1)
print('Instancia da classe PessoaJurica: ')
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa1.nome = "João Silva"
pessoa_fisica1.cpf = "10987654321"
pessoa_fisica1.cpf = "109.876.543-21"
pessoa_juridica1.cnpj = "98.765.432/0001-00" 
