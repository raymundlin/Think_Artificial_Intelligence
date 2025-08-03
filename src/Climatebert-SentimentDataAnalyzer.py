# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenterated by GPT-4, from the following prompt
# Prompt: Bar chart visualizing data from 'climatebert-climate-sentiment.csv', depicting normalized sentiment label distribution, categorized into 'Risk', 'Neutral', and 'Opportunity'.
#
# About: This script visualizes the distribution of sentiment labels in a dataset as a bar chart,
# with proportions annotated on each bar, using Python's pandas and matplotlib libraries.
#
# Setup: Python installed, with 'climatebert-climate-sentiment.csv' in your directory. 
# Install pandas and matplotlib using 'pip install pandas matplotlib' for data processing and visualization.
#
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../datasets/climatebert-climate-sentiment.csv')

# Summarize and plot the distribution of sentiment labels
label_distribution = data['label'].value_counts(normalize=True)
ax = label_distribution.plot(kind='bar', color='#125740', edgecolor='black', ylim=(0, label_distribution.max() * 1.1))
# plt.xlabel('Sentiment Labels')
plt.xlabel('態度標籤')
# plt.ylabel('Proportion')
plt.ylabel('比例')
# plt.title('Distribution of Sentiment Labels')
plt.title('態度標籤分佈')
plt.xticks(ticks=[0, 1, 2], labels=['風險 (0)', '中立 (1)', '機會 (2)'], rotation=0)
plt.grid(True, linestyle='--', linewidth=0.5)

# Annotate bars with percentages
for p in ax.patches:
    ax.annotate(f"{p.get_height():.2%}", (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# plt.show()

# Save the plot as an image
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
plt.savefig('C06-F06-ClimateBert_Sentiment_Graph.png', dpi=1200, bbox_inches='tight')

