import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Nepal Premier League 2024 Dashboard", layout="wide")

# --- Data Loaders ---
@st.cache_data
def load_batting():
    path = os.path.join(os.getcwd(), "Batting Records", "most_runs.csv")
    return pd.read_csv(path)

@st.cache_data
def load_bowling():
    path = os.path.join(os.getcwd(), "Bowling Records", "most_wickets.csv")
    return pd.read_csv(path)

@st.cache_data
def load_fielding():
    path = os.path.join(os.getcwd(), "Fielding Records", "most_catches.csv")
    return pd.read_csv(path)

@st.cache_data
def load_partnerships():
    path = os.path.join(os.getcwd(), "Partnership Records", "highest_partnerships_by_runs.csv")
    return pd.read_csv(path)

@st.cache_data
def load_final():
    path = os.path.join(os.getcwd(), "Final Tables", "npl_final.csv")
    return pd.read_csv(path)

# --- Sidebar Filters ---
st.sidebar.image(
    "https://wicketnepal.com/wp-content/uploads/2024/11/468719762_122127843350455690_7601835368897814823_n.jpg",
    use_container_width=True
)
st.sidebar.title("NPL 2024 Interactive Dashboard")
st.sidebar.markdown("Filter and explore the stats!")

batting_df = load_batting()
bowling_df = load_bowling()
fielding_df = load_fielding()
partnership_df = load_partnerships()
final_df = load_final()

players = sorted(batting_df['player'].unique())
selected_player = st.sidebar.selectbox("Select Player (Batting)", ["All"] + players)

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏏 Batting", "🎯 Bowling", "🧤 Fielding", "🤝 Partnerships", "🏆 Final Match"
])

