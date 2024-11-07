import streamlit as st


# --- PAGE SETUP ---
pages={

    " ":[
        
    st.Page(
        "Pages\Home.py",
        title="Home",
        icon=":material/home:",
        default=True)

        ],

    "Smart Tools": [

     st.Page(
    "Pages/Conversation.py",
    title="ConversAIon",
    icon=":material/forum:"),

    st.Page(
    "Pages/Imageprocessing.py",
    title="VisioCraft",
    icon=":material/photo_library:"),

  
    
    ]

}


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(pages)


# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Source code :  [Github](https://github.com/naveennk045)")


# --- RUN NAVIGATION ---
pg.run()
