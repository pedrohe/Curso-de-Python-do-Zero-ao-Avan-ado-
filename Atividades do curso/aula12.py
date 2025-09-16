#Segundo exercício do curso; Objetivos: aálculo de IMC e classificação + ellipsis.
#Comece abaixo:
nome = 'Pedro'
sobrenome = 'Cordeiro'
nome_completo = nome + ' ' + sobrenome
idade = 21
ano_de_nascimento = 2025 - idade
peso = 83.5 #em kg
altura_metros = 1.75 #em metros
imc = ...

#Isso acima é a chamada "ellipsis", que indica que algo foi omitido ou que há mais informações a serem consideradas.
#As elipssis ao serem executadas no Python, retornam o valor "Ellipsis", n gerando erro.

imc = peso / altura_metros **2

print( 'Nome:',nome_completo, end='\n')
print( 'Idade:',idade, end='\n')
print( 'Data de nascimento:',ano_de_nascimento, end='\n')
print( nome,'tem', altura_metros,'m de altura e pesa', peso, 'kg', end='\n')
print( 'Índice de Massa Corporal (IMC):', imc, end='\n')

#Para arredondar o IMC para duas casas decimais, podemos usar a função round().
imc = round(imc, 2)
print( 'IMC arredondado:', imc, end='\n')


#Dessa forma, podemos calcular o IMC e exibir o resultado, através de uma série de prints.
#Obrigado por acompanhar até aqui! :)