
import pandas as pd
import numpy as np

df = pd.read_csv("dogs-ranking-dataset.csv")
display(df.head())

## Select the specfic traits we want to compare and making list of breed names for row/column labels
traits = df[['popularity ranking', 'size', 'intelligence', 'score for kids', 'NUMBER OF GENETIC AILMENTS']]
costs = df[['$LIFETIME COST', 'PURCHASE PRICE', 'FOOD COSTS PER YEAR']]

breeds = df['Breed'].tolist()



#1. making jaccard function

def jaccard(a, b):
    union = np.sum(a.values == b.values) #match or not, then the sum of matches
    total = len(a) ## 5 traits total
    return union / total

# 2. Create empty similarity matrix (breed x breed)


similarity = np.zeros((len(df), len(df)))

## filling in the matrix with loop, calulating similairy score then storing in matrix position

for i in range(len(df)):
    for j in range(len(df)):
        similarity[i,j] = jaccard(traits.iloc[i], traits.iloc[j])
#3.


##labeled table

similarity_df = pd.DataFrame(similarity, index=breeds, columns=breeds)

#print(similarity_df)

similarityC = np.zeros((len(df), len(df)))

## filling in the matrix with loop, calulating similairy score then storing in matrix position

for i in range(len(df)):
    for j in range(len(df)):
        similarityC[i,j] = jaccard(costs.iloc[i], costs.iloc[j])
#3.


##labeled table

similarityC_df = pd.DataFrame(similarityC, index=breeds, columns=breeds)

#print(similarityC_df)

#4. function

def get_similar(breed, trait, top=5):
    idx = breeds.index(breed)
    sims = similarity[idx]
    pairs = list(zip(breeds, sims))
    pairs_sorted = sorted(pairs, key=lambda x: x[1], reverse=True)
    filtered = [(p[0], float(p[1])) for p in pairs_sorted if p[0] != breed]
    return filtered[:top]


# get_similar('German Shepherd', 'all traits')

def get_similarcost(breed, cost, top=5):
    idx = breeds.index(breed)
    sims = similarityC[idx]
    pairs = list(zip(breeds, sims))
    pairs_sorted = sorted(pairs, key=lambda x: x[1], reverse=True)
    filtered = [(p[0], float(p[1])) for p in pairs_sorted if p[0] != breed]
    return filtered[:top]


#get_similarcost('German Shepherd', 'cost')

from dash import Dash, html, dcc, Input, Output
import plotly.express as px

appp = Dash(__name__)

appp.layout = html.Div([
    html.H1("Dog Breed Similarity"),
    dcc.Dropdown(
        id='breed-dropdown',
        options=[{'label': b, 'value': b} for b in breeds],
        value='Rottweiler'
    ),
    dcc.Graph(id='traits-bargraph'),
    dcc.Graph(id='cost-bargraph')

])

@appp.callback(
    Output('traits-bargraph', 'figure'),
    Input('breed-dropdown', 'value')
)
def update_traits_graph(selected_breed):
    similar_breeds_data = get_similar(selected_breed, 'all_traits')

    df_plot = pd.DataFrame(
        similar_breeds_data,
        columns=['Breed', 'Similarity Score']
    )

    fig = px.bar(
        df_plot,
        x='Breed',
        y='Similarity Score',
        range_y=[0, 1],  # since similarity max = 1
        title=f"Top Similar Breeds to {selected_breed} (Popularity, Size, Intelligence, Kid Score, Genetic Ailments)"
    )
    return fig
@appp.callback(
    Output('cost-bargraph', 'figure'),
    Input('breed-dropdown', 'value')
)
def update_traits_graph(selected_breed):
    similar_breeds_data = get_similarcost(selected_breed, 'cost')

    df_plot = pd.DataFrame(
        similar_breeds_data,
        columns=['Breed', 'Similarity Score']
    )

    fig = px.bar(
        df_plot,
        x='Breed',
        y='Similarity Score',
        range_y=[0, 1],  # since similarity max = 1
        title=f"Top Similar Breed Costs to {selected_breed} (Lifetime Cost, Purchase Price, Food Costs Per Year)"
    )
    return fig

appp.run()

