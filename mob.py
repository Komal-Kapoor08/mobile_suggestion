import streamlit as st

import pickle





st.title('Mobile Configration for customer')
st.sidebar.title('Input here whatever you want')

Brand = st.sidebar.selectbox('Which Brand of Phone you are Looking for (0 -APPLE,1-Motorola,2-One plus, 3-Oppo, 4-Realme, 5-Redmi, 6-Samsung, 7-Vivo)',[0,1,2,3,4,5,6,7])
RAM = st.sidebar.selectbox('How Much RAM do you want in a phone?',[8,12,16,12,12,12,16,16,16])
Storage = st.sidebar.selectbox('How Much Storage do you Need ?', [128,256,512,256,256,512,512,512])
Camera = st.sidebar.selectbox('How many Megapixels do you want in a camera ?',[48,200,50,50,200,50,50,50])
Battery = st.sidebar.selectbox('How much Battery Backup do you want ?',[3274,5000,5400,4600,5000,5400,5000,5400])

with open('mob.pkl','rb') as f:
    model = pickle.load(f)

if st.sidebar.button('Submit', key = 'Submit_button'):
    input_data = [[RAM,Storage,Camera,Battery]]
    find = model.predict(input_data)


    if find[0] == 0:
        st.success('suggested phone : APPLE')
    elif find[0] ==1:
        st.success('suggested phone : Motorola')
    elif find[0] ==2:
        st.success('suggested phone : One plus')
    elif find[0] ==3:
        st.success('suggested phone : OPPO')
    elif find[0] ==4:
        st.success('suggested phone : Realme')
    elif find[0] ==5:
        st.success('suggested phone : Redmi')
    elif find[0] ==6:
        st.success('suggested phone : Samsung')
    elif find[0] ==7:
        st.success('suggested phone : Vivo')
    else:
        st.warning('Not Available')

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


