import pandas as pd
import streamlit as st
import matplotlib as plt
import re

df  = pd.read_csv('School_Attendance_by_School__2020-2021.csv')
df2 = pd.read_csv('CAPT_School_Performance__2010-2012.csv')
df3 = pd.read_csv('Education_Directory.csv')
df4 = pd.read_csv('Statewide_CMT_8th_Grade_Reading_and_Math__2007-2013.csv')
df5 = pd.read_csv('College_Enrollment__Credit_Attainment_and_Remediation_of_High_School_Graduates_by_School.csv')
df6 = pd.read_csv('School_Attendance_by_District__2022-2023.csv')
df7 = pd.read_csv('smarterbalancedallstudents2015-2019byperformance.csv')
df8 = pd.read_csv('CAPT_School_Performance__2013.csv')




st.title('Education Observations')
st.markdown('---')


cols = ['District Name', 'Location']
df_short = df3.loc[:100, cols].dropna(0)
def parse_latitude(location):
    m = re.findall(r'-*\d+\.-*\d+(?=,)', str(location))
    return None if m == None or len(m) == 0 else float(m[0])
def parse_longitude(location):
    m = re.findall(r'(?<=, )-*\d+\.-*\d+', str(location))
    return None if m == None or len(m) == 0 else float(m[0])

df_short = df_short.assign(lat=[parse_latitude(row) for row in df_short['Location']], lon=[parse_longitude(row) for row in df_short['Location']])
#st.dataframe(df_short, width=800, height=200)

st.map(df_short)


## Attendance rates ##
st.subheader('Attendance rates by District in Connecticut 2019 - 2021')
cols1 = ['District name','2019-2020 attendance rate','2020-2021 attendance rate - year to date','2019-2020 student count']
df_short = df.loc[:100, cols1]

st.dataframe(df_short, width = 800, height = 200)
st.markdown('---')

st.subheader('Attendance rates by District in Connecticut 2022 - 2023')
cols1 = ['District name','Overall 2021-2022 attendance rate','Overall 2022-2023 attendance rate - year to date']
df_short = df6.loc[:100, cols1]

st.dataframe(df_short, width = 800, height = 200)
st.markdown('---')


## Subjects for 8th grade math ##
st.subheader(' 8th math and reading grades (2007 - 2013) state wide')
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.scatter(df4['Year'], df4['Total Mathematics % Goal Range'], color ='red')
ax1.set_xlabel('Year')
ax1.set_ylabel('Mathematics grade')
ax1.set_title('Math')


fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.scatter(df4['Year'], df4['Total Reading % Goal Range'],color ='purple')
ax2.set_xlabel('Year')
ax2.set_ylabel('Reading grade')
ax2.set_title('Reading')


col2, col3 = st.columns(2)
with col2:
    st.pyplot(fig1)
    
with col3:
    st.pyplot(fig2)

st.markdown('---')

#CAPT School Performance 2010-2012


st.subheader('CAPT School Performance 2010-2012')

District = st.radio("What district would you like to look at?",('Bridgeport School District', 'Hartford School District','New Haven School District','Seymour School District'))
if District == 'Bridgeport School District':
    df2 = df2.loc[df2['District Name'] == 'Bridgeport School District']
elif District == 'Hartford School District':
    df2 = df2.loc[df2['District Name'] == 'Hartford School District']
elif District == 'New Haven School District':
     df2 = df2.loc[df2['District Name'] == 'New Haven School District']
else:
    df2 = df2.loc[df2['District Name'] == 'Seymour School District']

fig3 = plt.figure()
ax3= fig3.add_subplot()
ax3.set_xlabel('Overall SPI OVERALL 2010')
ax3.hist(df2['Overall SPI OVERALL 2010'])


fig4 = plt.figure()
ax4= fig4.add_subplot()
ax4.set_xlabel('Overall SPI OVERALL 2011')
ax4.hist(df2['Overall SPI OVERALL 2011'])


fig5 = plt.figure()
ax5= fig5.add_subplot()
ax5.set_xlabel('Overall SPI OVERALL 2012')
ax5.hist(df2['Overall SPI OVERALL 2012'])


col3, col4, col5 = st.columns(3)
with col3:
    st.pyplot(fig3)
    
with col4:
    st.pyplot(fig4)

with col5:
    st.pyplot(fig5)

st.markdown('---')


#What subject did the best
st.subheader('CAPT School Performance 2013 compairing subjects')
District1 = st.radio("What district would you like to look at?",('Bridgeport School District', 'Hartford School District','New Haven School District','Derby School District'))
if District1 == 'Bridgeport School District':
    df8 = df8.loc[df8['District Name'] == 'Bridgeport School District']
elif District1 == 'Hartford School District':
    df8 = df8.loc[df8['District Name'] == 'Hartford School District']
elif District1 == 'New Haven School District':
     df8 = df8.loc[df8['District Name'] == 'New Haven School District']
else:
    df8 = df8.loc[df8['District Name'] == 'Derby School District']

fig6 = plt.figure()
ax6= fig6.add_subplot()
ax6.set_xlabel('SPI Math (2013')
ax6.hist(df8['SPI MATH 2013'])


fig7 = plt.figure()
ax7= fig7.add_subplot()
ax7.set_xlabel('Reading (2013)')
ax7.hist(df8['SPI READ 2013'])


fig8 = plt.figure()
ax8= fig8.add_subplot()
ax8.set_xlabel('Writing')
ax8.hist(df8['SPI WRITE 2013'])

fig9 = plt.figure()
ax9= fig9.add_subplot()
ax9.set_xlabel('Science (2013')
ax9.hist(df8['SPI SCIENCE 2013'])


col6, col7, col8,col9 = st.columns(4)
with col6:
    st.pyplot(fig6)
    
with col7:
    st.pyplot(fig7)

with col8:
    st.pyplot(fig8)

with col9:
    st.pyplot(fig9)


#college enrollment 
st.subheader('College enrollment')
cols7 = ['School Name','Graduating Class','Indicator','Value']
df_short = df5.loc[:100, cols7]

st.dataframe(df_short, width = 800, height = 200)
st.markdown('---')

