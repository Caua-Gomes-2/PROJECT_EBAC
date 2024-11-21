import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Análise descritiva das colunas numéricas
print(df[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].describe())

# Histograma das Notas
plt.figure(figsize=(10, 6))
sns.histplot(df['Nota'], bins=20, kde=True)
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid()
plt.show()

# Gráfico de Dispersão entre Preço e Nota
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Preço', y='Nota', hue='Marca', alpha=0.7)
plt.title('Relação entre Preço e Nota dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Nota')
plt.legend(title='Marca')
plt.grid()
plt.show()

# Gráfico de Barra: Número de Avaliações por Marca
plt.figure(figsize=(12, 6))
df.groupby('Marca')['N_Avaliações'].sum().sort_values().plot(kind='barh')
plt.title('Número Total de Avaliações por Marca')
plt.xlabel('Número de Avaliações')
plt.ylabel('Marca')
plt.grid()
plt.show()

# Gráfico de Pizza: Distribuição de Produtos por Gênero
plt.figure(figsize=(8, 8))
df['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Produtos por Gênero')
plt.ylabel('')
plt.show()

# Gráfico de Densidade do Preço
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True)
plt.title('Densidade dos Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.grid()
plt.show()

# Gráfico de Regressão: Preço vs. Desconto
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Preço', y='Desconto', scatter_kws={'alpha':0.5})
plt.title('Relação entre Preço e Desconto')
plt.xlabel('Preço (R$)')
plt.ylabel('Desconto (%)')
plt.grid()
plt.show()