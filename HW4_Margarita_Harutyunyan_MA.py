# -*- coding: utf-8 -*-
"""HW4_Margarita_Harutyunyan_MA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o6cJjOonaJBgX-_7G9zpvGrhXmNuzF7n
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.colors as colors
from heapq import nlargest, nsmallest
from copy import deepcopy
from infomap import Infomap
from operator import itemgetter

edges = pd.read_csv('connections.txt', delimiter=' ', names=['from', 'to'])
edges.head(10)

"""# Homework


"""

#1
graph = nx.DiGraph()

graph.add_edges_from(np.array(edges))

#2
edges.shape

#Calculating the betweenness centrality and finding the top 10 bridge nodes based on that
betweenness = nx.betweenness_centrality(graph)
top_bridges = nlargest(10, betweenness, key=betweenness.get)
#Printing the top 10 bridge nodes and their betweenness centrality values
for node in top_bridges:
    print(f"Node {node}: Betweenness {betweenness[node]}")

#3
(graph.number_of_nodes(), graph.number_of_edges())
nx.density(graph)

#A density of 0 indicates no connections, while a density of 1 represents a fully connected
#graph. The graph's density i got indicates that the level of edge connectivity in the graph 
#is relatively low.

#4
# Calculate the degrees for each node and find the top 10 mith highest degree
degrees = dict(graph.degree())
highest_degrees = nlargest(10, degrees, key=degrees.get)
# Print 10 nodes with their degrees
for node in highest_degrees:
    print(f"Node {node}: Degree {degrees[node]}")

#Find the nodes with the lowest number of connections (degrees less than or equal to 3)
lowest_degrees = [node for node, degree in degrees.items() if degree <= 3]
for node in lowest_degrees:
    print(f"Node {node}: Degree {degrees[node]}")

#5
#Calculating the in-degrees and out-degrees for each node
in_degrees = dict(graph.in_degree)
out_degrees = dict(graph.out_degree)
# Find the 10 nodes with the highest in-degrees and 10 with highest out-degrees
highest_IN_degrees = nlargest(10, in_degrees, key = in_degrees.get)
highest_OUT_degrees = nlargest(10, out_degrees, key = out_degrees.get)

print("=======IN DEGREES=======")
for i in highest_IN_degrees:
    print(f'Node {i}: Degree {in_degrees[i]}')
    

print("======OUT DEGREES=======")
for i in highest_OUT_degrees:
    print(f'Node {i}: Degree {out_degrees[i]}')

#6
#Calculating the closeness centrality for each node and finding top 10 with highest closeness centrality
closeness = nx.closeness_centrality(graph)
top_closeness = nlargest(10, closeness, key=closeness.get)

for node in top_closeness:
    print(f"Node {node}: Closeness {closeness[node]}")

#Calculating eigenvector centralities for in and out edges
eigenvector_in = nx.eigenvector_centrality(graph, max_iter=300)
eigenvector_out = nx.eigenvector_centrality(graph.reverse(), max_iter=300)

#Calculating eigenvector centralities for every node and finding top 10 highest
eigenvector = {}
for node in graph.nodes():
    eigenvector[node] = (eigenvector_in[node] + eigenvector_out[node]) / 2
    
top_eigenvector = nlargest(10, eigenvector, key=eigenvector.get)

for node in top_eigenvector:
    print(f"Node {node}: Eigenvector {eigenvector[node]}")

#The node with the highest betweenness centrality measure is node 1684 . 
#This indicates that it lies on the most shortest paths between pairs of nodes in the 
#network. As a result, it acts as a bridge, controlling the flow of information between 
#different parts of the network.
#The node with the highest closeness centrality is 2642. It is the most central in the
#network, as it has the shortest average distance to all other nodes. This means that it is
#closely connected to other nodes and can quickly transmit information and exert influence 
#over them.
#Node 0 has the highest eigenvector centrality measure. It is highly connected to other
#important nodes in the network, making it influential in terms of its ability to spread 
#information and exert influence.

#7
def findCommunities(graph):
    im = Infomap("--two-level --directed")
    print("Building Infomap network from a NetworkX graph...")
    
    for e in graph.edges():
        im.addLink(*e)
        
    print("Find communities with Infomap...")
    im.run();
    print("Found {0} communities with codelength: {1}".format(im.num_top_modules,
    im.codelength))
    communities = {}
    
    for node in im.tree:
        communities[node.node_id] = node.module_id
        
    nx.set_node_attributes(graph, communities,'community')
    return im.num_top_modules

findCommunities(graph)

"""93 communities found"""

#8
#Dict of nodes and their corresponding communities
nodes_comm = {n: d["community"] for n, d in graph.nodes(data=True)}
#List of all communities
comms = list(nodes_comm.values())
#Taking unique ones
distinct_comms = np.unique(comms)
#Dictionary for each community and the node count
community_count = {}

#Filling above dictionary
for com in distinct_comms:
    count = comms.count(com)
    community_count[com] = count

max_ = max(community_count, key=community_count.get)
min_ = min(community_count, key=community_count.get)

print(f"Largest community: {max_}, with {community_count[max_]} nodes")
print(f"Smallest community: {min_}, with {community_count[min_]} nodes")

#9
#Communities based on their sizes in descending order
communities_sort = sorted(community_count.items(), key=lambda x: x[1], reverse=True)
#Top 3 largest communities
largest_communities = communities_sort[:3]
for i in range(len(largest_communities)):
    print(f'Community {largest_communities[i][0]}: Nodes {largest_communities[i][1]}')

"""So our top 3 largest communities are comunnity 4, 2 and 8"""

selected_data4 = dict((n,d['community']) for n,d in graph.nodes().items() if d['community'] == 4)
sg4 = graph.subgraph(list(selected_data4.keys()))
pos4 = nx.spring_layout(sg4, seed=5656)
nx.draw(sg4, pos=pos4, node_size = 80)
plt.title("Community 4")
plt.show()

selected_data2 = dict((n,d['community']) for n,d in graph.nodes().items() if d['community'] == 2)
sg2=graph.subgraph(list(selected_data2.keys()))
pos2 = nx.spring_layout(sg2, seed=5656)
nx.draw(sg2, pos=pos2, node_size = 100)
plt.title("Community 2")
plt.show()

selected_data8 = dict((n,d['community']) for n,d in graph.nodes().items() if d['community'] == 8)
sg8=graph.subgraph(list(selected_data8.keys()))
pos8 = nx.spring_layout(sg8, seed=5656)
nx.draw(sg8, pos=pos8, node_size = 80)
plt.title("Community 8")
plt.show()

# A function that removes the top 3 nodes based on closeness, betweenness, and eigenvector
def top3_removing(sg):
    sg_copy = sg.copy()  # Create a copy of the graph

    dict_betweenness = nx.betweenness_centrality(sg_copy)
    nx.set_node_attributes(sg_copy, dict_betweenness, 'betweenness')
    betweenness_sort = sorted(dict_betweenness.items(), key=itemgetter(1), reverse=True)
    top3bet = [tup[0] for tup in betweenness_sort][:3]

    dict_closeness = nx.closeness_centrality(sg_copy)
    nx.set_node_attributes(sg_copy, dict_closeness, 'closeness')
    closeness_sort = sorted(dict_closeness.items(), key=itemgetter(1), reverse=True)
    top3clo = [tup[0] for tup in closeness_sort][:3]

    dict_eigenvector = nx.eigenvector_centrality(sg_copy, max_iter = 10000)
    nx.set_node_attributes(sg_copy, dict_eigenvector, 'eigenvector')
    eigenvector_sort = sorted(dict_eigenvector.items(), key=itemgetter(1), reverse=True)
    top3eig = [tup[0] for tup in eigenvector_sort][:3]
    top3 = list(set(top3clo + top3bet + top3eig))

    sg_copy.remove_nodes_from(top3)

    return sg_copy

# getting the commmunities without the "influencers"
sg4_removed = top3_removing(sg4)
sg2_removed = top3_removing(sg2)
sg8_removed = top3_removing(sg8)

pos4_removed = nx.spring_layout(sg4_removed, seed=5656)
nx.draw(sg4_removed, pos=pos4_removed, node_size = 80)
plt.title("Community 4 with no influencers")
plt.show()

pos2_removed = nx.spring_layout(sg2_removed, seed=5656)
nx.draw(sg2_removed, pos=pos2_removed, node_size = 80)
plt.title("Community 2 with no influencers")
plt.show()

pos8_removed = nx.spring_layout(sg8_removed, seed=5656)
nx.draw(sg8_removed, pos=pos8_removed, node_size = 80)
plt.title("Community 8 with no influencers")
plt.show()

#10 
def top_3(sg):
    sg_copy = sg.copy()  # Create a copy of the graph

    dict_betweenness = nx.betweenness_centrality(sg_copy)
    nx.set_node_attributes(sg_copy, dict_betweenness, 'betweenness')
    betweenness_sort = sorted(dict_betweenness.items(), key=itemgetter(1), reverse=True)
    top3bet = [tup[0] for tup in betweenness_sort][:3]

    dict_closeness = nx.closeness_centrality(sg_copy)
    nx.set_node_attributes(sg_copy, dict_closeness, 'closeness')
    closeness_sort = sorted(dict_closeness.items(), key=itemgetter(1), reverse=True)
    top3clo = [tup[0] for tup in closeness_sort][:3]

    dict_eigenvector = nx.eigenvector_centrality(sg_copy, max_iter = 10000)
    nx.set_node_attributes(sg_copy, dict_eigenvector, 'eigenvector')
    eigenvector_sort = sorted(dict_eigenvector.items(), key=itemgetter(1), reverse=True)
    top3eig = [tup[0] for tup in eigenvector_sort][:3]
    top3 = list(set(top3clo + top3bet + top3eig))

    return top3

#Influencers of Community 4
top3_in4 = top_3(sg4)
#Color map where influencers are yellow ones and the others are green
color_map= ['yellow' if node in top3_in4 else 'green' for node in sg4]
pos4 = nx.spring_layout(sg4, seed=5656)
nx.draw(sg4,node_color=color_map, with_labels=False, pos=pos4)
plt.title("Community 4 influencers")
plt.show()

#Influencers of Community 2
top3_in2 = top_3(sg2)
#Color map where influencers are yellow ones and the others are green
color_map= ['yellow' if node in top3_in2 else 'green' for node in sg2]
pos2 = nx.spring_layout(sg2, seed=5656)
nx.draw(sg2,node_color=color_map, with_labels=False, pos=pos2)
plt.title("Community 2 influencers")
plt.show()

#Influencers of Community 8
top3_in8 = top_3(sg8)
#Color map where influencers are yellow ones and the others are green
color_map= ['yellow' if node in top3_in8 else 'green' for node in sg8]
pos8 = nx.spring_layout(sg8, seed=5656)
nx.draw(sg8,node_color=color_map, with_labels=False, pos=pos8)
plt.title("Community 8 influencers")
plt.show()

"""For my action plan I will consider the *hypothetical business* is a digital marketing agency specializing in providing a range of digital marketing services to clients. 
Services: search engine optimization, paid advertising (PPC), content marketing, email marketing, and so on. The agency helps businesses increase their online visibility, attract customers, and achieve their marketing goals.


