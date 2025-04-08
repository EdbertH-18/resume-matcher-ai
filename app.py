import streamlit as st
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util
from huggingface_hub import login
import os

# token
login(token=os.environ.get("HF_TOKEN"))

# -- Page config
st.set_page_config(page_title="LLM-Powered HR Filter", layout="wide")
st.title("LLM-Powered HR Filter")
st.markdown("Helps HR and recruiters find the most relevant candidates based on job descriptions.")

# -- Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("AI_Resume_Screening.csv")
    df = df[['Name', 'Skills']]
    return df

df = load_data()

# Optional Raw Data Preview
with st.expander("📂 Preview Resume Dataset", expanded=False):
    st.dataframe(df)

# -- Load model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# -- Embed all resumes
@st.cache_resource
def embed_resumes(texts):
    return model.encode(texts, convert_to_tensor=True)

resume_texts = df["Skills"].tolist()
resume_embeddings = embed_resumes(resume_texts)

# -- UI Input
user_input = st.text_area("📄 Paste the job description here:", height=100)

if user_input:
    user_vector = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(user_vector, resume_embeddings)[0].flatten()

    # Top 5 and Bottom 5
    top_indices = torch.topk(similarities, 5).indices.cpu().numpy()
    bottom_indices = torch.topk(similarities, 5, largest=False).indices.cpu().numpy()

    top_df = df.iloc[top_indices].copy()
    bottom_df = df.iloc[bottom_indices].copy()
    top_df["Similarity"] = similarities[top_indices].cpu().numpy()
    bottom_df["Similarity"] = similarities[bottom_indices].cpu().numpy()

    def get_match_label(score):
        if score >= 0.75:
            return "🟢 Excellent Match"
        elif score >= 0.6:
            return "🟡 Good Match"
        elif score >= 0.45:
            return "🟠 Fair Match"
        else:
            return "🔴 Weak Match"

    st.write("🔢 **Score Range for this Query:**")
    st.write(f"Max: {similarities.max():.2f} | Min: {similarities.min():.2f}")

    # --- Show Top 5 Results
    st.markdown("Top 5 Matching Resumes")

    for i, row in top_df.iterrows():
        label = get_match_label(row["Similarity"])
        with st.expander(f"👤 {row.get('Name', 'Candidate')} | {label} | Score: {row['Similarity']:.2f}"):
            st.markdown(f"""
            **🛠️ Skills:** {row.get('Skills', 'N/A')}  
            """)