with tab1:
    st.header("Batting Analysis")
    df = batting_df.copy()
    df['runs'] = pd.to_numeric(df['runs'], errors='coerce')
    df['batting_average'] = pd.to_numeric(df['batting_average'], errors='coerce')
    df['strike_rate'] = pd.to_numeric(df['strike_rate'], errors='coerce')
    df['fifties_scored'] = pd.to_numeric(df['fifties_scored'], errors='coerce')
    df['hundreds_scored'] = pd.to_numeric(df['hundreds_scored'], errors='coerce')
    df['boundary_fours'] = pd.to_numeric(df['boundary_fours'], errors='coerce')
    df['boundary_sixes'] = pd.to_numeric(df['boundary_sixes'], errors='coerce')
    df['total_boundaries'] = df['boundary_fours'] + df['boundary_sixes']

    # Filter
    if selected_player != "All":
        df = df[df['player'] == selected_player]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 Run Scorers")
        top_runs = df.sort_values('runs', ascending=False).head(10)
        fig = px.bar(top_runs, x='player', y='runs', color='runs', color_continuous_scale='Blues', title='Top 10 Run Scorers')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Runs vs Strike Rate (All Players)")
        scatter_df = df[df['batting_average'].notna()].copy()
        if not scatter_df.empty:
            fig2 = px.scatter(
                scatter_df,
                x='strike_rate',
                y='runs',
                size='batting_average',
                hover_name='player',
                title='Runs vs Strike Rate',
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No data available for Runs vs Strike Rate plot.")

    st.subheader("Distribution of Batting Averages")
    fig3 = px.histogram(df, x='batting_average', nbins=15, color_discrete_sequence=['#ff6f61'])
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Most Boundaries (Fours + Sixes)")
    top_boundaries = df.sort_values('total_boundaries', ascending=False).head(10)
    fig4 = px.bar(top_boundaries, x='player', y='total_boundaries', color='total_boundaries', color_continuous_scale='Oranges')
    st.plotly_chart(fig4, use_container_width=True)

    st.dataframe(top_runs, use_container_width=True)

with tab2:
    st.header("Bowling Analysis")
    df = bowling_df.copy()
    df['wicket'] = pd.to_numeric(df['wicket'], errors='coerce')
    df['economy_rate'] = pd.to_numeric(df['economy_rate'], errors='coerce')
    df['bowling_average'] = pd.to_numeric(df['bowling_average'], errors='coerce')
    df['overs'] = pd.to_numeric(df['overs'], errors='coerce')

    st.subheader("Top 10 Wicket Takers")
    top_wickets = df.sort_values('wicket', ascending=False).head(10)
    fig = px.bar(top_wickets, x='player', y='wicket', color='wicket', color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Best Economy Rates (Min 20 Overs)")
    econ_bowlers = df[df['overs'] >= 20].sort_values('economy_rate').head(10)
    fig2 = px.bar(econ_bowlers, x='economy_rate', y='player', orientation='h', color='economy_rate', color_continuous_scale='Blues')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Bowling Average Distribution")
    fig3 = px.box(df[df['wicket'] >= 5], y='bowling_average', points="all", color_discrete_sequence=['#e67e22'])
    st.plotly_chart(fig3, use_container_width=True)

    st.dataframe(top_wickets, use_container_width=True)

with tab3:
    st.header("Fielding Analysis")
    df = fielding_df.copy()
    df['catches'] = pd.to_numeric(df['catches'], errors='coerce')

    st.subheader("Top 10 Fielders by Catches")
    top_catchers = df.sort_values('catches', ascending=False).head(10)
    fig = px.bar(top_catchers, x='player', y='catches', color='catches', color_continuous_scale='Teal')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribution of Catches Among Players")
    fig2 = px.histogram(df, x='catches', nbins=10, color_discrete_sequence=['#00b894'])
    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(top_catchers, use_container_width=True)

with tab4:
    st.header("Partnership Analysis")
    df = partnership_df.copy()
    df['runs'] = pd.to_numeric(df['runs'], errors='coerce')
    df['wickets'] = pd.to_numeric(df['wickets'], errors='coerce')

    st.subheader("Top 10 Highest Partnerships by Runs")
    top_part = df.sort_values('runs', ascending=False).head(10)
    fig = px.bar(top_part, x='partners', y='runs', color='wickets', color_continuous_scale='Plasma')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribution of Partnership Runs")
    fig2 = px.histogram(df, x='runs', nbins=20, color_discrete_sequence=['#6c5ce7'])
    st.plotly_chart(fig2, use_container_width=True)

    if 'team' in df.columns:
        st.subheader("Partnership Runs by Team")
        fig3 = px.box(df, x='team', y='runs', color='team', title='Partnership Runs by Team')
        st.plotly_chart(fig3, use_container_width=True)

    st.dataframe(top_part, use_container_width=True)

with tab5:
    st.header("Final Match Analysis")
    df = final_df.copy()
    df['ball_over'] = pd.to_numeric(df['ball_over'], errors='coerce')
    df['total_runs'] = pd.to_numeric(df['total_runs'], errors='coerce')
    df['inning'] = df['inning'].astype(str)

    st.subheader("Run Progression by Innings (Worm Plot)")
    df['cumulative_runs'] = df.groupby(['inning'])['total_runs'].cumsum()
    fig = px.line(df, x='ball_over', y='cumulative_runs', color='inning', markers=True,
                  title='Run Progression by Innings')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Runs Scored Per Over")
    df['over'] = df['ball_over'].astype(int)
    runs_per_over = df.groupby(['inning', 'over'])['total_runs'].sum().reset_index()
    fig2 = px.bar(runs_per_over, x='over', y='total_runs', color='inning', barmode='group', title='Runs Per Over')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Boundary Frequency Heatmap")
    if 'batsman_runs' in df.columns:
        df['is_boundary'] = df['batsman_runs'].isin([4, 6])
        boundary_heatmap = df[df['is_boundary']].groupby(['inning', 'over']).size().reset_index(name='boundary_count')
        fig3 = px.density_heatmap(boundary_heatmap, x='over', y='inning', z='boundary_count', color_continuous_scale='Inferno')
        st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Top Batsmen - Run Contribution (Pie)")
    if 'batsman' in df.columns and 'batsman_runs' in df.columns:
        top_batsmen = df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(6)
        fig4 = px.pie(names=top_batsmen.index, values=top_batsmen.values, hole=0.4, title='Top Batsmen Run Contribution')
        st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Wicket Fall Timeline")
    if 'player_dismissed' in df.columns:
        wickets = df[df['player_dismissed'].notna()].copy()
        if not wickets.empty:
            fig5 = px.scatter(wickets, x='ball_over', y='inning', color='dismissal_kind', symbol='dismissal_kind',
                              hover_data=['player_dismissed', 'bowler', 'fielder'], title='Wicket Fall Timeline')
            st.plotly_chart(fig5, use_container_width=True)

    st.dataframe(df.head(100), use_container_width=True)

st.markdown("---")
st.caption("Developed by Sangam Paudel | Nepal Premier League 2024 Dashboard")