The hypothetical business has a *budget* of 100,000 USD, for example, for the realisation within a specific period. 

*Cost per action (CPA)* represents the average expenditure for each desired customer action resulting from marketing activities. For example, if agency invests 1,000 USD in advertising and achieves 100 customer conversions, the CPA would amount to 10 USD, calculated by dividing the total expenditure (1,000 USD) by the number of conversions (100). We will take our cost per action 10 USD.

To understand who is the *target*, the agency needs to conduct a research and analyse the results to identify the most valuable audience segments. First thing is to conduct a market research. This will include gathering information about the industry, trends in market, customer preferances and of course competitors. Understand the pain points of the potential customers. Second step is analyzing competitors. See who are the target audience of competitors and identify gaps or untapped segments, so the agency will target them too. The next step will be developing buyer personas. These personas are representation of ideal customer and include many characteristics like demographics, interests , pain points, and media consumption habits. The agency creates several personas to have different segments to target. Then the agency evaluates and prioritizes the personas (different segments) based on size, potential value and alignment with the business's expertise. This is done because some segments may offer higher revenue potential or be more receptive to the agency's services. To narrow down the target audience agency uses digital marketing tools. The narrowing (նեղացումը) is done based on specific parameters like location, gender, age, online behaviors, interests ans so on. After all these the final step will be implementing targeted advertising campaigns to somehow tests and measure response rates, conversations. Optimize the parameters for targetting to ensure effective audience targeting. I think done!
"""