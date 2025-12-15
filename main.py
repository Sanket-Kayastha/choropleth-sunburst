import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt


data = pd.read_csv("nobel_prize_data.csv")
# print(data)
# print(data.shape)
# print(data.tail())

# print(data.describe())
# print(f"There is any duplicacy: {data.duplicated().values.any()}")
# print(f"To check NaN vlues: {data.isna().values.any()}")
# print(data.isna().sum())
# col_subset = ['year','category', 'laureate_type',
#                 'birth_date','full_name', 'organization_name']
# print(data.loc[data.birth_date.isna()][col_subset])

# print(data.birth_date = pd.to_datetime(data.birth_date))
# print(data.head())
# biology = data.sex.value_counts()
# # print(biology)

# fig = px.pie(labels=biology.index, values=biology.values, title="Percentage of Male vs Female Winners",names=biology.index,hole=0.5)
# fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

# fig.show()
# top_three_women = data[data.sex == 'Female'].sort_values('year', ascending=True)[:3]
# print(top_three_women)

# is_winner = data.duplicated(subset=["full_name"], keep=False)
# multiple_winners = data[is_winner]
# print(f"There is {multiple_winners.full_name.nunique()}")
# col_subset = ['year', 'category', 'laureate_type', 'full_name']
# print(multiple_winners[col_subset])

# prizes = data.category.value_counts()
# # print(prizes)
# # print(prizes.index)
# v_bar = px.bar(
#     x=prizes.index,
#     y = prizes.values,
#     color=prizes.values,
#     color_continuous_scale='Aggrnyl',
#     title="Number of Prizes Awarded per Category"
# )
# v_bar.update_layout(xaxis_title="Nobel Prize Category", coloraxis_showscale=False, yaxis_title="Number of Prizes")
# v_bar.show()

# prize_per_year = data.groupby(by='year').count().prize
# moving_avg = prize_per_year.rolling(window=5).mean()
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(ticks=np.arange(1900,2021, step=5),
#            fontsize=14,
#            rotation=45)

# plt.scatter(x=prize_per_year.index,
#             y=prize_per_year.values,
#             c='dodgerblue',
#             alpha=0.7,
#             s=100,)

# plt.plot(prize_per_year.index,
#          moving_avg.values,
#          c='crimson',
#          linewidth=3)

# plt.show()

# top_countries = data.groupby(['birth_country_current'],as_index=False).agg({'prize':pd.Series.count})
# # print(top_countries)
# top_countries.sort_values(by='prize', inplace=True)
# top20_countries = top_countries[-20:]
# # print(top20_countries)
# h_bar = px.bar(x=top20_countries.prize,
#                y=top20_countries.birth_country_current,
#                orientation='h',
#                color=top20_countries.prize,
#                color_continuous_scale='Viridis',
#                title="Top 20 Countries by Number of Prizes")

# h_bar.update_layout(xaxis_title='Number of Prizes',
#                     yaxis_title ='Country',
#                     coloraxis_showscale=False)

# h_bar.show()

# df_countries = data.groupby(['birth_country_current', 'ISO'], as_index=False).agg({'prize':pd.Series.count})
# world_map = px.choropleth(df_countries,
#                           locations='ISO',
#                           color='prize',
#                           hover_name='birth_country_current',
#                           color_continuous_scale=px.colors.sequential.matter)

# world_map.show()

# top20_orgs = data.organization_name.value_counts()[:20]
# org_bar = px.bar(x=top20_orgs.values,
#                  y=top20_orgs.index,
#                  orientation='h',
#                  color=top20_orgs.values,
#                  title='Top 20 Research Institutions by Number of Prizes')

# org_bar.update_layout(xaxis_title='Number of Prizes',
#                       yaxis_title='Institution',
#                       coloraxis_showscale=False)

# org_bar.show()

# country_city_org = data.groupby(by=['organization_country','organization_city','organization_name'],as_index=False).agg({'prize':pd.Series.count})

# burst = px.sunburst(country_city_org,
#                     path=['organization_country','organization_city','organization_name'],values='prize', title='Where do Discoveries Take Place?')

# burst.update_layout(xaxis_title='Number of Prizes', yaxis_title='City', coloraxis_showscale=False)

# burst.show()

birth_years = data.birth_date.dt.year
data['winning_age'] = data.year - birth_years

print(data.winning_age.describe())
# display(data.nlargest(n=1, columns='winning_age'))