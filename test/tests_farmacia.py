import sys

# Adicionando o caminho do módulo src ao sys.path
sys.path.append('/home/frankazevedo/Workspaces/python_fundamental/env/IARTES/trabalho_final')

from src import farmacia as farm


class TestFarmacia:
    # Setup: atributos base para todos os testes
    
    nome = 'Farma 10'
    
    endereco = { 
        'rua' : 'rua baker', 
        'numero' : '221b', 
        'complemento': 'Casa do Sherlock Holmes', 
        'bairro': 'parque 10', 
        'cidade': 'londres', 
        'estado' : 'am', 
        'país': 'br'
        }
    
    estoque = { 
        'dipirona' : '10', 
        'ibuprofeno' : '2', 
        'aspirina' : '0'
        } 
    
    quantidade_clientes = 10
    
    quantidade_funcionarios = 2
    
    desconto_medicamentos = {
        'dipirona' : '0.12', 
        'ibuprofeno' : '0.4', 
        'paracetamol' : '0.37',
        'losartana' : '0.0'
        }

    faturamento_mensal = {
        'janeiro' : '2000.00', 
        'fevereiro' : '0.0', 
        'março' : '-100.00'
        }
    
    # testes dos atributos e métodos da classe Farmacia
        
    def test_get_nome(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        assert farmacia.get_nome() == self.nome.lower()
    
    def test_set_nome(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        novo_nome = 'Farma Nova'
        farmacia.set_nome(novo_nome)
        assert farmacia.get_nome() == novo_nome.lower()

    def test_get_endereco(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        assert farmacia.get_endereco() == {chave.lower(): valor.lower() for chave, valor in self.endereco.items()}
    
    def test_set_endereco(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque) 
        novo_endereco = { 
            'rua' : 'rua Abbey Road', 
            'numero' : 'NW8 9AY', 
            'complemento': 'A Rua dos Beatles', 
            'bairro': 'flores', 
            'cidade': 'londres', 
            'estado' : 'am', 
            'país': 'br'
            }
        farmacia.set_endereco(novo_endereco)
        assert farmacia.get_endereco() == {chave.lower(): valor.lower() for chave, valor in novo_endereco.items()}
    
    def test_get_estoque(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        assert farmacia.get_estoque() == {chave.lower(): valor.lower() for chave, valor in self.estoque.items()}
    
    def test_set_estoque(self):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        novo_estoque = { 
            'Paracetamol' : '200',
            'Ibuprofeno' : '10',
            'Aspirina' : '24',
            'Dipirona' : '10' 
            }
        farmacia.set_estoque(novo_estoque)
        assert farmacia.get_estoque() == {chave.lower(): valor.lower() for chave, valor in novo_estoque.items()}
    
    def test_exibir_informacoes_cadastrais_completas(self, capsys):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        farmacia.exibir_informacoes_cadastrais()
        # funcionalidade do pytest que captura a saída impressa pelo método exibir_informacoes_cadastrais()
        captured = capsys.readouterr()
        # saída esperada: string formatada 
        expected_output = 'Nome: farma 10\nEndereço: rua: rua baker, numero: 221b, complemento: casa do sherlock holmes, bairro: parque 10, cidade: londres, estado: am, país: br\n'        
        assert captured.out == expected_output
    
    # atributo 'nome' ausente (string vazia)
    def test_exibir_informacoes_cadastrais_incompletas(self, capsys):
        farmacia = farm.Farmacia('', self.endereco, self.estoque)
        farmacia.exibir_informacoes_cadastrais()
        # funcionalidade do pytest que captura a saída impressa pelo método exibir_informacoes_cadastrais()
        captured = capsys.readouterr()
        # saída esperada: string formatada 
        expected_output = 'Cadastro incompleto ou inválido\n'        
        assert captured.out == expected_output

    def test_exibir_estoque(self, capsys):
        farmacia = farm.Farmacia(self.nome, self.endereco, self.estoque)
        farmacia.exibir_estoque()
        # funcionalidade do pytest que captura a saída impressa pelo método exibir_estoque()
        captured = capsys.readouterr()
        # saída esperada: string formatada
        expected_output = 'Estoque:\ndipirona: 10 unidade(s)\nibuprofeno: 2 unidade(s)\naspirina: 0 unidade(s)\n'
        assert captured.out == expected_output
    
    # testes dos atributos e métodos da classe FarmaciaVarejo
    
    def test_get_quantidade_clientes(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        assert farmacia.get_quantidade_clientes() == self.quantidade_clientes
    
    def test_set_quantidade_clientes(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        nova_quantidade_clientes = 30
        farmacia.set_quantidade_clientes(nova_quantidade_clientes)
        assert farmacia.get_quantidade_clientes() == nova_quantidade_clientes
    
    def test_get_quantidade_funcionarios(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        assert farmacia.get_quantidade_funcionarios() == self.quantidade_funcionarios
    
    def test_set_quantidade_funcionarios(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        nova_quantidade_funcionarios = 20
        farmacia.set_quantidade_funcionarios(nova_quantidade_funcionarios)
        assert farmacia.get_quantidade_funcionarios() == nova_quantidade_funcionarios
    
    # quantidade de medicamento negativa (inválida)
    def test_comprar_medicamento_quantidade_invalida(self, capsys):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'dipirona'
        quantidade = -5
        farmacia.comprar_medicamento(medicamento, quantidade)
        captured = capsys.readouterr()
        expected_output = 'Quantidade inválida\n'
        assert captured.out == expected_output
    
    # comportamento adequado: medicamento existe no estoque e a quantidade é válida
    def test_comprar_medicamento_existente_quantidade_valida(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'dipirona'
        quantidade = 3
        farmacia.comprar_medicamento(medicamento, quantidade)
        expected_output = 13
        assert farmacia.get_estoque()[medicamento] == str(expected_output)
    
    # medicamento não existente no estoque e quantidade válida
    def test_comprar_medicamento_novo(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'advil'
        quantidade = 5
        farmacia.comprar_medicamento(medicamento, quantidade)
        expected_output = 5
        assert farmacia.get_estoque()[medicamento] == str(expected_output)
        
    # quantidade de medicamento negativa (inválida)
    def test_vender_medicamento_quantidade_invalida(self, capsys):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'dipirona'
        quantidade = -5
        farmacia.vender_medicamento(medicamento, quantidade)
        captured = capsys.readouterr()
        expected_output = 'Quantidade inválida\n'
        assert captured.out == expected_output
    
    # comportamento adequado: medicamento existe no estoque e a quantidade solicitada é menor ou igual à disponível
    def test_vender_medicamento_existente_quantidade_valida(self):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'dipirona'
        quantidade = 3
        farmacia.vender_medicamento(medicamento, quantidade)
        expected_output = 7
        assert farmacia.get_estoque()[medicamento] == str(expected_output)
    
    # medicamento existe no estoque, mas quantidade solicitada é superior à disponível
    def test_vender_medicamento_existente_quantidade_superior(self, capsys):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'dipirona'
        quantidade = 12
        farmacia.vender_medicamento(medicamento, quantidade)
        captured = capsys.readouterr()
        expected_output = 'Quantidade solicitada superior à disponível no Estoque\n'
        assert captured.out == expected_output
    
    # medicamento inexiste no estoque, embora a quantidade solicitada seja válida
    def test_vender_medicamento_inexistente(self, capsys):
        farmacia = farm.FarmaciaVarejo(self.nome, self.endereco, self.estoque, self.quantidade_clientes, self.quantidade_funcionarios)
        medicamento = 'advil'
        quantidade = 5
        farmacia.vender_medicamento(medicamento, quantidade)
        captured = capsys.readouterr()
        expected_output = 'Medicamento inexistente no Estoque\n'
        assert captured.out == expected_output
    
    # testes dos atributos e métodos da classe FarmaciaPopular
    
    def test_get_desconto_medicamentos(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        assert farmacia.get_desconto_medicamentos() == {chave.lower(): valor.lower() for chave, valor in self.desconto_medicamentos.items()}

    # informa valores positivos para as chaves de desconto_medicamento
    def test_set_desconto_medicamentos_positivo(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal) 
        novo_desconto_medicamentos = { 
            'dipirona' : '0.25', 
            'Ibuprofeno' : '0.1', 
            'paracetamol' : '0.7' 
            }
        farmacia.set_desconto_medicamentos(novo_desconto_medicamentos)
        assert farmacia.get_desconto_medicamentos() == {chave.lower(): valor.lower() for chave, valor in novo_desconto_medicamentos.items()}
    
    # informa valores negativos para as chaves de desconto_medicamento
    def test_set_desconto_medicamentos_negativo(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal) 
        novo_desconto_medicamentos = { 
            'dipirona' : '-0.25', 
            'Ibuprofeno' : '0.1', 
            'paracetamol' : '0.7' 
            }
        farmacia.set_desconto_medicamentos(novo_desconto_medicamentos)
        assert farmacia.get_desconto_medicamentos() == {chave.lower(): valor.lower() for chave, valor in self.desconto_medicamentos.items()}

    def test_get_faturamento_mensal(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        assert farmacia.get_faturamento_mensal() == {chave.lower(): valor.lower() for chave, valor in self.faturamento_mensal.items()}

    def test_set_faturamento_mensal(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal) 
        novo_faturamento_mensal = { 
            'janeiro' : '2000.00', 
            'fevereiro' : '0.0', 
            'março' : '-100.00' 
            }
        farmacia.set_faturamento_mensal(novo_faturamento_mensal)
        assert farmacia.get_faturamento_mensal() == {chave.lower(): valor.lower() for chave, valor in novo_faturamento_mensal.items()}
    
    # medicamento existe no estoque e possui desconto previsto
    def test_aplicar_desconto_medicamento_existente_estoque(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        medicamento = 'dipirona'
        desconto = 0.12
        assert farmacia.aplicar_desconto(medicamento) == desconto
    
    # medicamento não existe no estoque, embora possua desconto previsto
    def test_aplicar_desconto_medicamento_estoque_inexistente(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        medicamento = 'losartana'
        desconto = 0.0
        assert farmacia.aplicar_desconto(medicamento) == desconto
    
    # medicamento existe no estoque, mas não possui desconto previsto
    def test_aplicar_desconto_inexistentes(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        medicamento = 'aspirina'
        desconto = 0.0
        assert farmacia.aplicar_desconto(medicamento) == desconto
    
    # medicamento não existe no estoque nem possui desconto previsto
    def test_aplicar_desconto_medicamento_e_desconto_inexistentes(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        medicamento = 'advil'
        desconto = 0.0
        assert farmacia.aplicar_desconto(medicamento) == desconto
    
    # o dicionário faturamento_mensal não possui quaisquer chaves e valores 
    def test_calcular_faturamento_anual_vazio(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        novo_faturamento_mensal = {}
        farmacia.set_faturamento_mensal(novo_faturamento_mensal)
        assert farmacia.calcular_faturamento_anual() == 0.0

    # o dicionário faturamento_mensal possui todas os valores iguais a 0.0 (zero)
    def test_calcular_faturamento_anual_faturamento_mensal_zero(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        novo_faturamento_mensal = {
            'janeiro' : '0.00', 
            'fevereiro' : '0.0', 
            'março' : '0.00'
            }
        farmacia.set_faturamento_mensal(novo_faturamento_mensal)
        assert farmacia.calcular_faturamento_anual() == 0.0
    
    # o dicionário faturamento_mensal possui valores variados (inclusive negativos)
    def test_calcular_faturamento_anual_com_dados(self):
        farmacia = farm.FarmaciaPopular(self.nome, self.endereco, self.estoque, self.desconto_medicamentos, self.faturamento_mensal)
        faturamento_mensal = 1900.0
        assert farmacia.calcular_faturamento_anual() == faturamento_mensal
