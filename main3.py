import streamlit as st

st.set_page_config(page_title="IIEST Civil-Met Hub", layout="wide")

st.title("IIEST Civil-Met Notes & Resources")

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7,tab8 = st.tabs(
    ["📖 Syllabus", "❓ PYQs", "📚 Books", "📝 Classnotes", "🧪 Lab Notes", "📐 Drawing Plates", "📂 Assignments","⏰Civil-Met-(A,B)ROUTINE"]
)

# --- Tab 1: Syllabus ---
with tab1:
    st.header("Syllabus")
    st.markdown("[Physics Syllabus](https://drive.google.com/file/d/1u3QJSGBeNrry3zmk75aJJNzvTEMjwB3k/view?usp=drive_link)")
    st.markdown("[Maths Syllabus](https://drive.google.com/file/d/1R20GWLIeyLrvGyVubwCJzygXPhxaIQnB/view?usp=drive_link)")
    #st.markdown("[AI_ML Syllabus]()")
    st.markdown("[materials](https://drive.google.com/file/d/1-MyY4tZKGMwT1iclaeekGZ3D39X3BfUn/view?usp=drive_link)")
    st.markdown("[energy_env_climate](https://drive.google.com/file/d/1J866HBgAwWaakmc1kfuLMypHfQHnNbLG/view?usp=sharing)")
    #st.markdown("[Engineering_drawing]()")

# --- Tab 2: PYQs ---
with tab2:
    st.header("pyq")
    pyq = {
        "Maths": {
            "2017_MA-1101":"https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2016_MA_1101":"https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2015_MA_1101":"https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing",
            "2020-21_MA_1101":"https://drive.google.com/file/d/1IL1x3cecxPsGAXYsFtD9XgGoqDheLwke/view?usp=drive_link",
            "2022_MA_mid_sem":"https://drive.google.com/file/d/1MbRvk1Wg1fnbH-rTMjEY4prgIby4CeNY/view?usp=drive_link",
            "2023_MA_1101_mid":"https://drive.google.com/file/d/14WptP5_jNHpd7bRs1bEyzVUevDwnlAOA/view?usp=drive_link",




        },
        
        "Physics":{
            "2021_PH_1101":"https://drive.google.com/file/d/17OhlHtvOn8w7eHbiOHgZjuScbHT8pbKC/view?usp=sharing",
            "2017_PH_1101":"https://drive.google.com/file/d/1RSl_8Nk4ecLemjBcfcOTo1bda_8-pCYu/view?usp=drive_link",
            "MECHA_2021_1101":"https://drive.google.com/file/d/1V_F-4Il5zt0gvGS8mXxdg4-Jc79iSgVg/view?usp=drive_link",
            "PH_2020-21_1101":"https://drive.google.com/file/d/1RRIQKscrrSj84uL_r0OPfUPpFK6XzHMN/view?usp=drive_link",
            "MECHA_2022_MID_1101":"https://drive.google.com/file/d/1MbRvk1Wg1fnbH-rTMjEY4prgIby4CeNY/view?usp=drive_link",
            "mecha_2023_end_1101":"https://drive.google.com/file/d/1vjgNjWsBfNX1k6C-RK1a_bdKqxa0M_-e/view?usp=drive_link",
            "mecha_2021_mid_soln":"https://drive.google.com/file/d/1O6JMxsTWdAapOZ8QUj0VwnhGojPZOPZh/view?usp=drive_link",




        }
    }

    for subject, papers in pyq.items():
        with st.expander(subject):
            for paper, link in papers.items():
                st.markdown(f"- [{paper}]({link})")
    

