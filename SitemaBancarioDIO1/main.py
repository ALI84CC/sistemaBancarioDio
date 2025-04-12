
'''
[1] DEPOSITAR

[2]  SACAR

[3] EXTRATO

[4] SAIR

'''
from datetime import date
 
saldo = 1000 
limite = 500
extrato = ""
numero_saques = 0
limite_saque=3
transacao = 10
valor_sacado = 0
while  True:

   operacao = int(input("informe a operação de 1 a 4:"))

   if operacao == 1:
      valor = float(input("informe o valor para deposito:"))

      if valor > 0:
         saldo =  valor + saldo
         print(f"valor depositado foi R$:{valor: .2f} e com saldo atual R$:{saldo: .2f}")
         extrato += f"Você realizou um deposito de R${valor:.2f}"
         transacao -= 1
         data_atual = date.today()
         data_local = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
         print(f" Depositado em: {data_local}")
      else:
          print("Operação falhou! O valor informado é inválido.")
   elif operacao == 2:
       saque = float(input(f"informe o valor a sacar:"))

       if(numero_saques <= limite_saque):
         if(limite > saque) :
          valor_sacado = limite - saque
          limite_saque = numero_saques - limite_saque
          data_atual = date.today()
          data_local = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
       else:
          print("valor do saque superior ao limite")
       if(transacao < 10):
          transacao -= 1 
          
       print(f'Seu último saque foi de R${valor_sacado: .2f},seu saldo total é de R${saldo: .2f}')
       print(f" Depositado em: {data_local}")
       print(f"Caro Cliente você possui ${limite_saque}")
       
       extrato = f"Você realizou um saque de R${saque:.2f}"
       
   elif operacao == 3:
      print('--------Bem-vindo ao seu extrato------')
      print('-----Aqui estão as informações do dia------')
      print('----Seu saldo disponível R$: ', saldo)
      print('----Limite disponivel R$:', limite)
      if extrato != "" :
         print(f'----O Ultimo deposito foi R$:{valor: .2f}')
      else:
         print("Não forma realizadas movimentações!!") 
   elif operacao == 4:
      break
   else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")