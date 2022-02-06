import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
import random 
import numpy as np

def write():
	st.title("Remplacement Voiture -> VAE")
	elecbike = st.slider("Selectionner le pourcentage du parc automobile à remplacer par des VAE",0,100,50, help="Valeur")
	st.write("### Remplacement de", elecbike,"% du parc automobile par des VAE")

	remplacement = 1400000000.0 * elecbike/100

	st.write("Nombre de voitures à remplacer :", int(remplacement))

	st.markdown("""### Composition batterie """)
	data_batt = pd.read_csv('battcomp.csv', sep=';', index_col=0)
	data_comp = pd.read_csv('comp.csv', sep=';', index_col=0)
	name = data_batt.columns
	cmap = plt.get_cmap('bwr')
	outer_colors = cmap(np.arange(11)*20)
	fig1, ax1 = plt.subplots()
	ax1.pie(data_comp['Values'], labels=name, pctdistance= 0.8, startangle=90,colors=outer_colors, autopct='%1.1f%%')
	ax1.axis('equal')
	st.pyplot(fig1)

	for i in data_comp.index:
		st.write("Quantité de",i,"nécessaire :", int(2500*data_batt.iloc[0][i]*0.000001*remplacement), "tonnes")
	
	st.caption("Hypothèses : 50g de lithium/batterie - 1400000000 de véhicules en circulation")