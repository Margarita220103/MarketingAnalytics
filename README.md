# Homework 4 Marketing Analytics Margarita Harutyunyan
## Social Network Analysis for Target Market

This repository demonstrates the use of social network analysis methods to identify influential individuals and communities in a network. To do this the repository uses measures like edge betweenness, density, community structure. The overall analysis gives insights to do the segmentation properly and to target right individuals.

## Importing required libraries
pandas (as pd)   
numpy (as np)    
matplotlib.pyplot (as plt)   
networkx (as nx)   
matplotlib.colors   
heapq (nlargest, nsmallest)   
copy (deepcopy)   
infomap (Infomap)   
operator (itemgetter)
You can install these dependencies using the pip package manager.

```bash
pip install package_name
```

## Loading the data

The script reads an input file ('connections.txt') containing edge connections and creates a pandas DataFrame. The file is attached to repository

## Tasks achived in the repository

1. Creating a directed graph and adding edges:
   - A directed graph object is created using NetworkX (nx.DiGraph()).
   - Edges from the DataFrame are added to the graph.
2. Calculating betweenness centrality and finding top 10 bridge nodes:
   - The script calculates the betweenness centrality for each node using NetworkX.
   - The top 10 bridge nodes with the highest betweenness centrality are identified and printed.
3. Analyzing graph density, number of nodes, and number of edges:
   - The script calculates the graph's density, number of nodes, and number of edges using NetworkX.
   - The results are printed.
4. Calculating node degrees and finding top 10 nodes with highest degrees:
   - The script calculates the degree for each node using NetworkX.
   - The top 10 nodes with the highest degrees are identified and printed.
   - The nodes with the lowest number of connections (degrees less than or equal to 3) are also printed.
5. Calculating in-degrees and out-degrees for each node:
   - The script calculates the in-degree and out-degree for each node using NetworkX.
   - The top 10 nodes with the highest in-degrees and out-degrees are identified and printed.
6. Finding communities using Infomap:
   - The script defines a function, findCommunities, which uses the Infomap library to detect communities in the graph.
   - The communities are assigned as node attributes in the graph.
   - The number of communities found is printed.
7. Analyzing community sizes and identifying the largest and smallest communities:
   - The script calculates the number of nodes in each community and creates a dictionary with community IDs as keys and node counts as values.
   - The largest and smallest communities are identified and printed.
8. Visualizing the top 3 largest communities:
    - The script selects the nodes belonging to each of the top 3 largest communities.
    - Subgraphs are created for each community.
    - The subgraphs are visualized using the spring layout algorithm and matplotlib.
9. Removing top 3 influential nodes from each community:
    - The script defines a function, top3_removing, which removes the top 3 influential nodes (based on betweenness centrality, closeness centrality, and eigenvector centrality) from each community subgraph.
    - The modified subgraphs are visualized using the spring layout algorithm and matplotlib.
10. Identifying influencers within each community:
    - The script defines a function, top_3, which identifies the top 3 influential nodes within each community subgraph.
    - The influencers are highlighted in yellow in the visualizations.
11. Action plan:
    - A hypothetical action plan is outlined for a digital marketing agency specializing in providing various digital marketing services.
