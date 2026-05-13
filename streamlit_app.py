import asyncio
from pathlib import Path
import time
import os
import requests

import streamlit as st
import inngest

from dotenv import load_dotenv

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="RAG AI Assistant",
    page_icon="💬",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0E1117;
        color: white;
    }

    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }

    .subtitle {
        color: #A0A0A0;
        margin-bottom: 30px;
    }

    .uploadedFile {
        border: 1px solid #333;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("📚 RAG Dashboard")

    st.markdown("---")

    st.subheader("⚙️ Models")

    st.write("LLM: llama3")
    st.write("Embeddings: nomic-embed-text")
    st.write("Vector DB: Qdrant")

    st.markdown("---")

    st.subheader("📄 Uploaded PDFs")

    if st.session_state.uploaded_files:

        for file in st.session_state.uploaded_files:
            st.markdown(
                f"""
                <div class="uploadedFile">
                    📄 {file}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.caption("No PDFs uploaded yet.")

# =========================================
# MAIN TITLE
# =========================================

st.markdown(
    '<div class="main-title">🤖 Local RAG AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload PDFs and ask questions using your local AI pipeline.</div>',
    unsafe_allow_html=True
)

# =========================================
# INNGEST CLIENT
# =========================================

@st.cache_resource
def get_inngest_client() -> inngest.Inngest:

    return inngest.Inngest(
        app_id="rag_app",
        is_production=False
    )

# =========================================
# SAVE PDF
# =========================================

def save_uploaded_pdf(file) -> Path:

    uploads_dir = Path("uploads")

    uploads_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = uploads_dir / file.name

    file_bytes = file.getbuffer()

    file_path.write_bytes(file_bytes)

    return file_path

# =========================================
# SEND INGEST EVENT
# =========================================

async def send_rag_ingest_event(
    pdf_path: Path
) -> None:

    client = get_inngest_client()

    await client.send(

        inngest.Event(

            name="rag/ingest_pdf",

            data={
                "pdf_path": str(pdf_path.resolve()),
                "source_id": pdf_path.name,
            },
        )
    )

# =========================================
# PDF UPLOAD SECTION
# =========================================

st.subheader("📄 Upload PDF")

uploaded = st.file_uploader(
    "Choose a PDF",
    type=["pdf"],
    accept_multiple_files=False
)

if uploaded is not None:

    with st.spinner("Uploading and ingesting PDF..."):

        path = save_uploaded_pdf(uploaded)

        asyncio.run(
            send_rag_ingest_event(path)
        )

        time.sleep(0.3)

    if uploaded.name not in st.session_state.uploaded_files:

        st.session_state.uploaded_files.append(
            uploaded.name
        )

    st.success(
        f"✅ Ingestion triggered for: {path.name}"
    )

# =========================================
# DIVIDER
# =========================================

st.divider()

# =========================================
# QUERY EVENT
# =========================================

async def send_rag_query_event(
    question: str,
    top_k: int
):

    client = get_inngest_client()

    result = await client.send(

        inngest.Event(

            name="rag/query_pdf_ai",

            data={
                "question": question,
                "top_k": top_k,
            },
        )
    )

    return result[0]

# =========================================
# INNGEST API URL
# =========================================

def _inngest_api_base() -> str:

    return os.getenv(
        "INNGEST_API_BASE",
        "http://127.0.0.1:8288/v1"
    )

# =========================================
# FETCH RUNS
# =========================================

def fetch_runs(event_id: str):

    url = f"{_inngest_api_base()}/events/{event_id}/runs"

    resp = requests.get(url)

    resp.raise_for_status()

    data = resp.json()

    return data.get("data", [])

# =========================================
# WAIT FOR OUTPUT
# =========================================

def wait_for_run_output(
    event_id: str,
    timeout_s: float = 120.0,
    poll_interval_s: float = 0.5
):

    start = time.time()

    while True:

        runs = fetch_runs(event_id)

        if runs:

            run = runs[0]

            status = run.get("status")

            if status in (
                "Completed",
                "Succeeded",
                "Success",
                "Finished"
            ):

                return run.get("output") or {}

            if status in (
                "Failed",
                "Cancelled"
            ):

                raise RuntimeError(
                    f"Function run {status}"
                )

        if time.time() - start > timeout_s:

            raise TimeoutError(
                "Timed out waiting for run output"
            )

        time.sleep(poll_interval_s)

# =========================================
# CHAT HISTORY DISPLAY
# =========================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

# =========================================
# CHAT INPUT
# =========================================

prompt = st.chat_input(
    "Ask a question about your PDFs..."
)

# =========================================
# HANDLE QUESTION
# =========================================

if prompt:

    # -----------------------------
    # USER MESSAGE
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.write(prompt)

    # -----------------------------
    # AI RESPONSE
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Send query event
            event_id = asyncio.run(

                send_rag_query_event(
                    prompt,
                    top_k=5
                )
            )

            # Wait for answer
            output = wait_for_run_output(
                event_id
            )

            answer = output.get(
                "answer",
                "No answer generated."
            )

            sources = output.get(
                "source",
                []
            )

            # Streaming effect
            placeholder = st.empty()

            streamed = ""

            for word in answer.split():

                streamed += word + " "

                placeholder.markdown(streamed)

                time.sleep(0.02)

            # Save assistant response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            # Sources
            if sources:

                with st.expander(
                    "📚 Sources"
                ):

                    for s in sources:

                        st.write(f"- {s}")