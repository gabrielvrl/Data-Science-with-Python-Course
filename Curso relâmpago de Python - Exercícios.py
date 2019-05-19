#!/usr/bin/env python
# coding: utf-8

# # Curso relâmpago de Python - Exercícios
# 
# Este é um exercício opcional para testar sua compreensão sobre o Python Basics. Se você achar isso extremamente desafiador, então você provavelmente ainda não está pronto para o resto deste curso e não tem experiência de programação suficiente para continuar. Eu sugiro que você faça outro curso mais orientado para iniciantes, como [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercícios
# 
# Responda as perguntas ou complete as tarefas descritas em negrito abaixo, use o método específico, se aplicável.

# ** Quanto é 7 elevado na potência 4?**

# In[ ]:





# In[1]:


7**4


# ** Quebre a seguinte string em uma lista:**
# 
#     s = "Olá, Pai!"

# In[2]:


s = 'Olá, Pai!'


# In[3]:


s.split()


# In[ ]:





# In[2]:





# ** Dada as variáveis:**
# 
#     Planeta = "Terra"
#     Diametro = 12742
# 
# ** Use .format() para printar a seguinte frase: **
# 
#     O diâmetro da terra é de 12742 kilômetros.

# In[ ]:





# In[ ]:





# In[5]:


planeta = "Terra"
diametro = 12742


# In[7]:


print('O diâmetro da {one} é de {two} kilômetros'.format(one=planeta,two=diametro))


# In[1]:





# ** Dada a lista abaixo, use indexação para obter apenas a string "ola". **

# In[13]:


lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]


# In[14]:


lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]


# In[15]:


print(lst[3][1][2])


# In[3]:





# ** Dado o seguinte dicionário aninhado, extraia a palavra "hello" **

# In[6]:


d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}


# In[15]:


d['k1'][3]['café'][3]['alvo'][3]


# In[5]:





# ** Qual a principal diferença entre um dicionário e uma tupla? **

# In[3]:


O dicionário é uma lista com valores atribuidos a uma variável, a tupla é uma lista imutável.


# ** Construa uma função que retire o domínio dado um e-mail no seguinte formato: **
# 
#     user@domain.com
#     
# **Por exemplo, passando como parâmetro "user@domain.com" retornaria: domain.com**

# In[20]:


def obterDominio(email):
    print(email.split('@')[-1])


# In[ ]:





# In[26]:


obterDominio('user@domain.com')


# ** Crie uma função básica que retorna True se a palavra 'dog' estiver contida na string de entrada. Não se preocupe com os casos de extremos, como uma pontuação que está sendo anexada à palavra cão, mas que seja senível à caixa. **

# In[33]:


def encontreCachorro(string):
    return 'cachorro' in string.lower()


# In[34]:


encontreCachorro('Existe um cachorro aí?')


# ** Crie uma função que conta o número de vezes que a palavra "dog" ocorre em uma string. Novamente ignore os casos extremos. **

# In[30]:


def contaCachorro (frase): return frase.lower().count("cachorro")


# In[31]:


contaCachorro('Esse cachorro é mais rápido que o outro cachorro.')


# ** Use expressões lambda e a função filter () para filtrar as palavras de uma lista que não começa com a letra 's'. Por exemplo: **
# 
#     seq = ['sopa','cachorro','salada','gato','ótimo']
# 
# ** Deveria ser filtrado para:**
# 
#     ['sopa','salada']

# In[7]:


seq = ['sopa','cachorro','salada','gato','ótimo']


# In[8]:





# ### Problema final
# ** Você está dirigindo um pouco rápido demais, e um policial para você. Escreva uma função para retornar um dos 3 resultados possíveis: "Sem multa", "Pequena multa" ou "Multa Grande".
#    Se a sua velocidade for igual ou inferior a 60, o resultado é "Sem multa". Se a velocidade for entre 61 e 80 inclusive, o resultado é "Multa Pequena". Se a velocidade é de 81 ou mais, o resultado é "Multa Grande". A menos que seja seu aniversário (codificado como um valor booleano nos parâmetros da função) - em seu aniversário, sua velocidade pode ser 5 maior em todos os casos. **

# In[10]:


def capturar_velocidade(speed, is_birthday):
    pass


# 

# In[11]:


capturar_velocidade(65,False)


# In[12]:


capturar_velocidade(81,False)

