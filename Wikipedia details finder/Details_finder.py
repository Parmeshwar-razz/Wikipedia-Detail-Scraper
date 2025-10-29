# from bs4 import BeautifulSoup
# import chromedriver_autoinstaller
# from selenium import webdriver
# import streamlit as st

# chromedriver_autoinstaller.install()
# if "driver" not in st.session_state:
#     st.session_state.driver = webdriver.Chrome()
# name = st.text_input("Enter the name").replace(" ",'+')
# # link = None
# if st.button("Find Details "):
#     links = 'https://www.google.com/search?q='+name+'+wikipedia'
#     # driver = webdriver.Chrome()
#     st.session_state.driver.get(links)
#     soup = BeautifulSoup(st.session_state.driver.page_source,'html.parser')
#     # wikipedia link extractor 
#     link = None
#     for i in soup.find_all('div'):
#         try:
#             link_temp = i.find('a',href=True)
#             if 'en.wikipedia.org' in link_temp['href']:
#                 link = link_temp
#                 st.session_state.link= link_temp
#                 break
#         except:
#             pass
#     st.success(link['href'])
#     st.success("for visit this link click visit ")
#     # st.button("visit")

# if st.button("Visit"):
#     person_link = st.session_state.link['href']
#     st.session_state.driver.get(person_link)
#     soup = BeautifulSoup(st.session_state.driver.page_source,'html.parser')
#     for p in soup.find_all('p'):
#         st.write(p.text)

from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
import streamlit as st
import time

# 🧩 Install and setup driver only once
chromedriver_autoinstaller.install()
if "driver" not in st.session_state:
    st.session_state.driver = webdriver.Chrome()

st.title("🌐 Wikipedia Info Finder")
st.markdown("Enter any name below to automatically find and display Wikipedia details.")


name = st.text_input("🔍 Enter the name").strip().replace(" ", '+')

if st.button("🔎 Find Details"):
    if not name:
        st.warning("⚠️ Please enter a name before searching.")
    else:
        links = f'https://www.google.com/search?q={name}+wikipedia'
        with st.spinner("Searching on Google... Please wait ⏳"):
            st.session_state.driver.get(links)
            soup = BeautifulSoup(st.session_state.driver.page_source, 'html.parser')

            # Find Wikipedia link
            link = None
            for i in soup.find_all('div'):
                try:
                    link_temp = i.find('a', href=True)
                    if link_temp and 'en.wikipedia.org' in link_temp['href']:
                        link = link_temp
                        st.session_state.link = link_temp['href']
                        break
                except:
                    pass

            time.sleep(1.5)

        if link:
            st.success(f"✅ Wikipedia link found: [{link['href']}]({link['href']})")
            st.info("Click the **Visit Wikipedia Page** button below to see full details.")
        else:
            st.error("❌ No Wikipedia link found. Try another name.")

# Visit and show Wikipedia details
if "link" in st.session_state and st.button("📖 Visit Wikipedia Page"):
    with st.spinner("Fetching data from Wikipedia... Please wait ⏳"):
        person_link = st.session_state.link
        st.session_state.driver.get(person_link)
        soup = BeautifulSoup(st.session_state.driver.page_source, 'html.parser')
        paragraphs = [p.text.strip() for p in soup.find_all('p') if p.text.strip()]

    # output box for details
    st.markdown("### 🧾 Extracted Wikipedia Details:")
    st.markdown(
        f"""
        <div style="
             background-color: rgba(255, 255, 255, 0.05); /* light transparent background */
            color: inherit;
            padding:15px;
            height:400px;
            overflow-y:scroll;
            border-radius:10px;
            color:solid black;
        ">
        {'<br><br>'.join(paragraphs)}
        </div>
        """,
        unsafe_allow_html=True
    )
