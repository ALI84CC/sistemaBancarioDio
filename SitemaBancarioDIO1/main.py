'''
SISTEMA BANCARIO DIO 

DIGITE A OPÇÂO DESEJADA :

[1]  DEPOSITAR

[2]  SACAR

[3] EXTRATO

[4] Sair

'''
saldo = 0 
limite = 500
extrato = ""


while  True:

   operacao = int(input("informe a operação de 1 a 4:"))

   if operacao == 1:
      valor = float(input("informe o valor para deposito:"))

      if valor > 0:
         saldo =  valor + saldo

         extrato += f"Você realizou um deposito de R${valor:.2f}"
      else:
          print("Operação falhou! O valor informado é inválido.")
   elif operacao == 2:
      