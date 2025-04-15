import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ler CSV
df = pd.read_csv('C:/Users/william/Desktop/Curso/ecommerce_estatistica.csv')
print(df.head().to_string())
print(df.columns.tolist())

# Histograma com parametros
plt.figure(figsize=(10, 8))
plt.hist(df['Gênero'], bins=15, color='#00CED1')
plt.title('Histograma - Compra de roupas')
plt.xlabel('Gênero'), plt.xticks(rotation=90)
plt.ylabel('Frequencia')
plt.show()

# Grafico de dispersão

plt.figure(figsize=(10, 6))
plt.scatter(df['Qtd_Vendidos_Cod'], df['Desconto'], alpha=0.6)
plt.xscale('log')
plt.title('Desconto aplicado por quantidade de vendas', fontsize=14)
plt.xlabel('Quantidade Vendida (codificada)', fontsize=12)
plt.ylabel('Desconto (%)', fontsize=12)
plt.grid(True)
plt.show()

# Mapa de calor
corr = df[['N_Avaliações', 'Nota_MinMax']].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação entre Número de Avaliações e Nota Normalizada')
plt.show()

# grafico de barras

vendas_por_marca = df.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values(ascending=False)
vendas_por_marca = vendas_por_marca.head(10)

plt.figure(figsize=(12, 6))
vendas_por_marca.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Quantidade de Vendas por Marca', fontsize=14)
plt.xlabel('Marca', fontsize=12)
plt.ylabel('Quantidade Vendida (codificada)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# grafico de pizza

vendas_por_marca = df.groupby('Marca')['Qtd_Vendidos_Cod'].sum()

# Selecionar as 10 maiores
top_10 = vendas_por_marca.sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 8))
plt.pie(top_10,
        labels=top_10.index,
        autopct='%1.1f%%',  # mostra % com 1 casa decimal
        startangle=140,
        colors=plt.cm.tab20.colors)  # cores variadas

plt.title('Top 10 Marcas Mais Vendidas (%)', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()

# grafico de densidade
plt.figure(figsize=(12, 6))
sns.kdeplot(df['Qtd_Vendidos_Cod'], fill=True, color='Green')
plt.title('Quantidade de vendas')
plt.xlabel('Vendas')
plt.show()

# grafico de regressao
sns.regplot(x='N_Avaliações', y='Nota', data=df, color='black', scatter_kws={'alpha': 0.5, 'color': 'red'})
plt.title('Nota por numero de avaliaçoes')
plt.xlabel('Numero de avaliaçoes')
plt.ylabel('Nota')
plt.show()
