# store the idea with
# make_method() & declare_methods()
# make_operator() & declare_operators()

def make_method (name, rule):
	# print(name, rule)
	if 'Requires' in rule:
		require = rule['Requires']
		# print(require)
	else:
		require = None

	if 'Consumes' in rule:
		consume = rule['Consumes']
		# print(consume)
	else:
		consume = None

	condition = []

	def method (state, ID):
	# def method():
		print(1)
		if consume:
			for item in rule['Consumes']:
				item_cost = rule['Consumes'][item]
				condition.append(('have_enough', ID, state[ID], item_cost))
		if require:
			# print(require)
			for item in require:
				condition.append(('have_enough', ID, state[ID], 1))
		print(condition)
		return condition
		# your code here
		# pass

	return method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# print("here is data", data)

	method_list = []

	# sort the json on input
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=False):
		my_method = make_method(key, value)
		method_list.append(my_method)
		# print(key, value)

	# for key, value in method_list:
		# pyhop.declare_methods('produce_' + key, m, m)
		# pyhop.declare_methods()
	# method_list.sort()
	# sorted list of methods
	# pyhop.declare_methods('foo', m, m)
	# pyhop.declare_methods(method_list)
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)
	# pass

def make_operator (rule):

	if 'Produces' in rule:
		produces = rule['Produces']
		print("produces", produces)
	else:
		produces = None

	if 'Consumes' in rule:
		consume = rule['Consumes']
		print("consume", consume)
	else:
		consume = None

	def operator (state, ID):
		# your code here
		if consume:
			for key, value in consume.items():
				state[ID] -= value
		if produces:
			for key, value in produces.items():
				state[ID] += value
		# return state
		# pass
	return operator

def declare_operators (data):
	# your code
	for key, value in sorted(data['Recipes'].items(), key=lambda item: item[1]["Time"], reverse=False):
		# print(data['Recipes'].items())
		# operator = make_operator(value)
		pyhop.declare_operators(make_operator(value))

	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	pass


