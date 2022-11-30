import pandas as pd
from pyvis.network import Network
import csv

filepath = '/home/cristian/Desktop/Entrega_2/support.csv'

with open(filepath) as inf:
    reader = csv.reader(inf.readlines(), delimiter=',')
    max_col=0
    for line in reader:
        
        actual_num_col = str(line).count(',')
        if max_col < actual_num_col:
            max_col = actual_num_col
    with open(filepath) as inf:
        reader = csv.reader(inf.readlines(), delimiter=',')
    dframe1 = []
    for line in reader:
       
        actual_num_col = str(line).count(',')
        fill_col = max_col- actual_num_col
        dframe1.append(line)
        
        inf.close()

dframe1=pd.DataFrame(dframe1)
dframe1 = dframe1.iloc[1: , :]
dframe1[0] = dframe1[0].str.replace(';',',')

duty1 = dframe1[0].str.split(',', expand=True)
duty1[1] = duty1[1].astype(float)
duty1[1] = duty1[1] * 100
data_total = pd.concat([duty1, dframe1[1]], axis = 1)
df1=pd.DataFrame.from_records(data_total.values)

nodes = df1[2].to_list()

nodes = [node.strip() for node in nodes]

def draw_network(
    nodes: list,
    df1: pd.DataFrame,
    minium_weight: int = 0,
    repulsion: int = 100,
    spring_length=200, 
):
    net = Network("1000px", "1000px", notebook=False)
    net.add_nodes(nodes)
       
    itemcol = []
    for column in df1:
        cur = df1.columns.get_loc(column)
        if cur > 1:
            itemcol.append(cur)
    
    for index, row in df1.iterrows():
        nodes_row = []
        for i in itemcol:
            nodes_row.append(row[i])
        
        edges = get_edges(nodes_row, row[1], nodes, minium_weight)
        net.add_edges(edges)

    net.repulsion(repulsion, spring_length=spring_length)    
    return net

lista = []
for i in df1:
    cur = df1.columns.get_loc(i)
    if cur > 1:
        lista.append(cur-2)


def get_edges(node: list, weights: float, all_nodes: list, minium_weight: int):
    edges = [(node[0].strip(), node[0].strip(), weights)]
    
    if str(node[1])!=('None'):
        edges.append((node[0].strip(), node[1].strip(), weights))
    
    for i in lista:
        if i > 1:
    
            if str(node[i]) !=('None'):
                edges.append((node[i].strip(), node[i].strip(), weights))
             
    edges = [edge for edge in edges if edge[2] >= minium_weight]
    
    return edges

net = draw_network(nodes, df1, minium_weight=0.05, repulsion=100, spring_length=600)

net.show("/home/cristian/Desktop/Entrega_2/data/grafo.html")
