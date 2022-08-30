
from load_data import LoadData
import pandas as pd 
import json
from graph_data import GraphJson

ld = LoadData()
df_drugs = ld.load_data("drugs")
df_pubmed = ld.load_data("pubmed")
df_clinical = ld.load_data("clinical_trials")

# cnvert clumn t lwercase
df_drugs['drug'] = df_drugs['drug'].str.lower()
df_pubmed['title'] = df_pubmed['title'].str.lower()
df_clinical['title'] = df_clinical['title'].str.lower()

columns = ['drug', 'title', 'journal', 'date']
df_drug_clinic = ld.search_data(df_drugs, 'drug', df_clinical, 'title')
df_drug_clinic = df_drug_clinic[columns]
df_drug_clinic['reference'] = "clinical_trials"


df_drug_pubmed = ld.search_data(df_drugs, 'drug', df_pubmed, 'title')
df_drug_pubmed = df_drug_pubmed[columns]
df_drug_pubmed['reference'] = "pubmed"


df_drug_graph = pd.DataFrame()
df_drug_graph = pd.concat([df_drug_graph, df_drug_pubmed, df_drug_clinic])

df_drug_graph.index = range(len(df_drug_graph))    


graph = GraphJson(name= "drug relation")

for i in range(len(df_drug_graph)):
    drug_name = df_drug_graph.loc[i,'drug']
    journal_name = df_drug_graph.loc[i,'journal']
    reference = df_drug_graph.loc[i,'reference']
    date = str(df_drug_graph.loc[i,'date'].date())
    title = df_drug_graph.loc[i,'title']

    # add nodes
    graph.add_node(id = drug_name, label = 'drug')
    graph.add_node(id = journal_name, label = 'journal')
    graph.add_node(id = title, label = reference)

    # add edges (relations)
    graph.add_edge(source=drug_name, target=journal_name, metadata={'date':date, 'label':'referenced in journal'})
    graph.add_edge(source=drug_name, target=title, metadata={'date':date, 'label':f'referenced in {reference}'})

    

with open('graph_output/data.json', 'w') as f:
    json.dump(graph.graph_to_json(), f, indent=4)
