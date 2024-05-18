import random

def roll_dice():
   """
   Função que simula a rolagem de um dado.
   
   Retorna:
     Valor obtido na rolagem do dado.
   """
   return random.randint(1, 6)

def dice_spin_simulator():
   """
   Função que executa o giro de dados.
   """
   print("Bem-vindo ao Simulador de Giro de Dados!")
   
   while True:
      print("\nPressione Enter para girar o dado. Digite 'sair' para encerrar.")
      user_input = input()
      
      if user_input.lower() == "sair":
         print("Fim do Simulador de Giro de Dados!")
         break
      
      try:
         dice_value = roll_dice()
         print(f"O dado girou e você tirou um {dice_value}!")
      except ValueError:
         print("Erro: Valor inválido. Por favor, insira um valor numérico.")

# Executar o simulador
dice_spin_simulator()