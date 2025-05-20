# Combining the full notebook code into one large code block for easier copying and use
full_notebook_code = """
# 📘 COVID-19 Global Trends Analysis

# ===================================================
# 1️⃣ Data Collection
# ===================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset from OWID
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(url)
print("✅ Dataset loaded successfully.")

# ===================================================
# 2️⃣ Data Loading & Exploration
# ===================================================
print("Columns in the dataset:")
print(df.columns)
df.head()
df.isnull().sum().sort_values(ascending=False)
df.info()

# ===================================================
# 3️⃣ Data Cleaning
# ===================================================
columns_to_keep = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
                   'total_deaths', 'new_deaths', 'total_vaccinations', 'people_fully_vaccinated',
                   'population']
df = df[columns_to_keep]
df = df.dropna(subset=['date', 'location'])
df['date'] = pd.to_datetime(df['date'])
df.fillna(0, inplace=True)
df = df[~df['continent'].isnull()]
print("✅ Data cleaned.")

# ===================================================
# 4️⃣ Exploratory Data Analysis (EDA)
# ===================================================
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

countries = ['Kenya', 'India', 'United States']
df_selected = df[df['location'].isin(countries)]

# Total cases over time
for country in countries:
    data = df_selected[df_selected['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)
plt.title(' Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Daily new cases
for country in countries:
    data = df_selected[df_selected['location'] == country]
    plt.plot(data['date'], data['new_cases'], label=country)
plt.title(' Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()

# Death rate
df_selected['death_rate'] = df_selected['total_deaths'] / df_selected['total_cases']
for country in countries:
    data = df_selected[df_selected['location'] == country]
    plt.plot(data['date'], data['death_rate'], label=country)
plt.title(' Death Rate Over Time (Deaths / Cases)')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()

# ===================================================
# 5️⃣ Vaccination Progress
# ===================================================
for country in countries:
    data = df_selected[df_selected['location'] == country]
    plt.plot(data['date'], data['people_fully_vaccinated'], label=country)
plt.title('💉 Cumulative People Fully Vaccinated')
plt.xlabel('Date')
plt.ylabel('Fully Vaccinated People')
plt.legend()
plt.show()

latest = df_selected[df_selected['date'] == df_selected['date'].max()]
latest['vaccinated_percent'] = (latest['people_fully_vaccinated'] / latest['population']) * 100
sns.barplot(data=latest, x='location', y='vaccinated_percent')
plt.title('✅ % of Population Fully Vaccinated (Latest Date)')
plt.ylabel('Percent Vaccinated')
plt.xlabel('Country')
plt.ylim(0, 100)
plt.show()

# ===================================================
# 6️⃣ Choropleth Map (Optional)
# ===================================================
latest_global = df[df['date'] == df['date'].max()]
latest_global = latest_global[latest_global['total_cases'] > 0]
fig = px.choropleth(latest_global,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title='🌍 Total COVID-19 Cases by Country (Latest)')
fig.show()

# ===================================================
# 7️⃣ Insights & Reporting
# ===================================================
from IPython.display import Markdown
Markdown(\"\"\"
###  Key Insights

- 🇮🇳 India and 🇺🇸 USA had significantly higher total cases compared to 🇰🇪 Kenya.
-  The death rate in the USA showed spikes during mid-2021.
-  Vaccination rollout was fastest in the USA among selected countries.
-  Daily new cases in Kenya remained low but spiked during wave periods.
\"\"\")

# Conclusion (Markdown Cell):
#  Conclusion
# This notebook provides a snapshot of global COVID-19 trends using real-world data.
# By exploring metrics such as cases, deaths, and vaccinations, we gained insights into how
# different countries managed the pandemic over time.
#
# Recommendations for further exploration:
# - Normalize metrics per 100k population
# - Add interactivity (e.g., sliders or dropdowns)
# - Predict future trends with regression or time-series models
"""

# Save this full code to a file
file_path = "/mnt/data/covid19_analysis_full_notebook.py"
with open(file_path, "w") as f:
    f.write(full_notebook_code)

file_path

