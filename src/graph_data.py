
import json

class GraphJson():

    data_json = json.loads('''{
            "graph":{},
            "nodes":[],
            "edges":[]
        }'''
    )

    nodes = []

    def __init__(self, name:str) -> None:
        self.data_json['graph'] = {'name': name} 

    def _has_node(self, node:str):
        if node in self.nodes:
            return True
        else:
            return False

    def add_node(self, id:str, label:str):
        if self._has_node(id) == False:
            self.data_json['nodes'].append({'id':id, 'label':label})
            self.nodes.append(id)

    def add_edge(self, source:str, target:str, metadata):
        self.data_json['edges'].append({'source':source, 'target':target, 'metadata':metadata})

    def graph_to_json(self):
        return self.data_json

# if __name__ == "__main__":
#     G = GraphJsn(name = "drug relation")
#     G.add_node(id="A", label="drug")
#     G.add_node(id="A", label="xxx")
#     G.add_node(id="A", label="DCLG")
#     G.add_node(id="B", label="jurnal")
#     G.add_node(id="C", label="pubmed")
#     G.add_edge('A', 'B', label = '2020-01-01')
#     G.add_edge('A', 'C', label = '2019-01-11')

#     print(G.graph_to_json())
