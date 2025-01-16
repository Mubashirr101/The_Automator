import streamlit as st
import pandas as pd
from pprint import pprint
import io

# Example dictionary
data = {
    "name": "John",
    "age": 25,
    "skills": {"Python": "Intermediate", "R": "Beginner"},
}
# Example dictionary
data = {"name": "John", "age": 25, "skills": ["Python", "R", "SQL"]}

# Display dictionary
st.write(data)

# Example dictionary
data = {"name": "John", "age": 25, "skills": ["Python", "R", "SQL"]}

# Display dictionary as code
st.code(f"{data}", language="python")

# Example dictionary
data = {
    "name": "John",
    "age": 25,
    "skills": {"Python": "Intermediate", "R": "Beginner"},
}

# Pretty print dictionary
buffer = io.StringIO()
pprint(data, stream=buffer)
st.text(buffer.getvalue())

# Display dictionary as JSON
st.json(data)
# Example dictionary
data = {"name": ["John", "Jane"], "age": [25, 30], "skills": ["Python", "SQL"]}

# Convert to DataFrame and display
df = pd.DataFrame(data)
st.dataframe(df)
