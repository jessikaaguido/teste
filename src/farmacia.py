from abc import ABC

class Farmacia(ABC):
    def __init__(self, nome, endereco, estoque):
        # conforme lista de requisitos, todos os atributos da classe Farmacia são armaznados em Lower Case.
        self._nome = nome.lower()
        self._endereco = {chave.lower(): valor.lower() for chave, valor in endereco.items()}
        self._estoque = {chave.lower(): valor.lower() for chave, valor in estoque.items()}

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome.lower()
    
    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, endereco):
        # compressão de dicionário
        endereco_lower = {chave.lower(): valor.lower() for chave, valor in endereco.items()}
        self._endereco = endereco_lower

    def get_estoque(self):
        return self._estoque
    
    def set_estoque(self, estoque):
        # compressão de dicionário
        estoque_lower = {chave.lower(): valor.lower() for chave, valor in estoque.items()}
        self._estoque = estoque_lower
    
    def exibir_informacoes_cadastrais(self):
        # Verifica se o atributo nome é vazio ('') ou se pelo menos um valor no dicionário endereco é vazio ('')
        if not self._nome or any(not values for values in self._endereco.values()):
            print("Cadastro incompleto ou inválido")
        else:
            endereco_str = ', '.join([f'{chave}: {valor}' for chave, valor in self._endereco.items()])
            print(f'Nome: {self._nome}\nEndereço: {endereco_str}')
    
    def exibir_estoque(self):
        print("Estoque:")
        for produto, quantidade in self._estoque.items():
            print(f"{produto}: {quantidade} unidade(s)")


class FarmaciaVarejo(Farmacia):
    def __init__(self, nome, endereco, estoque, quantidade_clientes, quantidade_funcionarios):
        super().__init__(nome, endereco, estoque)
        self._quantidade_clientes = quantidade_clientes
        self._quantidade_funcionarios = quantidade_funcionarios
        #self._faturamento_mensal = {}

    def get_quantidade_clientes(self):
        return self._quantidade_clientes

    def set_quantidade_clientes(self, quantidade_clientes):
        if quantidade_clientes > 0:
            self._quantidade_clientes = quantidade_clientes
    
    def get_quantidade_funcionarios(self):
        return self._quantidade_funcionarios

    def set_quantidade_funcionarios(self, quantidade_funcionarios):
        if quantidade_funcionarios > 0:
            self._quantidade_funcionarios = quantidade_funcionarios
    
    def comprar_medicamento(self, medicamento, quantidade):
        # quantidade inválida?
        if quantidade <= 0:
            print('Quantidade inválida')
        
        # medicamento existente no estoque e quantidade válida
        elif medicamento in self._estoque:
            quantidade_estoque = int(self._estoque[medicamento])
            quantidade_estoque += quantidade
            self._estoque[medicamento] = str(quantidade_estoque)
        
        # medicamento não existente no estoque: cria nova entrada
        else:
            self._estoque[medicamento] = str(quantidade)
    
    def vender_medicamento(self, medicamento, quantidade):
        # quantidade inválida?
        if quantidade <= 0:
            print('Quantidade inválida')
                
        # medicamento existente no estoque
        elif medicamento in self._estoque:
            # a quantidade solicitada é menor que ou igual à disponível?
            if quantidade <= int(self._estoque[medicamento]):
                quantidade_estoque = int(self._estoque[medicamento])
                quantidade_estoque -= quantidade
                self._estoque[medicamento] = str(quantidade_estoque)
            
            # quantidade solicitada superior à disponível
            else:
                print('Quantidade solicitada superior à disponível no Estoque')
        
        # medicamento não existente no estoque
        else:
            print('Medicamento inexistente no Estoque')


class FarmaciaPopular(Farmacia):
    def __init__(self, nome, endereco, estoque, desconto_medicamentos, faturamento_mensal):
        super().__init__(nome, endereco, estoque)
        self._desconto_medicamentos = desconto_medicamentos
        self._faturamento_mensal = faturamento_mensal

    def get_desconto_medicamentos(self):
        return self._desconto_medicamentos
    
    def set_desconto_medicamentos(self, desconto_medicamentos):
        if all(float(valor) >= 0 for valor in desconto_medicamentos.values()):
            desconto_medicamentos_lower = {chave.lower(): valor for chave, valor in desconto_medicamentos.items()}
            self._desconto_medicamentos = desconto_medicamentos_lower
    
    def get_faturamento_mensal(self):
        return self._faturamento_mensal

    def set_faturamento_mensal(self, faturamento_mensal):
       # compressão de dicionário
       faturamento_mensal_lower = {chave.lower(): valor.lower() for chave, valor in faturamento_mensal.items()}
       self._faturamento_mensal = faturamento_mensal_lower
       
    def aplicar_desconto(self, medicamento):
        desconto = 0.0
        if medicamento in self._estoque and medicamento in self._desconto_medicamentos:
            desconto = float(self._desconto_medicamentos[medicamento])
            #return desconto
        return desconto
    
    def calcular_faturamento_anual(self):
        if not self._faturamento_mensal:
            return 0.0
        
        total_faturamento = sum(float(valor) for valor in self._faturamento_mensal.values())
        return total_faturamento