# --- Tab 3: Books ---
with tab3:
    st.header("Books Referred by Professors")
    st.markdown("[wave and oscillation - NK Bajaj](https://drive.google.com/file/d/115xtoNhhJhrpgCqjwTdNZnk0Lq421sSW/view?usp=sharing)")
    st.markdown("[engineering_mechanics_dynamics -- Meriam & Kraige](https://drive.google.com/file/d/1RmyPBGEKn-qwXb2lkUlxfNQhryj-LHhs/view?usp=drive_link)")
    st.markdown("[optics-Ajoy Ghatak](https://drive.google.com/file/d/1zmDjO9GWLBDqJXfIV4ZSfxeHrkTej4ab/view?usp=drive_link)")
    st.markdown("[Introduction to Electrodynamics-griffiths](https://drive.google.com/file/d/1zvnwOvivXpYq52NUmtFvpfrE6hsv6iIQ/view?usp=drive_link)")
    st.markdown("[optics-Eugene Hecht](https://drive.google.com/file/d/1R15VPR7EDGBP0GZ_-GPkqRppDfUZzOe0/view?usp=drive_link)")
    st.markdown("[Quantum Physics-Robert Eisberg and Robert Resnik](https://drive.google.com/file/d/1m9Twnc5sn_Tv3Yy1OFlRqVblCqCJ_WdD/view?usp=drive_link)")
    st.markdown("[concepts of modern physics-Arthur Beiser](https://drive.google.com/file/d/1KPDAMoUSEMWoGRJm3zMDQMlV6vjnQqMT/view?usp=drive_link)")
    st.markdown("[Free and forced vibrations-DP_roychoudhury](https://drive.google.com/file/d/1YSmz30MzgjhdWlaLXWIRCdsAPsJFIVMv/view?usp=drive_link)")
    st.markdown("[Advanced engineering mathematics-kreyszig](https://drive.google.com/file/d/19cuVy4mMbmoQbAYnoKpVcGPYxaSCK8np/view?usp=drive_link)")
    st.markdown("[Engineering mathematics-SS SASTRY](https://drive.google.com/file/d/10vCcObvmvxOOky-XycGMX2VEwYXsg_a0/view?usp=drive_link)")
    st.markdown("[Integral calculus & diff. eqn](https://drive.google.com/file/d/1ReQu37i1qbTYO4QLMHLOYtRR9rJcgz1z/view?usp=drive_link)")
    st.markdown("[Advanced calculus-DV widder](https://drive.google.com/file/d/1BfajFPEg5d0WE40Qn7g12J5c7WhZij4w/view?usp=drive_link)")
    st.markdown("[engineering mechanics-mariam & kraige](https://drive.google.com/file/d/1RmyPBGEKn-qwXb2lkUlxfNQhryj-LHhs/view?usp=drive_link)")
    st.markdown("[engineering mechanics-mariam & kraige-solution](https://drive.google.com/file/d/1mKJZmNWfFUkfYR-qL_9EIWX5mBOyNXsP/view?usp=drive_link)")
    st.markdown("[engineering mechanics dynamics-meriam & kraige](https://drive.google.com/file/d/1IX9mE9JHqT_oL7ch2MTnMurNAhLGUWIk/view?usp=drive_link)")
    st.markdown("[engineering mechanics statics-meriam & kraige](https://drive.google.com/file/d/1aAdahyyFnhp7xP8KOByaIYJioTNG2CDY/view?usp=drive_link)")
    st.markdown("[manufacturing engineering and technology-S vijay sekhar](https://drive.google.com/file/d/1A7-f9UI__vZ-UVVFtfdSc_oFP02E3Wiq/view?usp=drive_link)")

# --- Tab 4: Classnotes ---
with tab4:
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
                st.markdown(f"- [{chapter}]({link})")

# --- Tab 5: Lab Notes ---
with tab5:
    st.header("Lab Notes")
    st.write("will update soon")

# --- Tab 6: Drawing Plates ---
with tab6:
    st.header("Engineering Dreawing")
    st.markdown("[Plate 1](https://drive.google.com/file/d/12EnfY4K7jU44tMil1zmY12neoGumgZtC/view?usp=drive_link)")
    st.markdown("[Plate 2](https://drive.google.com/file/d/1pYd_ecgkcGMP-6dodt4cCSuLhTyT6XB5/view?usp=drive_link)")
    st.markdown("[Plate 3](https://drive.google.com/file/d/1zVcv9G50FbpmcL8tLJRioEt1SKJqLgEl/view?usp=drive_link)")
    st.markdown("[Plate 4](https://drive.google.com/file/d/1h42sX1H2OckqK3e6DW8t750RejpfcMfT/view?usp=drive_link)")
    st.markdown("[plate 5](https://drive.google.com/file/d/1FpCtrrH18297cae3Q8aycGIhDAQQjg53/view?usp=drive_link)")
    st.markdown("[plate 6](https://drive.google.com/file/d/1azU_s8oFA-sDpbEnIdDh3pO2BzUPZRk6/view?usp=drive_link)")
    st.markdown("[plate 7](https://drive.google.com/file/d/1PU9ZmBvwUCF0GNPnQQSGiLkwwFsYlJSk/view?usp=drive_link)")
    st.markdown("[ED pyq](https://drive.google.com/file/d/1YeiEFJs4TysuL0MRsyRf5LCZKsOhVE5i/view?usp=drive_link)")
    st.markdown("[Assignment](https://drive.google.com/file/d/1dekTEMA1j0Xumf-wUu_d0wlwGUP3mo2H/view?usp=drive_link)")
    st.markdown("[ED viva](https://drive.google.com/file/d/1oBawP4nIfz3KsLrUfLMUXVBfE8gMEiaC/view?usp=drive_link)")
    st.markdown("[Ed Book-N.D.BHATT](https://drive.google.com/file/d/1qGiz2NjwAwwAVjithmeP-PC-6vu1SNmJ/view?usp=drive_link)")
    st.markdown("[all plates](https://drive.google.com/file/d/1DJyxjuUqUY50DOPW7OIYGN919fkBe7A-/view?usp=drive_link)")
# --- Tab 7: Assignments ---
with tab7:
    st.header("Assignments")
    st.write("will add later")

# --- Tab8:Routine ---
with tab8:
    st.header("CIVIL-MET ROUTINE")
    st.markdown("[Routine](https://drive.google.com/file/d/11lOd5H1rRadfqFL27fvBgLkns4y5pL9g/view?usp=sharing)")