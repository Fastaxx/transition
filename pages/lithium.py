import streamlit as st
import pandas as pd


def write():
	st.title("Lithium")
	elecbike = st.slider("",0,100,50, help="Valeur")
	st.write("Remplacement de", elecbike,"% du parc automobile par des vélos électriques")

	remplacement = 1400000000.0 * elecbike/100

	st.write("Nombre de voitures à remplacer = Nombre de vélos à construire = Nombre de batterie : ", remplacement)
	qte_lithium = 28*remplacement

	st.write("Quantité de lithium nécessaire :", qte_lithium*0.000001, "tonnes")
	data_batt = pd.read_csv('battcomp.csv', sep=';', index_col=0)
	df_comp = pd.DataFrame(data_batt)
	st.bar_chart(df_comp)
	
	st.caption("Hypothèses : 28g de lithium/batterie - 1400000000 de véhicules en circulation")