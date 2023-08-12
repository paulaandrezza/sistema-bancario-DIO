import os
from getpass import getpass
from time import sleep

from usuario import User


def clear():
  def screen_clear():
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')
          
  sleep(0.1)
  screen_clear()
  
def enter():
  input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
  
def invalid_option():
  print("Opção Inválida!")
  enter()
  clear()
  
def title(text):
  print(50 * "\033[1;34m*\033[0m")
  print(f"\033[1;34m***  {text: ^40}  ***\033[0m")
  print(50 * "\033[1;34m*\033[0m")
  
def menu():
  title("Menu principal")
  print("\033[1m1.\033[0m Novo usuário\n\033[1m2.\033[0m Acessar\n\033[1m0.\033[0m Sair")
  select = int(input("\033[34mSelecione uma opção: \033[0m"))
  if 0 < select > 2:
    invalid_option()
    select = menu()
  return select

def sub_menu():
  title("Menu de opções")
  print("\033[1m1.\033[0m Depósito\n\033[1m2.\033[0m Saque\n\033[1m3.\033[0m Extrato\n\033[1m0.\033[0m Voltar ao menu anterior")
  select = int(input("\033[34mSelecione uma opção: \033[0m"))
  if 0 < select > 3:
    invalid_option()
    select = sub_menu()
  return select


if __name__ == "__main__":
  title("Bem-vindo(a) ao DIObank")
  enter()
  clear()
  users = []
  
  option = menu()
  while option != 0:
    if option == 1:
      name = input("Informe o nome do usuário: ")
      password = getpass("Informe a senha: ")
      users.append(User(name, password))
      print("Usuário cadastrado com sucesso!")
      enter()
      clear()
    elif option == 2:
      user_name = input("Informe o nome do usuário: ")
      user_password = getpass("Informe a senha: ")
      
      found_user = None
      for user in users:
        if user.name == user_name and user.password == user_password:
          found_user = user
          break
      
      if found_user:
        clear()
        sub_option = sub_menu()
        while sub_option != 0:
          clear()
          if sub_option == 1:
            title("Depósito")
            print(found_user.deposito())
          elif sub_option == 2:
            title("Saque")
            print(found_user.saque())
          elif sub_option == 3:
            title("Extrato")
            print(found_user.extrato())
          
          enter()
          clear()
          sub_option = sub_menu()
        
      else:
        print("Usuário e/ou senha inválidos!")
        enter()
        clear()
          
    option = menu()
      
