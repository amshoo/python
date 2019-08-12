#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Import pyplot and nx
import matplotlib.pyplot as plt
import networkx as nx
import operator


# In[2]:


def graph():    
    import graph
    Graph = graph.H
    return Graph
H = graph()


# In[3]:


import Selection_Algorithm

# In[5]:

#CC = Constraint Coefficient of selected set of node
__all__ = ['constraint', 'local_constraint', 'effective_size']

def mutual_weight(H, u, v, weight=None):
    try:
        a_uv = H[u][v].get(weight, 1)
    except KeyError:
        a_uv = 0
    try:
        a_vu = H[v][u].get(weight, 1)
    except KeyError:
        a_vu = 0
    return a_uv + a_vu


# In[11]:


def normalized_mutual_weight(H, u, v, norm=sum, weight=None):
    scale = norm(mutual_weight(H, u, w, weight)
                 for w in set(nx.all_neighbors(H, u)))
    return 0 if scale == 0 else mutual_weight(H, u, v, weight) / scale
#Returns the constraint on all nodes in the graph H
def constraint(H, nodes=None, weight=None):   
    if nodes is None:
        nodes = H
    constraint = {}
    for v in Selection_Algorithm.sel_subgraphs():
        # Constraint is not defined for isolated nodes
        if len(H[v]) == 0:
            constraint[v] = float('nan')
            continue
        constraint[v] = sum(local_constraint(H, v, n, weight)
        for n in set(nx.all_neighbors(H, v)))               
    return constraint
#Returns the local constraint on the node `u` with respect to the node `v` in the graph H
def local_constraint(H, u, v, weight=None):
    nmw = normalized_mutual_weight
    direct = nmw(H, u, v, weight=weight)
    indirect = sum(nmw(H, u, w, weight=weight) * nmw(H, w, v, weight=weight)
                   for w in set(nx.all_neighbors(H, u)))
    return (direct + indirect) ** 2

#Ranking
#return sorted list of node and it Constraint_Coefficient
sorted_x = sorted(constraint(H, nodes=None, weight=None).items(), 
                  key=operator.itemgetter(1))

# In[13]:
#return the CC of node i
def CC_of(i):
    CC_of_i = constraint(H, nodes=None, weight=None).get(i)
    return CC_of_i

#constraint(H, nodes=None, weight=None)

