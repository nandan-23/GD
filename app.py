import streamlit as st
import pandas as pd
import ast
import plotly.express as px
from textblob import TextBlob

# Load the Excel files
topics_df = pd.read_excel('topics_list.xlsx')
tweets_df = pd.read_excel('Filtered_True_vals_with_dates.xlsx')

# Preprocess the data
tweets_df['LLama_candidates_NEW'] = tweets_df['LLama_candidates_NEW'].apply(ast.literal_eval)
tweets_df['Date'] = pd.to_datetime(tweets_df['Date'])

topics_df['Topic'] = topics_df['Topic'].str.lower().str.strip()
tweets_df['LLama_candidates_NEW'] = tweets_df['LLama_candidates_NEW'].apply(lambda x: [topic.lower().strip() for topic in x])

# Find the earliest and latest tweet dates
earliest_date = tweets_df['Date'].min()
latest_date = tweets_df['Date'].max()

# Function to filter tweets by topic
def filter_tweets_by_topic(topic):
    return tweets_df[tweets_df['LLama_candidates_NEW'].apply(lambda x: topic in x)]

# Function to get the frequency of tweets over time for a given topic, grouped by weeks
def get_topic_frequency_over_time(topic):
    filtered_tweets = filter_tweets_by_topic(topic)
    frequency = filtered_tweets.groupby(filtered_tweets['Date'].dt.to_period('W')).size().reset_index(name='Frequency')
    frequency['Date'] = frequency['Date'].dt.to_timestamp()
    frequency['Topic'] = topic  # Add a column to identify the topic
    return frequency

# Function to perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Function to get sentiment distribution for a topic
def get_sentiment_distribution(topic):
    filtered_tweets = filter_tweets_by_topic(topic)
    filtered_tweets['Sentiment'] = filtered_tweets['TextofThePost'].apply(get_sentiment)
    sentiment_distribution = filtered_tweets['Sentiment'].value_counts().reset_index()
    sentiment_distribution.columns = ['Sentiment', 'Count']
    return sentiment_distribution

# Function to get up to 5 tweets for a topic
def get_sample_tweets(topic, num_tweets=5):
    filtered_tweets = filter_tweets_by_topic(topic)
    sample_tweets = filtered_tweets[['Date', 'TextofThePost']].head(num_tweets)
    return sample_tweets

# Extract unique topics from the tweets dataframe
unique_topics = tweets_df['LLama_candidates_NEW'].explode().unique()

# Streamlit app
st.set_page_config(layout="wide")  # Set the layout to wide
st.title("Tweet Frequency and Sentiment Analysis by Topic")

# Multiselect for selecting topics
selected_topics = st.multiselect('Select topics:', unique_topics, default=[])

# Initialize or update the session state for added topics
if 'added_topics' not in st.session_state:
    st.session_state.added_topics = []

if selected_topics:
    st.session_state.added_topics = list(set(selected_topics))

# Get frequency data for the added topics
all_frequency_df = pd.DataFrame()
for topic in st.session_state.added_topics:
    frequency_df = get_topic_frequency_over_time(topic)
    all_frequency_df = pd.concat([all_frequency_df, frequency_df])

# Plot the data if there are topics added
if not all_frequency_df.empty:
    fig = px.line(all_frequency_df, x='Date', y='Frequency', color='Topic', title='Tweet Frequency for Selected Topics', markers=True)
    fig.update_xaxes(range=[earliest_date, latest_date], dtick="W1", tickformat="%d-%b-%Y")
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=earliest_date, dtick=604800000), height=600)  # Adjust height and width for a larger graph
    st.plotly_chart(fig, use_container_width=True)  # Ensure the graph uses the full container width
else:
    st.write("No topics selected. Please select topics to visualize.")

# Sentiment Analysis Section
st.sidebar.title("Sentiment Analysis")

if len(st.session_state.added_topics) == 1:
    selected_sentiment_topic = st.session_state.added_topics[0]
else:
    selected_sentiment_topic = st.sidebar.selectbox('Select a topic for sentiment analysis:', st.session_state.added_topics)

if selected_sentiment_topic:
    total_tweets = len(filter_tweets_by_topic(selected_sentiment_topic))
    st.sidebar.write(f"Total tweets for {selected_sentiment_topic}: {total_tweets}")

    sentiment_distribution = get_sentiment_distribution(selected_sentiment_topic)
    fig_sentiment = px.pie(sentiment_distribution, values='Count', names='Sentiment', title=f'Sentiment Distribution for {selected_sentiment_topic}')
    st.sidebar.plotly_chart(fig_sentiment)

    st.sidebar.title(f'Top 5 Tweets for {selected_sentiment_topic}')
    sample_tweets = get_sample_tweets(selected_sentiment_topic)
    for i, row in sample_tweets.iterrows():
        st.sidebar.write(f"{row['Date']}: {row['TextofThePost']}")
else:
    st.sidebar.write("No topic selected for sentiment analysis.")
