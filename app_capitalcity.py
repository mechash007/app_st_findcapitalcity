import streamlit as st

st.title("Ask the Expert – Capital Cities of the World 🌍")

# Dictionary to store country-capital pairs
capital_dict = {}

# Read data from file
def read_from_data_file():
    try:
        with open("capital_data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if "/" in line:
                    country, city = line.split("/")
                    capital_dict[country.lower()] = city
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open("capital_data.txt", "w").close()

# Write new data to file
def write_to_file(country, city):
    with open("capital_data.txt", "a") as file:
        file.write(f"\n{country}/{city}")

# Load existing data
read_from_data_file()

# User input
query_country = st.text_input("Type the name of the country:")

if query_country:
    query_country = query_country.lower()

    if query_country in capital_dict:
        capital = capital_dict[query_country]
        st.success(
            f"The capital city of **{query_country.capitalize()}** is **{capital}**!"
        )
    else:
        st.warning("I don't know the capital of this country 🤔")
        new_city = st.text_input(
            f"Teach me! What is the capital of {query_country.capitalize()}?"
        )

        if st.button("Save"):
            if new_city:
                capital_dict[query_country] = new_city
                write_to_file(query_country, new_city)
                st.success("Thanks! I've learned something new 🎉")
            else:
                st.error("Please enter a capital city.")
