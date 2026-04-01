"""
Home — Optimization Algorithm Visualizer
"""

import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Optimization Visualizer",
    layout="wide",
    page_icon="🔍"
)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🔍 Navigation")
st.sidebar.markdown("Jump to any module:")

st.sidebar.page_link(
    "pages/1_Unconstrained_Minimization.py",
    label="📈 Unconstrained Minimization"
)

st.sidebar.page_link(
    "pages/2_Pareto_Front.py",
    label="📊 Pareto Front"
)

st.sidebar.page_link(
    "pages/3_Genetic_Algorithm.py",
    label="🧬 Genetic Algorithm"
)

st.sidebar.page_link(
    "pages/4_Simulated_Annealing.py",
    label="🌡️ Simulated Annealing"
)

# ------------------ HERO SECTION ------------------
st.title("🔍 Optimization Algorithm Visualizer")

st.markdown("""
Welcome to an **interactive playground for optimization algorithms**.

Explore how different algorithms behave, compare their performance visually,
and build intuition through hands-on experimentation.
""")

st.markdown("---")

# ------------------ MAIN LAYOUT ------------------
col1, col2 = st.columns(2)

# -------- LEFT COLUMN (Deterministic Methods) --------
with col1:
    st.subheader("📈 1 — Unconstrained Minimization")
    st.markdown("🟡 Intermediate")

    with st.expander("Learn more"):
        st.markdown("""
Compare three gradient-based methods on any 2D function:

- **Steepest Descent (SD)**
- **Newton's Method**
- **Conjugate Gradient (CG)**

📌 **What you'll learn:**
- Why Newton's method converges faster
- When CG is more efficient than SD
- How trajectories differ across methods
        """)

    st.page_link(
        "pages/1_Unconstrained_Minimization.py",
        label="🚀 Launch Demo"
    )

    st.markdown("---")

    st.subheader("🧬 3 — Genetic Algorithm")
    st.markdown("🟢 Beginner")

    with st.expander("Learn more"):
        st.markdown("""
Solve the **0/1 Knapsack problem** using a Genetic Algorithm:

- Tune population size, mutation rate, crossover rate
- Watch evolution across generations
- Observe convergence and diversity

📌 **What you'll learn:**
- How populations evolve
- Exploration vs exploitation trade-offs
- Effect of mutation and crossover
        """)

    st.page_link(
        "pages/3_Genetic_Algorithm.py",
        label="🚀 Launch Demo"
    )

# -------- RIGHT COLUMN (Other Methods) --------
with col2:
    st.subheader("📊 2 — Pareto Front")
    st.markdown("🟢 Beginner")

    with st.expander("Learn more"):
        st.markdown("""
Explore **multi-objective optimization**:

- Upload your own dataset or use built-in data
- Select any two objectives
- Identify Pareto optimal solutions

📌 **What you'll learn:**
- Trade-offs between objectives
- Dominance concepts
- Real-world decision making
        """)

    st.page_link(
        "pages/2_Pareto_Front.py",
        label="🚀 Launch Demo"
    )

    st.markdown("---")

    st.subheader("🌡️ 4 — Simulated Annealing")
    st.markdown("🟡 Intermediate")

    with st.expander("Learn more"):
        st.markdown("""
Schedule **10 exams into time slots** using Simulated Annealing:

- Adjust temperature and cooling rate
- Observe clash reduction over iterations
- Compare cooling strategies

📌 **What you'll learn:**
- Role of temperature in optimization
- Escaping local minima
- Cooling schedule effects
        """)

    st.page_link(
        "pages/4_Simulated_Annealing.py",
        label="🚀 Launch Demo"
    )

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)
