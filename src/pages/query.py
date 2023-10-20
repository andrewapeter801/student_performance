from pathlib import Path
import streamlit as st
import sys 
import os

sys.path.insert(0, os.path.join(Path(__file__).parents[1]))

from to_mongo import ToMongo

c = ToMongo()

st.header('Query Page')
st.write('''
         This page will search our database for any field you input! 
         
         Spelling of that name MUST BE EXACT!')
         '''
)

# Now we query the database
# Is to return information about a card from our database to a user in a friendly format
# Query the database off a user input, then display that info back to them!

# How can I use this in the future?
# When a user wants to query(or search) your database for information, we don't have to reference a local file anymore.
# We can plug and play a database and dashboards, knowing how to allow a user to retrieve and view information is a powerful tool

# When we build applications and dash

try:
    answer = st.text_input('Enter a column name:', value = '')
    st.write(list(c.cards.find({'name': answer})))
except:
    st.error('There was an issue with retrieving your card name input. Please double check that the spelling is exact!')