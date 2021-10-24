# git repo: https://github.com/szhong16/CMPM-146-P4

import pyhop
import json

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

pyhop.declare_methods ('have_enough', check_enough, produce_enough)

def produce (state, ID, item):
	# idea from manual, if it is a tool, check we already made it before or not
	# if item == 'bench' or item == 'furnace' or item == 'iron_axe' or item == 'iron_pickaxe' or \
	# 	item == 'stone_axe' or item == 'stone_pickaxe' or item == 'wooden_axe' or item == 'wooden_pickaxe':
	# 	if getattr(state, ('made_' + item))[ID] is True:
	# 		return False
	# 	else:
	# 		setattr(state, ('made_' + item), {ID: True})
	# 		return [('produce_{}'.format(item), ID)]
	# elif item == 'cart' or item == 'coal' or item == 'cobble' or item == 'ingot' or \
	# 	item == 'ore' or item == 'plank' or item == 'rail' or item == 'stick' or item == 'wood':
	# 	return [('produce_{}'.format(item), ID)]
	# else:
	# 	return False
	return [('produce_{}'.format(item), ID)]

pyhop.declare_methods ('produce', produce)

def make_method (name, rule):

	#sorting the requirement so that we do bench before wood
	def method (state, ID):
		condition = []
		for key, value in rule.items():
			if key != 'Produces':
				if type(value) == dict:
					for k, v in value.items():
						condition.append(('have_enough', ID, k, v))
		condition.append(('op_' + name, ID))
		return condition

	# def method(state, ID):
	# 	return my_method_list
	return method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# print("here is data", data)
	# pyhop.declare_methods(produce_name, *methods)

	# method_list = []
	# making a dict, idea from professor
	# organize this part and try to make it into one function which works for all methods
	# want to create a dict
	# and store all the methods which is for the key
	# try to use pyhop.declare_methods(produce_name, *methods)
	method_dict = {}

	# sort the json on input

	# The organize function, hard code version is below
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=True):
		key = key.replace(' ', '_')
		for name_of_produce in value['Produces'].items():
			# isinstance() method from my friend Yanwen Xu
			# if it is already in method_dict, means it has multiple ways to produce
			# [Ex: wood]
			# separate them by the same of the produces
			# dict: {name, list of method}
			if name_of_produce in method_dict:
				if isinstance(method_dict[name_of_produce], list):
					my_method = make_method(key, value)
					# print(method_dict[item])
					method_dict[name_of_produce].append(my_method)
				else:
					method_dict[name_of_produce] = [method_dict[name_of_produce]]
			else: # only one method for achieve this
				my_method = make_method(key, value)
				method_dict[name_of_produce] = [my_method]

	for name, method in method_dict.items():
		# print(name)
		pyhop.declare_methods('produce_' + name[0], *method)


	# for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=True):
	# 	key = key.replace(' ', '_')
	# 	produce_here = value['Produces'].items()
	# 	for pro, number in produce_here:
	# 		name_of_produce = pro
	# 		print (name_of_produce)
	# 	my_method = make_method(key, value)
	# 	time_for_this = value['Time']
		# print(time_for_this)
		# task_name = 'produce_' + name_of_produce
		# pyhop.declare_methods(name_of_produce, make_method(key, value))
		# method_list.append((key, name_of_produce, my_method, time_for_this))

	# but the current one just hard code it and it works
	# for name, produce_name, method, method_time in method_list:
	# 	if produce_name == 'ore':
	# 		temp_for_ore = []
	# 		for i, j, k, t in method_list:
	# 			# print(i, j, k)
	# 			if j == produce_name:
	# 				temp_for_ore.append(k)
	# 			# sorted(temp_for_ore, key=lambda time: t, reverse=False)
	# 		pyhop.declare_methods('produce_' + produce_name, temp_for_ore[0], temp_for_ore[1])
	# 	elif produce_name == 'wood':
	# 		temp_for_wood = []
	# 		for i, j, k, t in method_list:
	# 			# print(i, j, k)
	# 			if j == produce_name:
	# 				temp_for_wood.append(k)
	# 			# sorted(temp_for_wood, key=lambda time: t, reverse=False)
	# 		pyhop.declare_methods('produce_' + produce_name, temp_for_wood[0], temp_for_wood[1], temp_for_wood[2], temp_for_wood[3])
	# 	elif produce_name == 'coal' or produce_name == 'cobble':
	# 		temp_for_coal_cobble = []
	# 		for i, j, k, t in method_list:
	# 			if j == produce_name:
	# 				temp_for_coal_cobble.append(k)
	# 			# sorted(temp_for_coal_cobble, key=lambda time: t, reverse=False)
	# 		pyhop.declare_methods('produce_' + produce_name, temp_for_coal_cobble[0], temp_for_coal_cobble[1], temp_for_coal_cobble[2])
	# 	else:
	# 		pyhop.declare_methods('produce_' + produce_name, method)
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)
	# pass

