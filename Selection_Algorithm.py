
# coding: utf-8
import networkx as nx
import math


# In[ ]:
def graph():
    Graph = nx.karate_club_graph()
    return Graph
G = graph()


    
from itertools import combinations
def nodes_in_triangle(G, n):
    """
    Returns the nodes in a graph `G` that are involved in a triangle relationship with the node `n`.
    """
    triangle_nodes = set([n])

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):

        # Check if n1 and n2 have an edge between them
        if G.has_edge(n1, n2):

            # Add n1 to triangle_nodes
            triangle_nodes.add(n1)

            # Add n2 to triangle_nodes
            triangle_nodes.add(n2)

    return triangle_nodes
#equetion 1:selection constrain
def selection_constrain_of(i):
     # degree of N_i:
        N_i = subgraph_of(i).number_of_nodes()
        # sum(sdeg_j):
        sum_sdeg_j = subgraph_of(i).number_of_edges()
        # number of triangles: nodes
        NT_i = nx.triangles(G,i)
        if NT_i > 1:
        #equetion 1:selection constrain        
            TR_i = (N_i-(sum_sdeg_j/2))            
        return  TR_i
    
#Selection Algorithm
def Selection_Algorithm():
    # main part of AL loop
    i=0
    valid_set = []
    for i in G.nodes: 
        subgraph = subgraph_of(i)
        # degree of Ni:
        N_i = subgraph.number_of_nodes()
        # number of triangles: nodes
        NT_i = nx.triangles(G,i)
        # Extract the nodes of interest: nodes
        nodes = [n for n, d in subgraph.nodes(data=True)]
        # Create the set of nodes: nodeset
        nodeset = set(nodes)
        #equetion 1:selection constrain
        if NT_i > 1:
            TR_i = selection_constrain_of(i)
            i+=1        
            list1 = i, NT_i     
            valid_set.append(list1)
                
    return  valid_set


# In[ ]:
def sel_subgraphs():
    sel_subgraphs = []
    for i in G:
        sel_subgraph = G.subgraph(nodes_in_triangle(G, i))
        NT_i = nx.triangles(G,i)
        if NT_i > 1:            
            row = i        
            sel_subgraphs.append(row)
    return  sel_subgraphs

# In[ ]:
#return subgraphs
def subgraph_of(i):
    subgraph = G.subgraph(nodes_in_triangle(G, i))
    return  subgraph  

