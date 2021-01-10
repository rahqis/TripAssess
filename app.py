import streamlit as st
import wordsentimentsensor as wss
import articlegatherer as ag

sidebarTitle = st.sidebar.header("Saftey Check")

source = st.sidebar.selectbox(
    "Traveling From:",
    (
        "Afghanistan",
        "Albania",
        "Algeria",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bonaire, Sint, Eustatius, and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Brazil",
        "British Virgin Islands",
        "Brunei",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cape Verde",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Colombia",
        "Congo",
        "Costa Rica",
        "Cote d'Ivoire",
        "Croatia",
        "Cuba",
        "Curacao",
        "Cyprus",
        "Czech Republic",
        "Democratic Republic of Congo",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Ethiopia",
        "Faeroe Islands",
        "Falkland Islands",
        "Fiji",
        "Finland",
        "France",
        "French Polynesia",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Honduras",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kosovo",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Latvia",
        "Lebanon",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macedonia",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Mauritania",
        "Mauritius",
        "Mexico",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Romania",
        "Russia",
        "Rwanda",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Vincent and the Grenadines",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Somalia",
        "South Africa",
        "South Korea",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syria",
        "Taiwan",
        "Tanzania",
        "Thailand",
        "Timor",
        "Togo",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turks and Caicos Islands",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "United States Virgin Islands",
        "Uruguay",
        "Uzbekistan",
        "Vatican",
        "Venezuela",
        "Vietnam",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    ),
)

destination = st.sidebar.selectbox(
    "Traveling To:",
    (
        "Afghanistan",
        "Albania",
        "Algeria",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bonaire, Sint, Eustatius, and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Brazil",
        "British Virgin Islands",
        "Brunei",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cape Verde",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Colombia",
        "Congo",
        "Costa Rica",
        "Cote d'Ivoire",
        "Croatia",
        "Cuba",
        "Curacao",
        "Cyprus",
        "Czech Republic",
        "Democratic Republic of Congo",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Ethiopia",
        "Faeroe Islands",
        "Falkland Islands",
        "Fiji",
        "Finland",
        "France",
        "French Polynesia",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Honduras",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kosovo",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Latvia",
        "Lebanon",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macedonia",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Mauritania",
        "Mauritius",
        "Mexico",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Romania",
        "Russia",
        "Rwanda",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Vincent and the Grenadines",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Somalia",
        "South Africa",
        "South Korea",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syria",
        "Taiwan",
        "Tanzania",
        "Thailand",
        "Timor",
        "Togo",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turks and Caicos Islands",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "United States Virgin Islands",
        "Uruguay",
        "Uzbekistan",
        "Vatican",
        "Venezuela",
        "Vietnam",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    ),
)

mainTitle = st.title("Trip Assess")
hookText = st.header("Traveling?")
Explainatiion = st.subheader(
    "Before you do, use our Safety Check to gather all the safety information you need and check our SafetyMeter to have a stress free and great trip!"
)

# Top headlines on destination
# Top headlines' descriptions
topDestinationArticles = ag.collectTopArticles(destination)
topDescriptions = ag.gatherTopArticleDescriptions(topDestinationArticles)

# Top headlines on country relations
# Top headlines' descriptions on country relations
topRelationsArticles = ag.collectNationsRelationships(source, destination)
topRelationsDescriptions = ag.gatherRelationArticleDescriptions(topRelationsArticles)

# All articles on destinations based off relevancy
# Descriptions of all articles on destination based off relevnacy
allDestinationArticles = ag.collectAllArticles(destination)
allDestinationDescriptions = ag.gatherAllArticleDescriptions(allDestinationArticles)

st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: yellow;
        }
    </style>""",
    unsafe_allow_html=True,
)

def SafetyMeter(topDescriptions, topRelationsDescriptions, allDestinationDescriptions):
    good = wss.positiveSentimentDetector(topDescriptions)
    good += wss.positiveSentimentDetector(topRelationsDescriptions)
    good += wss.positiveSentimentDetector(allDestinationDescriptions)
    good = good / 3

    neutral = wss.neutralSentimentDetector(topDescriptions)
    neutral += wss.neutralSentimentDetector(topRelationsDescriptions)
    neutral += wss.neutralSentimentDetector(allDestinationDescriptions)
    neutral = neutral / 3

    bad = wss.negativeSentimentDetector(topDescriptions)
    bad += wss.negativeSentimentDetector(topRelationsDescriptions)
    bad += wss.negativeSentimentDetector(allDestinationDescriptions)
    bad = bad / 3

    difference = abs(good - bad)
    #Reports  okay safety
    if neutral > 95 and difference < 2:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: yellow;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(50)
        st.subheader('Okay To Travel')
        st.write('Most news from ' + destination + ' seem neither too safe or too dangerous, indicating that there is relative stability and ease to travel.')
    elif neutral < 95 and bad > good + 2 and bad < good + 10:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: #ff9100;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(20)
        st.subheader('Possibly Dangerous')
        st.write('Most news from ' + destination + ' has more dangerous reports, indicating that, though possibly safe, it is preferable not to travel to ' + destination + '.')
    elif neutral <= 95 and bad >= good + 10:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: red;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(3)
        st.subheader('Too Dangerous!')
        st.write(destination + ' is too dangerous to travel to. Too much instability, conflict, or restlessness has occurred recently.')
    elif neutral < 95 and good > bad + 2 and good < bad + 10:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: #bfff00;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(80)
        st.subheader('Mostly Safe')
        st.write(destination + ' is mostly safe, according to the news. It may have some dangers, but ' + destination + ' is overall safe to travel to.')
    elif neutral <= 95 and good >= bad + 10:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: green;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(97)
        st.subheader('Very Safe')
        st.subheader(destination + ' is very safe recently and you should be ready to pack your bags and have a great trip!')
    else:
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
            background-color: yellow;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(50)
        st.subheader('Okay To Travel')
        st.write('Most news from ' + destination + ' seem neither too safe or too dangerous, indicating that there is relative stability and ease to travel.')


SafetyMeter(topDescriptions, topRelationsDescriptions, allDestinationDescriptions)
st.subheader("Top Headlines in " + destination)

for source in topDestinationArticles:
    with st.beta_container():
        st.header(source["title"])
        if source['urlToImage']:
            st.image(source['urlToImage'], caption=source['description'], use_column_width=True)

for source in allDestinationArticles:
    with st.beta_container():
        st.header(source["title"])
        if source['urlToImage']:
            st.image(source['urlToImage'], caption=source['description'], use_column_width=True)

for source in topRelationsArticles:
    with st.beta_container():
        st.header(source["title"])
        if source['urlToImage']:
            st.image(source['urlToImage'], caption=source['description'], use_column_width=True)