def make_operator (rule):

	def operator (state, ID):
		# your code here
		for key, value in rule.items():
			if key == 'Produces':
				for k, v in value.items():
					# get this from set_up_state
					setattr(state, k, {ID: getattr(state, k)[ID] + v})
			if key == 'Consumes':
				for k, v in value.items():
					if getattr(state, k)[ID] >= v:
						setattr(state, k, {ID: getattr(state, k)[ID] - v})
					# else:
					# 	return False
			if key == 'Time':
				if state.time[ID] >= v:
					state.time[ID] -= v
				else:
					return False
		return state
		# pass
	return operator

	# def operator (state, ID):
	# 	# your code here
	# 	pass
	# return operator

def declare_operators (data):
	# your code
	operator_list = []
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=True):
	# for key, value in data['Recipes'].items():
		# print (key, value)
		key = key.replace(' ', '_')
		operator_temp = make_operator(value)
		time_for_oper = value['Time']
		# operator_temp(state, state.ID)
		# iterate the name of op; came from my friend: Yanwen Xu
		operator_temp.__name__ = 'op_' + key
		operator_list.append((operator_temp, time_for_oper))
		sorted(operator_list, key=lambda time: time_for_oper, reverse=False)

		# pyhop.declare_operators(operator)
		# print(operator)

	# total 25 operators
	# hard coded
	for oper, times in operator_list:
	# for oper in operator_list:
		pyhop.declare_operators(oper)
	# pyhop.declare_operators(operator_list[0], operator_list[1], operator_list[2], operator_list[3], operator_list[4], operator_list[5], operator_list[6], operator_list[7], operator_list[8], operator_list[9], operator_list[10], operator_list[11], operator_list[12], operator_list[13], operator_list[14], operator_list[15], operator_list[16], operator_list[17], operator_list[18], operator_list[19], operator_list[20], operator_list[21], operator_list[22], operator_list[23], operator_list[24])

	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	# pass

def add_heuristic (data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters:
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic (state, curr_task, tasks, plan, depth, calling_stack):
		# Idea:  Since for the tools, we only need to make one and use it for ever
		# So we want to made the tools' priority higher than others
		# also we sorted the method list when method is created
		# your code here
		# print(state, curr_task, tasks, plan, depth, calling_stack)
		# if we already call this task before, don't do it repeatly
		if curr_task in tasks:
			return False
		return True # if True, prune this branch

	pyhop.add_check(heuristic)


def set_up_state (data, ID, time=0):
	state = pyhop.State('state')
	state.time = {ID: time}

	for item in data['Items']:
		setattr(state, item, {ID: 0})

	for item in data['Tools']:
		setattr(state, item, {ID: 0})
		setattr(state, 'made_' + item, {ID: False})

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

	state = set_up_state(data, 'agent', time=250) # allot time here
	goals = set_up_goals(data, 'agent')	# agent is the ID

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')

	pyhop.print_operators()
	pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct;
	# try verbose=1 if it is taking too long
	# pyhop.pyhop(state, goals, verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'plank', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'wooden_pickaxe', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'furnace', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'stone_pickaxe', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'iron_pickaxe', 1)], verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 10)], verbose=3)
	pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)
