import streamlit as st
import pages.lithium
import ressources.ast as ast
import pandas as pd

PAGES = {
	"Remplacement Voiture -> VAE": pages.lithium
}

def main():
	st.sidebar.title("Navigation")
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))
	page = PAGES[selection]
	with st.spinner(f"Loading {selection} ..."):
		ast.write_page(page)



if __name__ == "__main__":
	main()