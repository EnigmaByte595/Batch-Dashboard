import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="IIEST Civil-Met Hub", layout="wide")

st.markdown(
    """
    <style>
    .book-link {
        display: inline-block;
        padding: 8px 14px;
        margin: 5px 0;
        background-color: #262730;
        color: #FFD700 !important;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    .book-link:hover {
        background-color: #333333;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("IIEST Civil-Met Notes & Resources")

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7,tab8 , tab9= st.tabs(
    ["📖 Syllabus", "❓ PYQs", "📚 Books", "📝 Classnotes", "🧪 Lab Notes", "📐 Drawing Plates", "📂 Assignments","⏰Civil-Met-(A,B)ROUTINE","Discussions"]
)

# --- Tab 1: Syllabus ---
with tab1:

    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#2980B9; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.header("Syllabus")
    book_card("Physics Syllabus","https://drive.google.com/file/d/1u3QJSGBeNrry3zmk75aJJNzvTEMjwB3k/view?usp=drive_link)")
    book_card("Maths Syllabus","https://drive.google.com/file/d/1R20GWLIeyLrvGyVubwCJzygXPhxaIQnB/view?usp=drive_link")
    #st.markdown("[AI_ML Syllabus]()")
    book_card("materials","https://drive.google.com/file/d/1-MyY4tZKGMwT1iclaeekGZ3D39X3BfUn/view?usp=drive_link")
    book_card("energy_env_climate","https://drive.google.com/file/d/1J866HBgAwWaakmc1kfuLMypHfQHnNbLG/view?usp=sharing")
    #st.markdown("[Engineering_drawing]()")


# --- Tab 2: PYQs ---
with tab2:

    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#F39C12; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.header("pyq")
    pyq = {
        "Maths": {
            "2017_MA-1101": "https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2016_MA_1101": "https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2015_MA_1101": "https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2020-21_MA_1101": "https://drive.google.com/file/d/1IL1x3cecxPsGAXYsFtD9XgGoqDheLwke/view?usp=drive_link",
            "2022_MA_mid_sem": "https://drive.google.com/file/d/1MbRvk1Wg1fnbH-rTMjEY4prgIby4CeNY/view?usp=drive_link",
            "2023_MA_1101_mid": "https://drive.google.com/file/d/14WptP5_jNHpd7bRs1bEyzVUevDwnlAOA/view?usp=drive_link",
        },
        "Physics": {
            "2021_PH_1101": "https://drive.google.com/file/d/17OhlHtvOn8w7eHbiOHgZjuScbHT8pbKC/view?usp=sharing",
            "2017_PH_1101": "https://drive.google.com/file/d/1RSl_8Nk4ecLemjBcfcOTo1bda_8-pCYu/view?usp=drive_link",
            "MECHA_2021_1101": "https://drive.google.com/file/d/1V_F-4Il5zt0gvGS8mXxdg4-Jc79iSgVg/view?usp=drive_link",
            "PH_2020-21_1101": "https://drive.google.com/file/d/1RRIQKscrrSj84uL_r0OPfUPpFK6XzHMN/view?usp=drive_link",
            "MECHA_2022_MID_1101": "https://drive.google.com/file/d/1MbRvk1Wg1fnbH-rTMjEY4prgIby4CeNY/view?usp=drive_link",
            "mecha_2023_end_1101": "https://drive.google.com/file/d/1vjgNjWsBfNX1k6C-RK1a_bdKqxa0M_-e/view?usp=drive_link",
            "mecha_2021_mid_soln": "https://drive.google.com/file/d/1O6JMxsTWdAapOZ8QUj0VwnhGojPZOPZh/view?usp=drive_link",
        }
    }

    for subject, papers in pyq.items():
        with st.expander(f"**{subject}**"):
            for paper, link in papers.items():
                book_card(paper, link)
    

    

# --- Tab 3: Books ---
with tab3:

    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#8E44AD; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    
    st.header("Books Referred by Professors")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📘 Physics")
        book_card("Wave and Oscillation - NK Bajaj", "https://drive.google.com/file/d/115xtoNhhJhrpgCqjwTdNZnk0Lq421sSW/view?usp=sharing")
        book_card("engineering_mechanics_dynamics -- Meriam & Kraige","https://drive.google.com/file/d/1RmyPBGEKn-qwXb2lkUlxfNQhryj-LHhs/view?usp=drive_link")
        book_card("optics-Ajoy Ghatak","https://drive.google.com/file/d/1zmDjO9GWLBDqJXfIV4ZSfxeHrkTej4ab/view?usp=drive_link")
        book_card("Introduction to Electrodynamics-griffiths","https://drive.google.com/file/d/1zvnwOvivXpYq52NUmtFvpfrE6hsv6iIQ/view?usp=drive_link")
        book_card("optics-Eugene Hecht","https://drive.google.com/file/d/1R15VPR7EDGBP0GZ_-GPkqRppDfUZzOe0/view?usp=drive_link")
        book_card("Quantum Physics-Robert Eisberg and Robert Resnik","https://drive.google.com/file/d/1m9Twnc5sn_Tv3Yy1OFlRqVblCqCJ_WdD/view?usp=drive_link")
        book_card("concepts of modern physics-Arthur Beiser","https://drive.google.com/file/d/1KPDAMoUSEMWoGRJm3zMDQMlV6vjnQqMT/view?usp=drive_link")
        book_card("Free and forced vibrations-DP_roychoudhury","https://drive.google.com/file/d/1YSmz30MzgjhdWlaLXWIRCdsAPsJFIVMv/view?usp=drive_link")
        book_card("engineering mechanics-mariam & kraige","https://drive.google.com/file/d/1RmyPBGEKn-qwXb2lkUlxfNQhryj-LHhs/view?usp=drive_link")
        book_card("engineering mechanics-mariam & kraige-solution","https://drive.google.com/file/d/1mKJZmNWfFUkfYR-qL_9EIWX5mBOyNXsP/view?usp=drive_link")
        book_card("engineering mechanics dynamics-meriam & kraige","https://drive.google.com/file/d/1IX9mE9JHqT_oL7ch2MTnMurNAhLGUWIk/view?usp=drive_link")
        book_card("engineering mechanics statics-meriam & kraige","https://drive.google.com/file/d/1aAdahyyFnhp7xP8KOByaIYJioTNG2CDY/view?usp=drive_link")
    with col2:
        st.subheader("📗 Mathematics")    
        book_card("Advanced engineering mathematics-kreyszig","https://drive.google.com/file/d/19cuVy4mMbmoQbAYnoKpVcGPYxaSCK8np/view?usp=drive_link")
        book_card("Engineering mathematics-SS SASTRY","https://drive.google.com/file/d/10vCcObvmvxOOky-XycGMX2VEwYXsg_a0/view?usp=drive_link")
        book_card("Integral calculus & diff. eqn","https://drive.google.com/file/d/1ReQu37i1qbTYO4QLMHLOYtRR9rJcgz1z/view?usp=drive_link")
        book_card("Advanced calculus-DV widder","https://drive.google.com/file/d/1BfajFPEg5d0WE40Qn7g12J5c7WhZij4w/view?usp=drive_link")
        book_card("manufacturing engineering and technology-S vijay sekhar","https://drive.google.com/file/d/1A7-f9UI__vZ-UVVFtfdSc_oFP02E3Wiq/view?usp=drive_link")
        book_card("gps(1st sem","https://drive.google.com/file/d/1jBvb9R74WDrWwgmaOJJSwHsJSfExmEP3/view?usp=drive_link")

# --- Tab 4: Classnotes ---
with tab4:
    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#E67E22; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.header("Classnotes")
    classnotes = {
        "Maths": {
            "Ordinary Differential Equation": "https://drive.google.com/file/d/169VgtBhtFiquhjY8kK4drDrB3aYO6eYv/view?usp=drive_link",
            "Infinite series": "https://drive.google.com/file/d/1cS18j8eNAuDhXN2zR9zr5cQwaPrY3wJb/view?usp=drive_link",
            "LCD,MVT,LEIBNITZ,TAYLOR,MCLAURIAN,ROC,ASYMPTOTES": "https://drive.google.com/file/d/1X6TdRmmte1w5gPhfUtho3D0NLvQ5uASK/view?usp=drive_link",
            "function of single variable":"https://drive.google.com/file/d/15KuGXs5M8uq_7W1IaM5xKwna4KX9sZAl/view?usp=drive_link",
            "function of several variable":"https://drive.google.com/file/d/15KuGXs5M8uq_7W1IaM5xKwna4KX9sZAl/view?usp=drive_link",
            "higher order differential eqn":"https://drive.google.com/file/d/1iSxpuAaxIII8LPYz4fslqAuL-H7iiSXg/view?usp=drive_link",
            "improper integral":"https://drive.google.com/file/d/1xI_6mfBgybxOn5XKeXLAYrQ7Ykz0fYF9/view?usp=drive_link",
        },
        "Physics": {
            "Vectors": "https://drive.google.com/file/d/1slR2P1t3eRWQzf_-2qTBk0gkC6skLwkU/view?usp=drive_link",
            "Waves": "https://drive.google.com/file/d/1EQmzu-B1uzdLocKPMlbd8RlcsX2bJ_3H/view?usp=drive_link",
            "wave Optics": "https://drive.google.com/file/d/1upBxIkkC-kV377JoHWU4mPIEZXwx4JGJ/view?usp=drive_link",
            "oscillations": "https://drive.google.com/file/d/1V7QXgRFGW1EYDnE0OWOTYL-J0HSe6yy_/view?usp=drive_link",
            "Quantum theory":"https://drive.google.com/file/d/1GbHcVqYBR8akyyFF0Fg82aQWfMcgzvJd/view?usp=drive_link",
            "EM Theory":"https://drive.google.com/file/d/1IAMSeSt9WzQccLpYD0hx_M8sC1BP96ju/view?usp=drive_link",
            "EMT":"https://drive.google.com/file/d/1TDuE04-yxNm6D6b_Y8eY-P8A8p6Muufj/view?usp=drive_link",
            "EMT_1":"https://drive.google.com/file/d/1Q3EW4TN7BwS03Sk2pHrFDWdaBvoh1PBl/view?usp=drive_link",
            "EMT_2":"https://drive.google.com/file/d/1lzTY7JVwfL7NDE0leUtCzyXJXIWonbG_/view?usp=drive_link",
            "EMT_3":"https://drive.google.com/file/d/1CCHwve10WiNtPjDBXDhYaeRE1X1Fb8si/view?usp=drive_link",
            "relativity":"https://drive.google.com/file/d/1TFq1CT5MGhxpLuwwCKEIji6_E-Vn-UIk/view?usp=drive_link",
            "relativity1":"https://drive.google.com/file/d/1R_LFwrW_im0jeTeMpaxnuaKhjgkCJZHl/view?usp=drive_link",
            "relativity2":"https://drive.google.com/file/d/1T--z7VOSt2oEA6VAZ9kx7YCl2LHuK980/view?usp=drive_link",
            "polarisation":"https://drive.google.com/file/d/1W9ASoPw04D-XnkEQKo5A2CQubvtxm4NI/view?usp=drive_link",
            "Interference":"https://drive.google.com/file/d/1jsqFqKsvVz_jlsWc4aMSQiHyvN-8FXwb/view?usp=drive_link",
            "Quantum mechanics1":"https://drive.google.com/file/d/1yu473QIPcpgOunbEjGWZqtob6yYpVai5/view?usp=drive_link",
            "quant_mech2":"https://drive.google.com/file/d/1KB7txfNviPs-mfhcXDCGkamzNOMDQl4d/view?usp=drive_link",
            "Laser":"https://drive.google.com/file/d/1doOXCjOx0SwUKS_5NZKr5s-oXG5DG7oW/view?usp=drive_link",
            "Relativity_probability":"https://drive.google.com/file/d/1n9QqKrt8Q2fz-vqMFppd77NCYkAx8bWv/view?usp=drive_link",
            "qm_compton_effect":"https://drive.google.com/file/d/1-lOosl6clBsZJB2wvoamSklEsLgvK-up/view?usp=drive_link",
            "Quantum_mech_special_theory_of_relativity1":"https://drive.google.com/file/d/1F-c-Wm7lmskkBmrzmLvqvsdjUDkY4X4a/view?usp=drive_link",
            "QM_special_theory_of_relativity2":"https://drive.google.com/file/d/1rvNJJV_BlIabYJaxf2abdnLAPGUc4DHl/view?usp=drive_link",
            "Diffraction":"https://drive.google.com/file/d/1fvFf-CGDjVHWtOnS1YXUN3-M-8uJiMxw/view?usp=drive_link",
            "Double_slit_diff_pattern":"https://drive.google.com/file/d/17H0PvLNFLbnG-HnXs4x0RplNnJGwfwj_/view?usp=drive_link",
            "mechanics-dynamics":"https://drive.google.com/file/d/1wXkqvKELoh3r2IVOeYZQ4T568z7rKBDE/view?usp=drive_link",
            "mechanics_practice":"https://drive.google.com/file/d/1EUbFVQwxYYTXk-TJZ1kGHJ305MWZ7uhv/view?usp=drive_link",
        },
        "Energy_Environment_climate_change": {
            "Air standard": "https://drive.google.com/file/d/1cOLew49keaRYTVj1xRQWwG1U1I5JKX1-/view?usp=drive_link",
            "Environment": "https://drive.google.com/file/d/1ok7g72pF8-lphibZj1_gDv3L1dajbvE3/view?usp=drive_link",
            "Ecosystem":"https://drive.google.com/file/d/14sGFyhdDqckJjs7EURMJNQzZ-x5P4nuJ/view?usp=drive_link",
            "Solid waste management":"https://drive.google.com/file/d/1GtOjgJ8Gg7OIcSUBhJq0weMDCSbnMoGo/view?usp=drive_link",
            "Environment legislation":"https://drive.google.com/file/d/1vDWh9bbS24J_v8-vKrhAUS9V0kbz9D7x/view?usp=drive_link",
            "Noise pollution":"https://drive.google.com/file/d/1IZF5kD5wb--YbHNkkM1bqoeQ7unfujX4/view?usp=drive_link",
            "water pollution":"https://drive.google.com/file/d/190wDONWt73dgaDmwugybjGQ2oPK97ZVC/view?usp=drive_link",
            "Environmental impact assesment":"https://drive.google.com/file/d/1dwK7JMY7qgjs6U-25rRa1exa5H7pROI9/view?usp=drive_link",
        },
        "materials": {
            "Introduction":"https://drive.google.com/file/d/1Ze-WR6fpxNuN-d-1xJ2NI2-z3g7S84YP/view?usp=drive_link",
            "structure and properties of ceramics": "https://drive.google.com/file/d/1dMsQ8fhDmfBOHu6tT2xBQpyCOr40HIFS/view?usp=drive_link",
            "mechanical prperties":"https://drive.google.com/file/d/12COuDBAfSgOn9tkymIZCK0tsnDlfdY3J/view?usp=drive_link",
            "MME-1st-sem":"https://drive.google.com/file/d/1Z4ZRfgrYVx1boAiCNAyAb0uMrG5m6fi7/view?usp=drive_link",
        },
        "AI_ML": {
            "python": "https://drive.google.com/file/d/1_ZYYORKssVzG9OuBXn8a1e25yTxp8Yad/view?usp=drive_link",
            "Linux command handbook":"https://drive.google.com/file/d/1bViAqHqdyh7owIn7TVW0sJ4Oo9Nh04uv/view?usp=drive_link",
            "python problems":"https://www.hackerrank.com/domains/python",
        },
    }

    # Display expanders for each subject
    for subject, chapters in classnotes.items():
        with st.expander(subject):
            for chapter, link in chapters.items():
                book_card(chapter, link)

# --- Tab 5: Lab Notes ---
with tab5:

    st.header("Lab Notes")
    st.write("will update soon")

# --- Tab 6: Drawing Plates ---
with tab6:
    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#E91E63; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.header("Engineering Drawing")
    book_card("Plate 1","https://drive.google.com/file/d/12EnfY4K7jU44tMil1zmY12neoGumgZtC/view?usp=drive_link")
    book_card("Plate 2","https://drive.google.com/file/d/1pYd_ecgkcGMP-6dodt4cCSuLhTyT6XB5/view?usp=drive_link")
    book_card("Plate 3","https://drive.google.com/file/d/1zVcv9G50FbpmcL8tLJRioEt1SKJqLgEl/view?usp=drive_link")
    book_card("Plate 4","https://drive.google.com/file/d/1h42sX1H2OckqK3e6DW8t750RejpfcMfT/view?usp=drive_link")
    book_card("plate 5","https://drive.google.com/file/d/1FpCtrrH18297cae3Q8aycGIhDAQQjg53/view?usp=drive_link")
    book_card("plate 6","https://drive.google.com/file/d/1azU_s8oFA-sDpbEnIdDh3pO2BzUPZRk6/view?usp=drive_link")
    book_card("plate 7","https://drive.google.com/file/d/1PU9ZmBvwUCF0GNPnQQSGiLkwwFsYlJSk/view?usp=drive_link")
    book_card("ED pyq","https://drive.google.com/file/d/1YeiEFJs4TysuL0MRsyRf5LCZKsOhVE5i/view?usp=drive_link")
    book_card("Assignment","https://drive.google.com/file/d/1dekTEMA1j0Xumf-wUu_d0wlwGUP3mo2H/view?usp=drive_link")
    book_card("ED viva","https://drive.google.com/file/d/1oBawP4nIfz3KsLrUfLMUXVBfE8gMEiaC/view?usp=drive_link")
    book_card("Ed Book-N.D.BHATT","https://drive.google.com/file/d/1qGiz2NjwAwwAVjithmeP-PC-6vu1SNmJ/view?usp=drive_link")
    book_card("all plates","https://drive.google.com/file/d/1DJyxjuUqUY50DOPW7OIYGN919fkBe7A-/view?usp=drive_link")
# --- Tab 7: Assignments ---
with tab7:
    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#27AE60; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.header("Assignments")
    book_card("physics problem set-1","https://drive.google.com/file/d/1m7TFOjLHyQPkicUaRNkJzcb0S7ZCJg1j/view?usp=sharing")
    book_card("math problemset-1","https://drive.google.com/file/d/1engBCWYFKwaFTALKEdYrSfS2akSJkTfu/view?usp=sharing")
    book_card("Infinite_series_soln","https://drive.google.com/file/d/1eyKunaxhiZJNNt-8639MVZDUy8a0oLH9/view?usp=drive_link")
# --- Tab8:Routine ---
with tab8:
    def book_card(name, link):
        st.markdown(
            f"""
            <div style='
                background-color:#1E1E1E;
                padding:10px;
                margin:6px 0;
                border-radius:10px;
                box-shadow:2px 2px 6px rgba(0,0,0,0.4);
            '>
                <a href="{link}" target="_blank" style='color:#6C757D; text-decoration:none; font-size:16px; font-weight:600;'>
                    {name}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.header("CIVIL-MET ROUTINE")
    book_card("Routine","https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing")

with tab9:

    FILE = "comments.csv"

    # Load old comments safely (handle empty file)
    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        df = pd.read_csv(FILE)
    else:
        df = pd.DataFrame(columns=["time", "name", "comment"])

    st.title("💬 Batch Comments & Suggestions")

    # Input fields
    name = st.text_input("Your name:")
    comment = st.text_area("Write your comment:")

    # Save new comment
    if st.button("Submit"):
        if name and comment:
            new = pd.DataFrame(
                [[datetime.now().strftime("%Y-%m-%d %H:%M"), name, comment]],
                columns=["time", "name", "comment"]
            )
            df = pd.concat([df, new], ignore_index=True)
            df.to_csv(FILE, index=False)
            st.success("✅ Comment added!")
            st.balloons()
            st.snow()
        else:
            st.warning("⚠️ Please enter both name and comment.")

    # Display comments (latest first, like chat)
    st.subheader("🗨️ All Comments")
    if not df.empty:
        for i, row in df.iloc[::-1].iterrows():  # reverse order
            st.markdown(f"**{row['name']}** ({row['time']}): {row['comment']}")
    else:
        st.info("No comments yet. Be the first to add one! 🎉")

