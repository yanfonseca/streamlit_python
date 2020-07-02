# terminal commands
# streamlit --help
# streamlit run app.py

import streamlit as st

#Text
st.title('Esse é um título')
st.header('Primeiro header')
st.subheader('Sub header')
num = 1
st.text('Hello world==>' + str(num))
st.markdown('# Usando markdown.==>' + str(num))

#Text with color
st.success('Você conseguiu!')
st.info('Aqui tem uma informação!')
st.warning('Aqui tem uma aviso!')
st.error('Aqui tem um erro!')
st.exception("MeuPrimeiroErro('Digite corretamente da próxima vez.')")

#Access documentation, it is like ?functionname
st.help(st)

#Write text and it shows variables
st.write('Também é um texto, usando a função write.')
st.write(range(0,10))
st.write(*range(0,10))

#Python Imaging Library
from PIL import Image
img = Image.open('imagem.png')
st.image(img, width = 700, caption="Uma imagem foi adicionada")

#Run Videos
#video = open('video.mp4','rb')
#st.video(video)

#Audio
#audio = open('audio.mp3','rb').read()
#st.audio(audio, format='audio/mp3')

#Widgets
#Checkbot('show/hide)
if st.checkbox('show/hide'):
    st.text('Mostra ou esconde')

else:
    print('Print no temrinal')

#Radio
saude =st.radio('Como vai sua saúde?',('otima','ruim','normal'))

if saude == 'otima':
    st.success('Você está bem.')
elif saude =='normal':
    st.success('Está normal.')

else:
    st.info('Sua saúde está ruim.')

#SelectBox
ocupacao = st.selectbox('o que você faz da vida?',('','jogador de futebol','engenheiro','data scientist'))
st.write(f'Então você é ' + ocupacao)

#Multiselect
local = st.multiselect('Onde você mora?',('Rio de Janeiro','New York', 'São Paulo', 'Brasilia'))
st.success('trabalha em ' + str(local))

#Slider
age = st.slider('Quantos anos você tem?',1 ,10)

#Button
st.button('Um botão') # Não faz nada

if st.button('Clique aqui, por favor'):
    st.text('Voce apertou o botão')

#Text input
name = st.text_input("Qual é o seu nome completo?", 'Digite aqui:')
idade = st.text_input('Qual é a sua idade?', 'Digite aqui:')

if st.button('clicou - mostra mensagem'):
    resultado = name.title()
    st.success(resultado)

#Number input
number = st.number_input('Digite um número, por favor: ')

#Text area
mensagemlonga = st.text_area('Digite abaixo: ', 'Digite aqui')

if st.button('clicou2'):
    resultado = mensagemlonga.title()
    st.success(resultado)

# Date input
import datetime
hoje = st.date_input('Hoje é dia, ', datetime.datetime.now())

#time
time = st.time_input('A hora é, ', datetime.time())

#Display JSON
st.text('Mostra json')
st.json({'nome':'seunome','sexo':'seusexo'})

#Display raw code
st.text('Mostra linha de código')
st.code('import streamlit as st \nimport pandas as pd')

#Display bar code
with st.echo():
    #posso adicionar comentários
    import pandas as pd 
    dataframe = pd.DataFrame()

#Display Bar
import time 
barra = st.progress(0)
for i in range(50):
    barra.progress(i + 1)

#Spinner
with st.spinner('Aguardando...'):
    time.sleep(5)
st.success('Acabou')

# Ballon
# Print balloons
#st.balloons()

#Sidebar
st.sidebar.header('Sobre')
st.sidebar.text('Posso escrever na barra ao lado')

st.sidebar.header('Sobre2')
st.sidebar.text('Posso escrever na barra ao lado')

st.sidebar.multiselect('Escolha opção: ',('opção1','opção2','opção3'))

#Function
@st.cache #Para rodar mais rápido
def run():
    return range(100)
st.write(run())


#Tables
months = ['Jan','Apr','Mar','June'] * 10
days = [31,30,31,30] * 10
dic = {'months':months, 'days':days}
st.table(pd.DataFrame(dic))

#Dataframe

import pandas as pd
dados = ['nome', 'cidade', 'bairro', 'idade']
pessoa = ['john','RJ', 'Flamengo', 64]

lista = list(zip(dados, pessoa))
df = pd.DataFrame(lista)
st.write(df)

#Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = np.sin(x)

plt.plot(x, y)
st.pyplot()
