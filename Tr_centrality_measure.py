
# coding: utf-8
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import Selection_Algorithm
import math


# In[ ]:
#TR_i = tr-ceyntrality i subgraph
def graph():
    Graph = nx.karate_club_graph()
    return Graph
G = graph()
def graph_h():
    H = nx.convert_node_labels_to_integers(G, first_label=0, ordering="default", label_attribute = None)
    return H
H = graph_h()

# In[ ]:
#equetion 2:TCi_constrain
def TC_constrain_of(i):
        sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_nodes()-1)
        sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
        N_i = Selection_Algorithm.subgraph_of(i).number_of_nodes()
        NT_i = nx.triangles(H,i)
        #equetion 2:TCi_constrain
        TC_i_cons = (sdeg_i/sum_sdeg_i)-((N_i-NT_i)/sum_sdeg_i)
        
        return  TC_i_cons 
#Tr-ceyntrality    
def TC_of(i):
    #degree of node i
    sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_nodes()-1)
    # number of nodes in G_i:
    N_i = Selection_Algorithm.subgraph_of(i).number_of_nodes()
    # number of triangles:
    NT_i = nx.triangles(H,i)
    #sumof_sdeg_i
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    #equetion 3:Tr centrality value of TC_i
    TC_i = (math.pi*(sdeg_i-1)-(2*(N_i)-NT_i))/sum_sdeg_i    
    return  TC_i


# In[ ]:
#LOOP tr-ceyntrality of the selected Set Of Subgraph
def loop_TC():
    # main part of AL loop
    i=0
    TC_list=[]
    for i in H.nodes:        
        # degree of Ni:
        N_i = Selection_Algorithm.subgraph_of(i).number_of_nodes()
        # number of triangles: nodes
        NT_i = nx.triangles(H,i)
        # Extract the nodes of interest: nodes
        nodes = [n for n, d in Selection_Algorithm.subgraph_of(i).nodes(data=True)]
        # Create the set of nodes: nodeset
        nodeset = set(nodes)
        #equetion 1:selection constrain
        if NT_i > 1:
            if TC_constrain_of(i) != 0:
                TR_i = round(TC_of(i), 4)
                i+=1
                TC = (i, TR_i)       
                TC_list.append(TC)            
    return  TC_list

