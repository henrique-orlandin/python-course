# 7 – Parcelar uma compra com 16% de acréscimo.
# Escreva um algoritmo que receba o valor de um produto, acrescente 16% a esse valor, divida em 10 parcelas e mostre para o usuário o valor da parcela e o valor total da compra.

product_price = 50
addition_rate = 16 # percentage
new_price = product_price + (product_price * addition_rate / 100)
number_of_installments = 10
installments = new_price / number_of_installments

print(f"Installments: R${installments:.2f}")
print(f"Total price: R${new_price:.2f}")