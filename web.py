import streamlit as st
import csv
import random
import json
import numpy as np
from streamlit_extras.colored_header import colored_header

entries = []
with open('csps.json', 'r') as file:
    for line in file:
        entries.append(json.loads(line))
dontuse = True
while(dontuse):
    entry = random.choice(entries)
    if len(entry['gun']) >= 1:
        continue
    else:
        dontuse = False
        
colored_header(
    label="Proyecto de Traducción",
    description="Traduce una oración de español a Guna",
    color_name='red-70'
)
st.header("Proyecto de Traducción")

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i
    
def set_state2(i, trad):
    file = open('buffer.txt',"w")
    file.truncate(0)
    file.write(trad)
    file.close()
    st.session_state.stage =i

if st.session_state.stage == 0:
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        st.button('Traduce una oración', on_click=set_state, args=[1])

if st.session_state.stage == 1:
    st.write("La oración a traducir es: ")
    st.subheader(f"{entry['spa']}")
    trad = st.text_input('Tu traducción en Guna')
    st.button('Enviar', on_click=set_state2, args=[2, trad])
    st.write("Dale clic al botón para mandar tu traducción")

if st.session_state.stage >= 2:
    trad = open('buffer.txt').read()
    st.write(f"Tu traducción es: {trad}. Esta traducción es correcta?")
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        st.button('Sí', on_click=set_state, args=[3])
        st.button('No', on_click=set_state, args=[1])
    

if st.session_state.stage >= 3:
    st.write(f':{"red"}[¡Muchas gracias por tu contribución!]')
    entry['gun'].append(trad)
    with open('csps.json', 'a') as file:
        json.dump(entry, file)
        file.write('\n')
    file.close()
    st.button('Traduce otra oración', on_click=set_state, args=[0])