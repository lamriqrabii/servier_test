

import json


class UtilsGraph():

    def __init__(self, json_file:json) -> None:
        self.json_file = json_file

    def get_node_with_edges(self, node_name:str):
        
        edges = self.json_file['edges']
        edges = [item['target'] for item in edges if item['metadata']['label']==f'referenced in {node_name}']
        
        max_edge = max(set(edges), key = edges.count)

        return max_edge
        
        


if __name__ == "__main__":

    with open('graph_output/data.json', 'rb') as f:
        doc_json = json.load(f)
    
    ug = UtilsGraph(doc_json)
    max_journal = ug.get_node_with_edges(node_name='journal')
    max_clinical = ug.get_node_with_edges(node_name='clinical_trials')
    max_pubmed = ug.get_node_with_edges(node_name='pubmed')

    print(f"le journal qui mentionne plus de drug est: {max_journal}")
    print(f"le clinical trials qui mentionne plus de drug est: {max_clinical}")
    print(f"le pubmed qui mentionne plus de drug est: {max_pubmed}")