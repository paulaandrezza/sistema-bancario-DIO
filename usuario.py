from datetime import datetime

LIMIT_WITHDRAWALS = 3

class User:
  def __init__(self, name, password):
    self.name = name
    self.password = password
    self.balance = 0
    self.extract = {}
    self.daily_withdrawals = 0
    
  def deposito(self):
    value = float(input("Informe o valor a ser depositado: R$ "))
    if value <= 0:
      return "O valor informado não é válido. Insira um valor positivo maior do que 0."
    self.balance += value
    self.extract[datetime.now()] = value
    return f"Depósito realizado com sucesso no valor de R$ {value:.2f}"
    
  def saque(self):
    value = float(input("Informe o valor a ser retirado: R$ "))
    if self.daily_withdrawals >= LIMIT_WITHDRAWALS:
      return "Você atingiu o limite diário de saques."
    elif value >= 500:
      return "O valor informado não é válido. Insira somente valores abaixo de R$ 500,00."
    elif self.balance < value:
      return "Saldo insuficiente."
    
    self.balance -= value
    self.daily_withdrawals += 1
    self.extract[datetime.now()] = value * -1
    return f"Saque realizado com sucesso no valor de R$ {value:.2f}"
    
  def extrato(self):
    fstring = ""
    for k,v in self.extract.items():
      fstring += "{:<30}{:>20}\n".format(str(k),v)
    
    fstring += "{:<30}{:>20}\n".format("Saldo", self.balance)       
    fstring += "{:<30}{:>20}\n".format("Saques diários restantes", LIMIT_WITHDRAWALS - self.daily_withdrawals)       
      
    return fstring