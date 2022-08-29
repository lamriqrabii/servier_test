
from load_data import LoadData
import pandas as pd 
import json

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
df_drug_clinic['reference'] = "clinic_trials"


df_drug_pubmed = ld.search_data(df_drugs, 'drug', df_pubmed, 'title')
df_drug_pubmed = df_drug_pubmed[columns]
df_drug_pubmed['reference'] = "pubmed"


df_drug_graph = pd.DataFrame()
df_drug_graph = pd.concat([df_drug_graph, df_drug_pubmed, df_drug_clinic])

df_drug_graph.index = range(len(df_drug_graph))    
#print(df_drug_graph)

## json output
json_graph = {
    "graphs": []
}

for i in range(len(df_drug_graph)):
    drug_name = df_drug_graph.loc[i,'drug']
    journal_name = df_drug_graph.loc[i,'journal']
    reference = df_drug_graph.loc[i,'reference']
    date = str(df_drug_graph.loc[i,'date'])
    title = df_drug_graph.loc[i,'title']

    node = {}
    node['0'] = {
        'label':'drug',
        'metadata':{
            'type':'drug',
            'name': drug_name
        }
    }
    node['1'] = {
        'label':reference,
        'metadata':{
            'type':reference,
            'name': title
        }
    }
    node['2'] = {
        'label':'journal',
        'metadata':{
            'type':'journal',
            'name': journal_name
        }
    }

    edge = [
        {
          "source": "0",
          "relation": "referenced in",
          "target": "1",
          "directed": 'true',
          "label": "referenced in",
          "metadata": {
            "date": date
          }
        },
        {
          "source": "0",
          "relation": "referenced in",
          "target": "2",
          "directed": 'true',
          "label": "referenced in",
          "metadata": {
            "date": date
          }
        }
      ]
    
    graph = {}
    graph['nodes'] = node
    graph['edges'] = edge
    json_graph['graphs'].append(graph)

with open('graph_output/data.json', 'w') as f:
    json.dump(json_graph, f, indent=4)
