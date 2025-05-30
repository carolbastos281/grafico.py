import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
# Carregar dados
df = pd.read_csv("global_street_food.csv")
st.title("Análise de Comida de Rua Global")
# ==========================
# Nuvem de Palavras
# ==========================
st.subheader("Nuvem de Palavras de Ingredientes")
text = " ".join(str(ingredient) for ingredient in df['Ingredients'].dropna())
stopwords = set(STOPWORDS)
stopwords.update(["garnish", "sauce", "served", "with", "and", "fresh", "powder", "chopped", "ground", "leaves", "optional"])
wordcloud = WordCloud(
   width=800,
   height=400,
   background_color='white',
   stopwords=stopwords,
   min_font_size=10,
   colormap='viridis',
   collocations=False
).generate(text)
fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis("off")
st.pyplot(fig_wc)
# ==========================
# Gráfico de Barras
# ==========================
st.subheader("Preço Médio por Número de Ingredientes")
df['Num_Ingredients'] = df['Ingredients'].apply(lambda x: len([item.strip() for item in str(x).split(',') if item.strip()]))
average_price_by_ingredients = df.groupby('Num_Ingredients')['Typical Price (USD)'].mean().reset_index()
average_price_by_ingredients = average_price_by_ingredients.sort_values('Num_Ingredients')
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
sns.barplot(data=average_price_by_ingredients, x='Num_Ingredients', y='Typical Price (USD)', ax=ax_bar, palette='coolwarm')
ax_bar.set_title('Preço Médio (USD) por Número de Ingredientes')
ax_bar.set_xlabel('Número de Ingredientes')
ax_bar.set_ylabel('Preço Médio Típico (USD)')
ax_bar.grid(axis='y', linestyle='--')
st.pyplot(fig_bar)
st.write("Dados do preço médio por número de ingredientes:")
st.dataframe(average_price_by_ingredients)


