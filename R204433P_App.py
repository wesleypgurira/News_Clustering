import streamlit as st
import pandas as pd
import pickle

# Loading my pre-trained clustering model
def load_clustering_model():
    with open('kmeans_model.pkl', 'rb') as f:
        km = pickle.load(f)
    return km

# Loading my combined DataFrame from pickle file
def load_combined_data():
    combined_df = pd.read_pickle('combined_data.pkl')
    return combined_df

# Streamlit app function (for running the app)
def main():
    st.markdown("Assignment 4: R204433P Gurira Wesley Panashe HAI")

    st.title("News Article Clustering")

    # Loading pre-trained clustering model
    km = load_clustering_model()

    # Loading combined DataFrame from pickle file
    data = load_combined_data()

    # Assigning cluster labels to DataFrame
    data['Cluster'] = km.labels_

    # Displaying clusters and related stories
    unique_clusters = data['Cluster'].unique()

    selected_cluster = st.sidebar.selectbox("Select a Cluster", unique_clusters)

    st.header(f"Cluster {selected_cluster}")

    cluster_articles = data[data['Cluster'] == selected_cluster]

    for idx, row in cluster_articles.iterrows():
        st.markdown(f"**Title:** {row['Title']}")
        st.markdown(f"**Category:** {row['Category']}")
        st.markdown(f"**Source:** {row['Source']}")
        st.markdown(f"**URL:** {row['Link']}")
        st.markdown("---")

# Running the app
if __name__ == "__main__":
    main()
