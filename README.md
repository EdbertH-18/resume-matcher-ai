# LLM-Powered HR Filter

> 📌 Project 1 of 5 in my AI Portfolio Series
> I'm building real-world AI tools to deepen my knowledge of NLP, ML, and GenAI product development.

---

## 🔍 What It Does
This is a semantic resume matcher.
It lets HR or recruiters paste a job description, and returns the **top 5 most relevant candidates** using LLM-based sentence embeddings.

Instead of keyword search, it understands meaning — "data science" and "machine learning" won't be treated as unrelated.

---

## 🧠 Tech Used
- SentenceTransformer (MiniLM-L6-v2)
- Streamlit
- PyTorch
- Hugging Face Hub (token required for model load)

---

## ✅ Try It Live
👉 [Launch the App](https://resume-matcher-ai-gyictans8dycejgueawtzv.streamlit.app/)

> No setup required. Fully interactive.

---

## 📝 Test Scenarios
| Job Description | Expected Match |
|-----------------|----------------|
| C++ + Java backend dev | Cindy Hamilton |
| Deep learning + AI research | James Pruitt, Rachel Johnson |
| NLP with Python | Margaret Martin |
| Cybersecurity | Elizabeth Smith |
| SQL + dashboards | Desiree White or others with SQL/React |

---

## 📌 Future Ideas
- Upload your own resume CSV
- Add resume sections (experience, education, tools)
- Model selector (MiniLM, BGE, OpenAI)
- Skill-highlighting in the UI

---

## 👋 About Me
Built by Edbert Hansel — connect with me on [LinkedIn](https://www.linkedin.com/in/edbert-hansel-33b080218/)

This is part of a 5-project portfolio designed to show what I can build as an AI/ML engineer from scratch.

> Let’s collaborate, connect, or brainstorm cool AI ideas ✨
