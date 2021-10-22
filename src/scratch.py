# store the idea with
# make_method() & declare_methods()
# make_operator() & declare_operators()

for key, value in data['Recipes'].items():
		key.replace(' ', '_')
		produce_here = value['Produces'].items()
		for pro, number in produce_here:
			name_of_produce = pro
			# print (name_of_produce)
		my_method = make_method(key, value)
		pyhop.declare_methods('produce_' + name_of_produce, my_method)
		# method_list.append((key, name_of_produce, my_method))
