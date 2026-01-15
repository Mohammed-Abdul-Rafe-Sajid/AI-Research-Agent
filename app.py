import streamlit as st
from graph.graph import build_graph
from graph.state import ResearchState


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agentic AI Research Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🎓 About")

    st.markdown(
        """
        **Mohammed Abdul Rafe Sajid**  
        AI & Research Enthusiast  

        🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-abdul-rafe-sajid-49a716291/)  
        🐙 [GitHub](https://github.com/Mohammed-Abdul-Rafe-Sajid)  
        🌐 [Portfolio](https://mohammedabdulrafesajid.netlify.app/)
        """
    )

    st.divider()

    st.markdown(
        """
        **About this project**

        An agentic AI system for academic research that:
        - Plans research steps
        - Retrieves papers (ArXiv)
        - Synthesizes findings
        - Verifies claims
        - Generates structured reports
        """
    )


# ---------------- HEADER ----------------
st.title("🎓 Agentic AI Research Assistant")
st.caption(
    "Autonomous literature retrieval, synthesis, verification, and reporting"
)

# ---------------- INPUT ----------------
query = st.text_area(
    "Enter a research question",
    placeholder="e.g., CNN vs Vision Transformers for medical image classification",
    height=100
)

run = st.button("Run Research")


# ---------------- EXECUTION ----------------
if run and query.strip():
    try:
        with st.spinner("Running research agents..."):
            graph = build_graph()

            state = ResearchState(
                user_query=query,
                research_scope={},
                plan=[],
                sources=[],
                documents=[],
                notes=[],
                flags=[],
                final_report=""
            )

            final_state = graph.invoke(state)

        st.success("Research completed successfully")

    except Exception as e:
        error_msg = str(e).lower()

        if "resource_exhausted" in error_msg or "quota" in error_msg:
            st.error(
                "🚫 **Gemini API quota exceeded**\n\n"
                "Please wait, switch API keys, or upgrade your plan."
            )
        elif "timeout" in error_msg:
            st.error("⏳ Request timed out. Please try again.")
        else:
            st.error("❌ An unexpected error occurred.")
            st.exception(e)

        st.stop()

    # ---------------- FINAL REPORT ----------------
    st.subheader("📚 Final Research Report")
    st.markdown(
        final_state.get("final_report", "No report generated.")
    )

    # ---------------- INTERMEDIATE OUTPUTS ----------------
    with st.expander("🔍 Research Scope"):
        st.json(final_state.get("research_scope", {}))

    with st.expander("🧩 Research Plan"):
        st.write(final_state.get("plan", []))

    with st.expander("📝 Synthesized Notes"):
        notes = final_state.get("notes", [])
        if notes:
            for note in notes:
                st.markdown(f"### {note.get('heading')}")
                for point in note.get("points", []):
                    st.markdown(f"- {point}")
        else:
            st.info("No synthesis notes generated.")

    with st.expander("⚠️ Verification Flags"):
        flags = final_state.get("flags", [])
        if flags:
            for f in flags:
                st.warning(f"{f.get('issue')}: {f.get('reason')}")
        else:
            st.info("No verification issues detected.")

else:
    st.info("Enter a research question and click **Run Research**")


# ---------------- FOOTER ----------------
st.markdown(
    "---\n"
    "<center>🎓 Built by Mohammed Abdul Rafe Sajid · Agentic AI Research Assistant</center>",
    unsafe_allow_html=True
)
