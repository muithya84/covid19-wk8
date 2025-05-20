# covid19-wk8
a simple data analysis notebook
#  Global COVID-19 Data Analysis Project

This project presents a comprehensive data analysis of the COVID-19 pandemic using real-world data. It tracks global trends in cases, deaths, and vaccinations, and provides insights using Python data tools and visualizations.

---

##  Objectives

- ✅ Import and clean COVID-19 data from [Our World in Data](https://ourworldindata.org/coronavirus)
- ✅ Analyze time trends of cases, deaths, and vaccinations
- ✅ Compare statistics across selected countries (e.g., Kenya, USA, India)
- ✅ Visualize trends with line charts, bar graphs, and choropleth maps
- ✅ Communicate findings in a clear and insightful report format

---

##  Dataset

- **Source:** [OWID COVID-19 Dataset (CSV)](https://covid.ourworldindata.org/data/owid-covid-data.csv)
- **Columns Used:**  
  `date`, `location`, `total_cases`, `new_cases`, `total_deaths`, `total_vaccinations`, `people_fully_vaccinated`, `population`

---

##  Features & Visualizations

- **Line charts**: Total cases, new daily cases, death rates
- **Bar charts**: Vaccination percentage comparisons
- **Choropleth map**: Total cases by country (optional, interactive with Plotly)
- **Markdown insights**: Summary of findings in notebook narrative

---

##  Tech Stack

| Tool           | Purpose                           |
|----------------|-----------------------------------|
| Python         | Core language                     |
| Pandas         | Data loading & cleaning           |
| Matplotlib     | Line and bar chart visualizations |
| Seaborn        | Enhanced visual styling           |
| Plotly         | Choropleth map visualization      |
| Jupyter        | Interactive notebook environment  |

---

## 🔍 How to Run

1. Clone this repository or download the notebook/script.
2. Install dependencies (optional via `requirements.txt`):
    ```bash
    pip install pandas matplotlib seaborn plotly
    ```
3. Run the notebook:
    - Via Jupyter Notebook:  
      `jupyter notebook covid19_analysis.ipynb`
    - Or run script directly (if `.py` file):  
      `python covid19_analysis_full_notebook.py`

---

##  Example Insights

-  India and USA recorded significantly higher total cases than Kenya.
-  The USA had the fastest full vaccination rollout among selected countries.
-  Death rates showed notable spikes in mid-2021, especially in the USA.
-  Global case distribution can be visualized using an interactive choropleth map.

---

##  Deliverables

- `covid19_analysis_full_notebook.py` – Main analysis script
- `README.md` – Project overview and usage
- (Optional) `covid19_analysis.ipynb` – Jupyter version with markdown insights
- (Optional) `requirements.txt` – Python dependencies

---

##  License

This project is open-source and free to use for learning and research.  
Please credit the [OWID dataset](https://ourworldindata.org/coronavirus-source-data) when publishing results.

---

##  Acknowledgments

- [Our World in Data](https://ourworldindata.org/) for making comprehensive COVID-19 data available.
- The global data science community for tools and inspiration.

