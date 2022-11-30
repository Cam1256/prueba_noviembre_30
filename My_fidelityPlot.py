from ctypes import alignment
import pandas as pd
from pyvis.network import Network
import numpy as np
import webbrowser
import csv

path = '/home/cristian/Desktop/Entrega_2/support2.csv'
outpath = '/home/cristian/Desktop/Entrega_2/support_snieves_out.csv'

with open(path) as inf:
    reader = csv.reader(inf.readlines(), delimiter=',')

with open(outpath, 'w') as outf:
    writer = csv.writer(outf, delimiter=',')
    max_col=0
    for line in reader:
        actual_num_col = str(line).count(',')
        if max_col < actual_num_col:
            max_col = actual_num_col
    with open(path) as inf:
        reader = csv.reader(inf.readlines(), delimiter=',')
        for line in reader:
        
            actual_num_col = str(line).count(',')
            fill_col = max_col- actual_num_col
            writer.writerow(line+(['']*fill_col))


       
        outf.columns = outf.columns.str.replace(';','')
        outf['supportitemsets']=outf['supportitemsets'].map(lambda x: x.replace(';',','))
        duty1 = outf['supportitemsets'].str.split(',', expand=True)

        data_total = pd.concat([duty1, inf], axis = 1).drop('supportitemsets', 1)
        data_total[1] = data_total[1].astype(float)
        data_total[1] = data_total[1] * 100
        df1=pd.DataFrame.from_records(data_total.values)

        nodes = df1[2].to_list()
        nodes = [node.strip() for node in nodes]

        def draw_network(
            nodes: list,
            data_total: pd.DataFrame,
            minium_weight: int = 0,
            repulsion: int = 100,
            spring_length=200,
            buttons=None,
            
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
                #print(nodes_row)
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
            nodes = all_nodes.copy()
                #edges = [(node[0], node[0], weights)]
                #if str(node[1])!=("nan")or(None):
                #    edges.append((node[0], node[1], weights))
                #if str(node[2])!=("nan")or(None):
                #    edges.append((node[0], node[1], weights))
                #    edges.append((node[2], node[0], weights))
                #    edges.append((node[2], node[1], weights))
                
            edges = [(node[0].strip(), node[0].strip(), weights)]
            
            if str(node[1])!=("nan"):
                edges.append((node[0].strip(), node[1].strip(), weights))
            
            for i in lista:
                if i > 1:
            
                    if str(node[i]) !=("nan"):
                        edges.append((node[i].strip(), node[i].strip(), weights))
                    
            edges = [edge for edge in edges if edge[2] >= minium_weight]

            return edges

        net = draw_network(nodes, data_total, minium_weight=0.05, repulsion=100, spring_length=600)
        #net.toggle_physics(True)
        net.show("/home/cristian/Desktop/Entrega_2/data/grafo.html")

        # url = 'file:///home/cristian/Desktop/Entrega_2/grafo.html'
        # webbrowser.open(url, new=2)



    


