
# coding: utf-8
import networkx as nx
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


#Graph Entropy 
def prob(i, j): 
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    nodes = Selection_Algorithm.subgraph_of(i).nodes
    degree = Selection_Algorithm.subgraph_of(i).degree[j]
    prob=degree/sum_sdeg_i 
    return prob  

def log2(i,j):
    degree = Selection_Algorithm.subgraph_of(i).degree[j]
    log_j = math.log(degree, 10)
    return log_j

def probs(i):
    probs=[]
    for i in Selection_Algorithm.subgraph_of(i).nodes:
        for j in Selection_Algorithm.subgraph_of(i).nodes:
            enr = (prob(i, j)*log2(i,j)) 
            #enr=(i, en)
        probs.append(enr)  
    return probs 
#Return PI of i
def PI_of(i):
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    #k = Selection_Algorithm.subgraph_of(i).degree(i)
    nt = NT_i = nx.triangles(G,i)
    s1 = math.log(sum_sdeg_i-nt, 10)
     #equetion 4:en value of PI_i
    PI_i = s1 - sum(probs(i))
    return PI_i


# In[ ]:
#LOOP PI of the selected Set Of Subgraph
def loop_PI():
    i=0
    PI_list=[]
    
    for i in Selection_Algorithm.sel_subgraphs():
        NT_i = nx.triangles(G,i)
        if NT_i > 1:            
            PI_i = round( PI_of(i), 4)
            i+=1
            PI = [i, PI_i]
            PI_list.append(PI)  
            
    return  PI_list

