import ast
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import operator
import os

f = open('structure_of_euclid')
book_structure = ast.literal_eval(f.read())
f.close()

relation_to_pythagorean_props = ['I.4', 'I.8', 'I.26', 'I.27', 'I.28', 'I.29', 'I.30', 'I.31', 'I.33', 'I.34', 'I.35', 'I.36', 'I.37', 'I.38', 'I.39', 'I.40', 'I.41', 'I.42', 'I.43', 'I.44', 'I.45', 'I.46', 'I.47', 'I.48']
conguency_list = ['I.4', 'I.8', 'I.26']
parallel_list = ['I.27', 'I.28', 'I.29', 'I.30', 'I.31', 'I.33', 'I.39', 'I.40']
area_list = ['I.34', 'I.35', 'I.36', 'I.37', 'I.38', 'I.41', 'I.42', 'I.43', 'I.44', 'I.45', 'I.46']
def get_all_relations(book_structure):
	prop_list = set()
	def_list = set()
	cn_list = set()
	post_list = set()

	prop_prop_list = set()

	for prop in book_structure.iterkeys():
		prop_list.add(prop)
		for item in book_structure[prop].iterkeys():
			if item == 'defs':
				for deff in book_structure[prop][item]:
					def_list.add(deff)
			elif item == 'cns':
				for cn in book_structure[prop][item]:
					cn_list.add(cn)
			elif item == 'posts':
				for post in book_structure[prop][item]:
					post_list.add(post)
			elif item == 'props':
				for another_prop in book_structure[prop][item]:
					prop_prop_list.add((prop, another_prop))

	return prop_list, def_list, cn_list, post_list, prop_prop_list

def get_relation_of_one_prop(book_structure, prop):
	prop_prop_list = []
	props = book_structure[prop]['props']
		



prop_prop_list = []
prop_cn_list = []
prop_post_list = []
prop_nodes = []
colors = ['#FF0000', '#00FF00', '#0000FF', '#FF6600', '#FF00FF', ]

def add_prop_edges(book_structure, prop, graph):
	for sub_prop in book_structure[prop]['props']:
		edge = pydot.Edge(sub_prop, prop)
		if sub_prop in conguency_list:
			edge = pydot.Edge(sub_prop, prop, color=colors[0])
			graph.add_node(pydot.Node(sub_prop, style='filled', fillcolor=colors[0]))
		if sub_prop in parallel_list:
			edge = pydot.Edge(sub_prop, prop, color=colors[1])
			graph.add_node(pydot.Node(sub_prop, style='filled', fillcolor=colors[1]))
		if sub_prop in area_list:
			edge = pydot.Edge(sub_prop, prop, color=colors[2])
			graph.add_node(pydot.Node(sub_prop, style='filled', fillcolor=colors[2]))
		if (sub_prop, prop) not in prop_prop_list:
			prop_prop_list.append((sub_prop, prop))
			graph.add_edge(edge)
		add_edges(book_structure, sub_prop, graph)



def add_post_edges(book_structure, prop, graph):
	for sub_post in book_structure[prop]['posts']:
		edge = pydot.Edge(sub_post, prop, color=colors[3])
		graph.add_node(pydot.Node(sub_post, style='filled', fillcolor=colors[3]))
		if (sub_post, prop) not in prop_prop_list:
			prop_prop_list.append((sub_post, prop))
			graph.add_edge(edge)

def add_cn_edges(book_structure, prop, graph):
	for sub_cn in book_structure[prop]['cns']:
		edge = pydot.Edge(sub_cn, prop, color=colors[4])
		graph.add_node(pydot.Node(sub_cn, style='filled', fillcolor=colors[4]))
		if (sub_cn, prop) not in prop_prop_list:
			prop_prop_list.append((sub_cn, prop))
			graph.add_edge(edge)

def add_edges(book_structure, prop, graph):
	# add strict
	if prop in relation_to_pythagorean_props:
		add_prop_edges(book_structure, prop, graph)
		add_post_edges(book_structure, prop, graph)
		add_cn_edges(book_structure, prop, graph)
	

