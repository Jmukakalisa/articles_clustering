import streamlit as st
import pandas as pd

# Load the clustered articles data
clustered_df = pd.read_csv('clustered_articles.csv')

# Streamlit webpage
st.title('Clustered News Articles')

# Display the clusters
clusters = clustered_df.groupby('prediction').apply(lambda x: x.to_dict(orient='records'))
for cluster_id, articles in clusters.items():
    st.header(f'Cluster {cluster_id}')
    for article in articles:
        st.subheader(article['heading'])
        st.write(f"[Read more]({article['link']})")