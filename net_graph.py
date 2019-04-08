
# coding: utf-8

# In[1]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[21]:


def net_graph():

    all_members = set(range(11))
    G = nx.Graph()
    G.add_nodes_from(all_members)
    G.name = "asking for an opinion"

    netdat = """ 0 1 1 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 1 0 0 0
 1 1 0 1 0 1 1 1 0 0 0
 0 0 0 0 0 0 1 1 0 0 0
 0 1 0 1 0 1 1 1 0 0 0
 0 1 0 1 1 0 1 1 0 0 0
 0 0 0 1 0 0 0 1 1 0 1
 0 1 0 1 0 0 1 0 0 0 1
 0 0 0 1 0 0 1 1 0 0 1
 1 0 1 1 1 0 0 0 0 0 0
 0 0 0 0 0 1 0 1 1 0 0"""

    for row, line in enumerate(netdat.split('\n')):
        thisrow = [int(b) for b in line.split()]
        for col, entry in enumerate(thisrow):
            if entry == 1:
                G.add_edge(row, col)
    return G
G = net_graph()


# In[29]:


#net_graph().nodes

