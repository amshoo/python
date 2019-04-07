#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# In[2]:


import Selection_Algorithm
#print('List of Valid Selected Set nodes', Selection_Algorithm.sel_subgraphs())
#return subgraphs of Node i = k
#i=0
#print('nodes in subgraphs of Node i', Selection_Algorithm.subgraph_of(i).nodes)
#return nodes and number of triangle 
#print('nodes with number of triangle in subgraphs of Node i', Selection_Algorithm.Selection_Algorithm())


# In[3]:


#Calcullating the TC_of node i
import Tr_centrality_measure
#return TC_of node i
#i=0
#print('TC_list', Tr_centrality_measure.TC_of(i))
#Tr_centrality_measure.TC_of(i)
#print('TC_list', Tr_centrality_measure.loop_TC())


# In[4]:


#Ranking
def TC_Ranking( val ):
      return val [1]

TC_Rank = Tr_centrality_measure.loop_TC()
TC_Rank.sort(key=lambda elem: elem[1])

#print('TC_Ranking', TC_Rank)


# In[ ]:


#Calcullating the PI_of node i
import Graph_Entropy_measure
#Tr_centrality_measure.TC_of(i)
#return PI_of node i
#i=0
#print('TC_list', Graph_Entropy_measure.PI_of(i))

#print('TC_list', Graph_Entropy_measure.loop_PI())


# In[ ]:


#Ranking
def PI_Ranking( val ):
      return val [1]

PI_Rank = Graph_Entropy_measure.loop_PI()
PI_Rank.sort(key=lambda elem: elem[1])

#print('PI_Ranking', PI_Rank)


# In[ ]:


#Calcullating the CC_of node i
import Constraint_Coefficient
#Constraint_Coefficient.constraint(Constraint_Coefficient.H, nodes=None, weight=None)
#print('CC_list', Constraint_Coefficient.CC_of(i))


# In[ ]:


#Ranking
#return sorted list of node and it Constraint_Coefficient
sorted_x = sorted(Constraint_Coefficient.constraint(Constraint_Coefficient.H, nodes=None, weight=None).items(), 
                  key=Constraint_Coefficient.operator.itemgetter(1))
#print('CC_Ranking', sorted_x)
from operator import itemgetter
# using map() + itergetter() to get names 
CC_list = list(map(itemgetter(0), sorted_x))   
CC_Rank_list = [x+1 for x in CC_list]
#return the ranking of CC in all selected node form Graph G.
#CC_Rank_list


# In[ ]:


#Calcullating the TPN_of node i
#import Total_Power_of_Node


# In[ ]:


#Ranking Result For all the Measures 
#[PI_Rank, sorted_x, TC_Rank]
#for value in TC_Rank:
   # print(value[0], value[1])
    #print(*value,sep='|')


# In[ ]:


TC_table = pd.DataFrame(TC_Rank, columns = ('nodes','TC_i'))
PI_table = pd.DataFrame(PI_Rank, columns = ('nodes','PI_i'))
CC_table = pd.DataFrame(sorted_x, columns = ('nodes','CC_i'))
CC_table.nodes = CC_table.nodes + 1
Result_table = pd.concat([TC_table, PI_table, CC_table], axis=1, sort=False)

First_Five = pd.DataFrame(Result_table.loc[0:4])
First_Five.index = First_Five.index + 1


print(First_Five)


# In[ ]:


#PI_table.plot.scatter(x='nodes', y = 'PI_i');
#ax = PI_table.plot.scatter(x='nodes', y='PI_i', color='DarkBlue', label='Group 1', s= PI_table['PI_i'] * 200);
#TC_table.plot.scatter(x='nodes', y='TC_i', color='DarkGreen', label='Group 2', s= TC_table['TC_i'] * 200, ax=ax);


# In[ ]:


#First_TC_table = pd.DataFrame(TC_table.loc[0:4])
#First_PI_table = pd.DataFrame(PI_table.loc[0:4])
#First_CC_table = pd.DataFrame(CC_table.loc[0:4])
#result = pd.merge(First_PI_table, First_TC_table,  how ='inner', on ='nodes')
#result1 = pd.merge(result, First_CC_table ,how ='inner', on ='nodes')
#result1


# In[ ]:




