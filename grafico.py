import pandas as pd
import matplotlib.pyplot as plt
import streamit as st

df = pd.read_csv("global_street_food.csv")
df
import pandas as pd #nao precisava importar de novo 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = "global_street_food.csv"
df = pd.read_csv(file_path)

text = " ".join(str(ingredient) for ingredient in df['Ingredients'].dropna())

stopwords = set(STOPWORDS)
stopwords.update(["garnish", "sauce", "served", "with", "and", "fresh", "powder", "chopped", "ground", "leaves", "optional"])
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=stopwords,
    min_font_size=10,
    colormap='viridis',  #cores
    collocations=False 
).generate(text)

# para ver a imagem gerada
plt.figure(figsize=(10, 5), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
import matplotlib.pyplot as plt 
import seaborn as sns

#sei que nao precisa dessa parte, mas coloquei para ficar organizado
file_path = "global_street_food.csv"
df = pd.read_csv(file_path)

#número de ingredientes
df['Num_Ingredients'] = df['Ingredients'].apply(lambda x: len([item.strip() for item in str(x).split(',') if item.strip()]))
average_price_by_ingredients = df.groupby('Num_Ingredients')['Typical Price (USD)'].mean().reset_index()

#número de ingredientes para o gráfico de barras
average_price_by_ingredients = average_price_by_ingredients.sort_values('Num_Ingredients')


plt.close('all') 
plt.figure(figsize=(10, 6))
sns.barplot(data=average_price_by_ingredients, x='Num_Ingredients', y='Typical Price (USD)', palette='coolwarm', hue='Num_Ingredients', dodge=False)

#remove a legenda 
if plt.gca().get_legend() is not None:
    plt.gca().get_legend().remove()

plt.title('Preço Médio (USD) por Número de Ingredientes')
plt.xlabel('Número de Ingredientes')
plt.ylabel('Preço Médio Típico (USD)')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.savefig("preco_medio_vs_num_ingredientes_bar_v2.png") # Nome do arquivo alterado para v2
plt.show()

write("\nDados do preço médio por número de ingredientes:")
write(average_price_by_ingredients)

