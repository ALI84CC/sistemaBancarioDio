'''
SISTEMA BANCARIO DIO 

DIGITE A OPÇÂO DESEJADA :

[1]  DEPOSITAR

[2]  SACAR

[3] EXTRATO

[4] Sair

'''
saldo = 100 
limite = 500
extrato = ""
numero_saques = 0
limite_saque=3

while  True:

   operacao = int(input("informe a operação de 1 a 4:"))

   if operacao == 1:
      valor = float(input("informe o valor para deposito:"))

      if valor > 0:
         saldo =  valor + saldo
         print(f"valor depositado foi R$:{valor: .2f} e com saldo atual R$:{saldo: .2f}")
         extrato += f"Você realizou um deposito de R${valor:.2f}"
      else:
          print("Operação falhou! O valor informado é inválido.")
   elif operacao == 2:
       saque = float(input(f"informe o valor a sacar:"))

       if(numero_saques <= 3 and saldo > saque and limite > saque): 
         saldo -= saque
         print(f'o último saque foi de R${saque: .2f} e seu saldo R${saldo: .2f}')
         limite_saque -= 1
         print('limites para saque:{limite_saque}')
         extrato += f"Você realizou um saque de R${saque:.2f}"
         if saldo > 0:
            print("transação aprovada!")
         else:
            print("transação negada!")
       else:
            print("Operação falhou! O valor informado é inválido.")      
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