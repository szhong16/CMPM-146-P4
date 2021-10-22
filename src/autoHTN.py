import pyhop
import json

from collections import namedtuple

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

pyhop.declare_methods ('have_enough', check_enough, produce_enough)

def produce (state, ID, item):
	return [('produce_{}'.format(item), ID)]

pyhop.declare_methods ('produce', produce)

def make_method (name, rule):

	my_method_list = []
	id = 'agent'

	for key, value in rule.items():
		if key != 'Produces':
			if type(value) == dict:
				for k, v in value.items():
					my_method_list.append(('have_enough', id, k, v))
	my_method_list.append(('op_' + name, id))

	def method(state, ID):
		return my_method_list
	return method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# print("here is data", data)

	method_list = []
	meth_name_list = []

	# sort the json on input
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=True):
		key = key.replace(' ', '_')
		produce_here = value['Produces'].items()
		for pro, number in produce_here:
			name_of_produce = pro
			# print (name_of_produce)
		my_method = make_method(key, value)
		method_list.append((key, name_of_produce, my_method))
		print(method_list)

	# reversed(method_list)
		# meth_name_list = [(name_of_produce, key)]
		# print (meth_name_list[0][1])
		# counter = 0
		# if not meth_name_list:
		# 	meth_name_list = [(name_of_produce, key)]
		# 	print("initial", name_of_produce, key)
		# else:
		# 	# for name, m in meth_name_list:
		# 	# 	print(name, m)
		# 	# 	if name_of_produce == name:
		# 	# 		meth_name_list[counter].append(key)
		# 	# 		counter += 1
		# 	# 	else:
		# 	# 		print ("2")
		# 		# meth_name_list.append(produce, key)
		# 	print(key, value)
	for name, produce_name, method in method_list:
		if produce_name == "cart" or produce_name == "rail" or \
			produce_name == "bench" or produce_name == "furnace" or \
			produce_name == "iron_axe" or produce_name == "iron_pickaxe" or \
			produce_name == "stone_axe" or produce_name == "stone_pickaxe" or \
			produce_name == "wooden_axe" or produce_name == "wooden_pickaxe" or \
			produce_name == "plank" or produce_name == "stick" or produce_name == "ingot":
			pyhop.declare_methods('produce_' + produce_name, method)
		elif produce_name == "wood" or produce_name == "coal" or \
			produce_name == "ore" or produce_name == "cobble":
			for i, j, k in method_list:
				temp = []
				if j == produce_name:
					temp.append(name)
					# print(name)
			pyhop.declare_methods('produce_' + produce_name, method)
		# pyhop.declare_methods('produce_' + key, m, m)
		# pyhop.declare_methods()
	# method_list.sort()
	# sorted list of methods
	# pyhop.declare_methods('foo', m, m)
	# pyhop.declare_methods(method_list)
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)
	# pass

def make_operator (rule):

	def operator (state, ID):
		# your code here
		pass
	return operator

def declare_operators (data):
	# your code
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=False):
		# print(data['Recipes'].items())
		# operator = make_operator(value)
		pyhop.declare_operators(make_operator(value))

	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	pass

def add_heuristic (data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters:
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic (state, curr_task, tasks, plan, depth, calling_stack):
		# Idea:  Since for the tools, we only need to make one and use it for ever
		# So we want to made the tools' priority higher than others
		# your code here
		return False # if True, prune this branch

	pyhop.add_check(heuristic)


def set_up_state (data, ID, time=0):
	state = pyhop.State('state')
	state.time = {ID: time}

	for item in data['Items']:
		setattr(state, item, {ID: 0})

	for item in data['Tools']:
		setattr(state, item, {ID: 0})

	for item, num in data['Initial'].items():
		setattr(state, item, {ID: num})

	return state

def set_up_goals (data, ID):
	goals = []
	for item, num in data['Goal'].items():
		goals.append(('have_enough', ID, item, num))

	return goals

if __name__ == '__main__':
	rules_filename = 'crafting.json'

	with open(rules_filename) as f:
		data = json.load(f) # returns a dict
		# print(data.keys())

	state = set_up_state(data, 'agent', time=239) # allot time here
	goals = set_up_goals(data, 'agent')	# agent is the ID

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')

	pyhop.print_operators()
	pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct;
	# try verbose=1 if it is taking too long
	pyhop.pyhop(state, goals, verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)
