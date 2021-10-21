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
				# condition.append(('have_enough', ID, item, item_cost))
		if require:
			# print(require)
			for item in require:
				# condition.append(('have_enough', ID, item, 1))
		print(condition)
		return condition
		# your code here
		# pass
