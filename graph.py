
# coding: utf-8

# In[3]:


import networkx as nx

#G = nx.karate_club_graph()
filepath = ('PB.txt')
fh=open("PB.txt", 'rb')
G = nx.read_weighted_edgelist(fh,nodetype=None, encoding='utf-8')
fh.close()

H = nx.convert_node_labels_to_integers(G, first_label=0, ordering="default", label_attribute = None)