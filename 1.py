import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
netflix_data = pd.read_csv('/Users/zhang/Desktop/电影推荐系统/netflix_titles.csv')
netflix_data.head(5) # 显示前5行
netflix_data.info() # 探索数据集。
netflix_data.describe() # 现在我们来读取数据集的基本统计信息。
# 转换数据类型。
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')
# 转换数据类型。
netflix_data['duration'] = pd.to_numeric(netflix_data['duration'].str.extract('(\d+)', expand=False), errors='coerce')
netflix_data.isnull().sum() # 检查缺失值。
# 用最常见的国家填充缺失值。
most_common_country = netflix_data['country'].mode()[0]
netflix_data['country'].fillna(most_common_country, inplace=True)
# 用“Not Available”填充缺失值。
netflix_data['cast'].fillna('Not Available', inplace=True)
netflix_data['director'].fillna('Not Available', inplace=True)
# 检查缺失值
missing_values = netflix_data['rating'].isnull()
(netflix_data[missing_values])
# 填补 'title' 列中的缺失值
netflix_data.loc[netflix_data['title'] == '13TH: A Conversation with Oprah Winfrey & Ava DuVernay', 'rating'] = 'U/A 13+'
netflix_data.loc[netflix_data['title'] == 'Gargantia on the Verdurous Planet', 'rating'] = 'TV-14'
netflix_data.loc[netflix_data['title'] == 'Little Lunch', 'rating'] = 'TV-G'
netflix_data.loc[netflix_data['title'] == 'My Honor Was Loyalty', 'rating'] = 'PG-13'
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']
# 创建评级分布的柱状图
plt.figure(figsize=(10, 6))
sns.countplot(x ='rating', data = netflix_data, order = netflix_data['rating'].value_counts().index) # 创建评级列的图表
plt.title('评级分布')  # 标题。
plt.xlabel('评级') # x轴标签。
plt.xticks(rotation=45, ha='right')
plt.ylabel('数量') # y轴标签。
plt.figure(figsize=(8, 5))
plt.pie(movies_shows,labels=movies_shows.index,  autopct='%1.1f%%', colors = ['green', 'red']) # 创建饼图。
plt.title('电影和电视节目数量') # 标题。
plt.show()
# 计算前十个国家
top_countries = netflix_data['country'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Blues_r') # 创建前十个国家的图表。
plt.title('Netflix 上制作内容最多的国家') # 标题
plt.xlabel('作品数量') # x轴标签
plt.ylabel('国家') # y轴标签
plt.show()
# 创建电影和电视节目发布数量的统计
release_count = netflix_data.groupby(['release_year', 'type']).size().reset_index(name='数量')
plt.figure(figsize=(12, 6))
sns.lineplot(x='release_year', y='数量', hue='type', marker='X', data=release_count,
palette='Set2') # 创建图表。
plt.title('Netflix 上电影和电视节目随时间的趋势') # 标题。
plt.xlabel('release_year') # x轴标签。
plt.ylabel('发布数量') # y轴标签。
plt.legend(title='type') # 图例。
plt.show()
# 画图部分
df_cast = netflix_data.copy()
df_cast['cast'] = df_cast['cast'].str.strip()

top_10_actor_movie = df_cast[(df_cast['type'] == 'Movie') & (df_cast['cast'] != 'unknown cast')].groupby('cast')['title'].count().sort_values(ascending=False).iloc[:10]
plt.figure(figsize=(10,8))
sns.barplot(x=top_10_actor_movie.index, y=top_10_actor_movie.values, order=top_10_actor_movie.index)
plt.xlabel('演员')
plt.ylabel('电影数量')
plt.title('最受欢迎的电影演员')
plt.xticks(rotation=90)
plt.show()

top_10_actor_Tv_show = df_cast[(df_cast['type'] == 'TV Show') & (df_cast['cast'] !=
'unknown cast')].groupby('cast')['title'].count().sort_values(ascending=False).iloc[:10]
plt.figure(figsize=(10,8))
sns.barplot(x=top_10_actor_Tv_show.index, y=top_10_actor_Tv_show.values, order=top_10_actor_Tv_show.index)
plt.xlabel('演员')
plt.ylabel('电视节目数量')
plt.title('最受欢迎的电视节目演员')
plt.xticks(rotation=90)
plt.show()

top_10_director_movie = netflix_data[(netflix_data['type'] == 'Movie') & (netflix_data['director'] != 'unknown director')].groupby('director')['title'].count().sort_values(ascending=False).iloc[:10]
plt.figure(figsize=(10,8))
sns.barplot(x=top_10_director_movie.index, y=top_10_director_movie.values, order=top_10_director_movie.index)
plt.xlabel('导演')
plt.ylabel('电影数量')
plt.title('最受欢迎的电影导演')
plt.xticks(rotation=90)
plt.show()
top_10_director_Tv_show = netflix_data[(netflix_data['type'] == 'TV Show') & (netflix_data['director'] != 'unknown director')].groupby('director')['title'].count().sort_values(ascending=False).iloc[:10]
plt.figure(figsize=(10,8))
sns.barplot(x=top_10_director_Tv_show.index, y=top_10_director_Tv_show.values, order=top_10_director_Tv_show.index)
plt.xlabel('导演')
plt.ylabel('电视节目数量')
plt.title('最受欢迎的电视节目导演')
plt.xticks(rotation=90)
plt.show()
