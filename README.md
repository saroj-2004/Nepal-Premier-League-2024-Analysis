# Nepal Premier League 2024 Data Analysis & Interactive Dashboard

## Project Overview

This project provides a comprehensive data analysis of the inaugural Nepal Premier League (NPL) T20 cricket tournament held in 2024. Using real match data, it explores batting, bowling, fielding, partnerships, wicketkeeping, and match summaries through interactive visualizations and statistical summaries.

A modern, interactive dashboard is also available, allowing users to explore the data visually and intuitively.

---

## Key Features

- **Batting Analysis:** Top run scorers, averages, strike rates, hundreds, fifties, boundaries, ducks, and performance distributions.
- **Bowling Analysis:** Top wicket-takers, economy rates, bowling averages, and four/five-wicket hauls.
- **Fielding Analysis:** Most catches, catch distributions, and fielding impact.
- **Partnership Analysis:** Highest partnerships by runs/wickets, team-wise partnership stats.
- **Wicketkeeping:** Most dismissals, catches, stumpings, and their distributions.
- **Final Match Analysis:** Run progression, runs per over, boundary heatmaps, batsmen contributions, wicket fall timelines, and shot direction frequencies.
- **Interactive Visualizations:** Built with Plotly and Streamlit for deep data exploration.
- **Web Dashboard:** Explore the data live at [nepalpremiereleague.streamlit.app](https://nepalpremiereleague.streamlit.app/)

---

## Technologies Used

- **Python** (Pandas, Plotly, Streamlit)
- **Jupyter Notebook** ([Nepal_Premier_League_2024_Analysis.ipynb](Nepal_Premier_League_2024_Analysis.ipynb))
- **CSV Data Files** (organized by record type)

---

## Project Structure

- [`app.py`](app.py): Streamlit dashboard application.
- [`requirements.txt`](requirements.txt): Python dependencies for the dashboard.
- [`Nepal_Premier_League_2024_Analysis.ipynb`](Nepal_Premier_League_2024_Analysis.ipynb): Main analysis notebook.
- `Batting Records/`: Batting statistics CSVs (e.g., most_runs.csv, most_fifties.csv).
- `Bowling Records/`: Bowling statistics CSVs (e.g., most_wickets.csv).
- `Fielding Records/`: Fielding statistics CSVs (e.g., most_catches.csv).
- `Final Tables/`: Points tables and final match data.
- `Partnership Records/`: Partnership statistics.
- `Player Averages/`: Player average statistics.
- `Team Records/`: Team performance statistics.
- `WicketKeepingRecords/`: Wicket-keeping statistics.

---

## How to Run the Dashboard Locally

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Nepal_Premier_League_Analysis.git
   cd Nepal_Premier_League_Analysis
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
4. **Open your browser:**  
   Visit [http://localhost:8501](http://localhost:8501) to interact with the dashboard.

---

## Try the Live Dashboard

**No installation needed!**  
👉 [Open the dashboard on Streamlit Cloud](https://nepalpremiereleague.streamlit.app/)

---

## Example Visualizations

- Bar charts for top run scorers, wicket-takers, and fielders.
- Scatter plots for runs vs. strike rate, catches vs. matches.
- Pie charts for run contributions.
- Heatmaps for boundary frequencies.
- Radar charts for shot direction analysis.
- Line and histogram plots for distributions and trends.

---

## Future Improvements

- Add advanced analytics (e.g., player impact scores, win probability).
- Integrate dashboards for live data exploration.
- Expand to multi-season analysis.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for suggestions or improvements.

---

## License

This project is licensed under the MIT License.

---

## Contact

- **Author:** Sangam Paudel
- **Email:** sangampaudel530@gmail.com
- **GitHub:** [sangampaudel530](https://github.com/sangampaudel530)

---

**If you found this project useful, please give it a star**