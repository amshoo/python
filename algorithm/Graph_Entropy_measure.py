
# coding: utf-8
import networkx as nx
import Selection_Algorithm
import math


# In[ ]:
#TR_i = tr-ceyntrality i subgraph
def graph():    
    import graph
    Graph = graph.H
    return Graph
H = graph()
# In[ ]:


#Graph Entropy 
def log1(i):
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    s1 = math.log(sum_sdeg_i, 10)
    return  s1
def prob(i, j): 
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    nodes = Selection_Algorithm.subgraph_of(i).nodes
    degree = Selection_Algorithm.subgraph_of(i).degree[j]
    prob=-(degree/sum_sdeg_i )
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
def PI_of(i):
    sum_sdeg_i = (Selection_Algorithm.subgraph_of(i).number_of_edges()*2)
    NT_i = nx.triangles(H,i)
    sdeg=Selection_Algorithm.subgraph_of(i).degree(i)
    s1 = (math.log(sum_sdeg_i, 10)+NT_i)
    #equetion 4:en value of PI_i
    PI_i =s1-sum(probs(i))
    return PI_i


# In[ ]:
#LOOP PI of the selected Set Of Subgraph
def loop_PI():
    i=0
    PI_list=[]
    
    for i in Selection_Algorithm.sel_subgraphs():
        NT_i = nx.triangles(H,i)
        if NT_i > 1:            
            PI_i = round(PI_of(i), 4)
            PI = i, 1/PI_i
            PI_list.append(PI)  
            
    return  PI_list
# In[ ]:
#ranking PI_list
def PI_Ranking( val ):
      return val [1]

PI_Rank = loop_PI()
PI_Rank.sort(key=lambda elem: elem[1])