def add_reverse_edges(book_structure, prop, graph):
	sub_prop_list = []
	# graph.add_node('Post.5')
	graph.add_node(pydot.Node("Post.5", style='filled', fillcolor=colors[3]))
	if prop not in prop_nodes:
		prop_nodes.append(prop)
		graph.add_node(pydot.Node(prop))
	if 'Post.5' in book_structure[prop]['posts']:
		if ('Post.5', prop) not in prop_post_list:
			prop_post_list.append(('Post.5', prop))
			# graph.add_edge(edge)
			edge = pydot.Edge('Post.5', prop, color=colors[3])
			graph.add_edge(edge)

	for prop_key in book_structure.iterkeys():
		if prop in book_structure[prop_key]['props']:
			if (prop, prop_key) not in prop_post_list:
				edge = pydot.Edge(prop, prop_key)
				if prop_key in conguency_list:
					edge = pydot.Edge(prop, prop_key, color=colors[0])
					graph.add_node(pydot.Node(prop_key, style='filled', fillcolor=colors[0]))
				if prop_key in parallel_list:
					edge = pydot.Edge(prop, prop_key, color=colors[1])
					graph.add_node(pydot.Node(prop_key, style='filled', fillcolor=colors[1]))
				if prop_key in area_list:
					edge = pydot.Edge(prop, prop_key, color=colors[2])
					graph.add_node(pydot.Node(prop_key, style='filled', fillcolor=colors[2]))
				# graph.add_node(pydot.Node('Post.5', style='filled', fillcolor=colors[3]))
				prop_post_list.append((prop, prop_key))
				graph.add_edge(edge)
				# edge = pydot.Edge(prop, prop_key)
				# graph.add_edge(edge)
				sub_prop_list.append(prop_key)
	for x in sub_prop_list:
		add_reverse_edges(book_structure, x, graph)

		# if prop not in sub_prop_list:
		# 	add_reverse_edges(book_structure, prop_key, graph)

graph = pydot.Dot(graph_type='digraph')
# graph.add_node(pydot.Node('Proposition Conguency', height=0.1, width=0.1, shape='box', label = "Proposition Conguency", color=colors[0], fontcolor=colors[0]))
graph.add_node(pydot.Node('Proposition Parallel', height=0.1, width=0.1, shape='box', label = "Proposition Parallel", color=colors[1], fontcolor=colors[1]))
graph.add_node(pydot.Node('Proposition Area', height=0.1, width=0.1, shape='box', label = "Proposition Area", color=colors[2], fontcolor=colors[2]))
graph.add_node(pydot.Node('Postulate', height=0.1, width=0.1, shape='box', label = "Postulate", color=colors[3], fontcolor=colors[3]))
# graph.add_node(pydot.Node('Common Notion', height=0.1, width=0.1, shape='box', label = "Common Notion", color=colors[4], fontcolor=colors[4]))
# graph.add_edge(pydot.Edge('Proposition Conguency', 'Proposition Parallel', color='white'))
graph.add_edge(pydot.Edge('Proposition Parallel', 'Proposition Area', color='white'))
graph.add_edge(pydot.Edge('Proposition Area', 'Postulate', color='white'))
# graph.add_edge(pydot.Edge('Postulate', 'Common Notion', color='white'))

# add_edges(book_structure, 'I.48', graph)
add_reverse_edges(book_structure, 'I.19', graph)

# graph.write_png('I_48.png')
graph.write_png('I_19.png')

# graph = pydot.Dot(graph_type='digraph')
# for file in os.listdir('../git/pydot/test/graphs'):
# 	if file.split('.')[-1] == 'dot':
# 		pydot.graph_from_dot_file('../git/pydot/test/graphs/' + file).write_png('./sample/' + file.split('.')[0] + '.png')







# G = nx.DiGraph()

# add_reverse_edges(book_structure, 'I.29', G, type=2)

# G.add_nodes_from(prop_list)
# G.add_edges_from(prop_prop_list)

# pos = nx.graphviz_layout(G, prog='dot')

# nx.draw(G, pos)

# nx.draw_networkx_nodes(G, pos, node_size=500)

# nx.draw_networkx_edges(G, pos, width=1, alpha=1, edge_color='black', style='solid')

# nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# plt.axis('off')

# plt.show()
