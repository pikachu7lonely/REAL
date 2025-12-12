from capaLogica.lPersona import LP
import streamlit as st

class PPersona:
    def __init__(self):
        self.lPersona = LP()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title('BIENVENIDO')
        with st.form('FormularioRegistro'):
            txtDocIdentidad = st.text_input('Documento Identidad')
            txtNombre = st.text_input('Nombre')
            txtEdad = st.number_input('Edad')
            btnGuardar = st.form_submit_button('Guardar', type= 'primary')

            if btnGuardar:
                persona = {
                    'docIdentidad' : txtDocIdentidad,
                    'nombre': txtNombre,
                    'edad': txtEdad
                }
                self.insertarPersona(persona)
        self.mostrarPersona

    def mostrarPersona(self):
        listaPersona = self.lPersona.mostrarPersona()
        st.dataframe(listaPersona)

    def insertarPersona(self, persona: dict):
        self.lPersona.insertarPersona(persona)
        st.toast('Registro guardado correctamente', icon= '😶‍🌫️', duration='short')

