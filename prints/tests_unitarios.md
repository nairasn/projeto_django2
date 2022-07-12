# Test Unitário

### Teste Unitário na models. Onde se busca testar o retorno da String do models.

#

Utilizado o metodo SetUp para questão de comparação. Criado pessoa ficticia para fins de teste que roda antes de rodar o teste de fato.

É feito o teste para "pegar" com GET o cliente com tal nome.
e é solicitado através do codigo que retorne exatamente o que foi pedido. 
<br>
<br>
1 - Nesse caso, o código flui como esperado, já que as strings estão iguais e o test retorna OK
![test_unitario_ok](https://github.com/nairasn/projeto_django2/blob/main/prints/test_unitario_ok.png)
<br>
<br>
<br>
2 - Já nese print, foi feita uma modificação no código ('Niara' ou invés de 'Naira') afim de que o teste retornasse errado. 
assim o teste volta como FAILED, e aponta o erro. 
![test_unitario_erro](https://github.com/nairasn/projeto_django2/blob/main/prints/test_unitario_erro.png)
