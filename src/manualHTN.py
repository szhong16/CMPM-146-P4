import pyhop

'''begin operators'''

def op_punch_for_wood (state, ID):
	if state.time[ID] >= 4:
		state.wood[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_craft_wooden_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
		state.wooden_axe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

# new operators

def op_craft_iron_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >=2:
		state.iron_axe[ID] += 1
		state.ingot[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_stone_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
		state.stone_axe[ID] += 1
		state.cobble[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_wooden_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
		state.wooden_pickaxe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_iron_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >=2:
		state.iron_pickaxe[ID] += 1
		state.ingot[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_stone_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
		state.stone_pickaxe[ID] += 1
		state.cobble[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_furnace_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 8:
		state.furnace[ID] += 1
		state.cobble[ID] -= 8
		state.time[ID] -= 1
		return state
	return False

def op_mining_for_coal_wooden (state, ID):
	if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.wooden_pickaxe -= 1
		state.time[ID] -= 4
		return state
	return False

def op_mining_for_coal_iron (state, ID):
	if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.iron_pickaxe -= 1
		state.time[ID] -= 1
		return state
	return False

def op_mining_for_coal_stone (state, ID):
	if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.stone_pickaxe -= 1
		state.time[ID] -= 2
		return state
	return False

def op_mining_for_ore_iron (state, ID):
	if state.time[ID] >= 2 and state.iron_pickaxe[ID] >= 1:
		state.ore[ID] += 1
		state.iron_pickaxe -= 1
		state.time[ID] -= 2
		return state
	return False

def op_mining_for_ore_stone (state, ID):
	if state.time[ID] >= 4 and state.stone_pickaxe[ID] >= 1:
		state.ore[ID] += 1
		state.stone_pickaxe -= 1
		state.time[ID] -= 4
		return state
	return False

def op_mining_for_cobble_iron (state, ID):
	if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.iron_pickaxe -= 1
		state.time[ID] -= 1
		return state
	return False

def op_mining_for_cobble_stone (state, ID):
	if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.stone_pickaxe -= 1
		state.time[ID] -= 2
		return state
	return False

def op_mining_for_cobble_wooden (state, ID):
	if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.wooden_pickaxe -= 1
		state.time[ID] -= 4
		return state
	return False

def op_crafting_for_plank (state, ID):
	if state.time[ID] >= 1 and state.wood[ID] >= 1:
		state.plank[ID] += 4
		state.wood[ID] -= 1
		state.time[ID] -= 1
		return state
	return False

def op_crafting_for_stick (state, ID):
	if state.time[ID] >= 1 and state.plank[ID] >= 2:
		state.stick[ID] += 4
		state.plank[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_crafting_for_bench (state, ID):
	if state.time[ID] >= 1 and state.plank[ID] >= 4:
		state.bench[ID] += 1
		state.plank[ID] -= 4
		state.time[ID] -= 1
		return state
	return False

def op_craft_rail_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 6 and state.stick[ID] >= 1:
		state.rail[ID] += 16
		state.ingot[ID] -= 6
		state.stick[ID] -= 1
		state.time[ID] -= 1
		return state
	return False

def op_craft_cart_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 5:
		state.cart[ID] += 1
		state.ingot[ID] -= 5
		state.time[ID] -= 1
		return state
	return False

def op_smelf_ore_in_furnace (state, ID):
	if state.time[ID] >= 5 and state.furnace[ID] >= 1 and state.coal[ID] >= 1 and state.ore[ID] >= 1:
		state.ingot[ID] += 1
		state.coal[ID] -= 1
		state.ore[ID] -= 1
		state.time[ID] -= 5
		return state
	return False

# your code here

pyhop.declare_operators (op_punch_for_wood, op_craft_wooden_axe_at_bench)

'''end operators'''

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

def produce (state, ID, item):
	if item == 'wood': 
		return [('produce_wood', ID)]
	# your code here
	elif item == 'wooden_axe':
		# this check to make sure we're not making multiple axes
		if state.made_wooden_axe[ID] is True:
			return False
		else:
			state.made_wooden_axe[ID] = True
		return [('produce_wooden_axe', ID)]
	else:
		return False

pyhop.declare_methods ('have_enough', check_enough, produce_enough)
pyhop.declare_methods ('produce', produce)

'''begin recipe methods'''

def punch_for_wood (state, ID):
	return [('op_punch_for_wood', ID)]

def craft_wooden_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_axe_at_bench', ID)]

# new recipe
def craft_iron_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_axe_at_bench', ID)]

def craft_stone_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_iron_axe_at_bench', ID)]

def craft_wooden_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_pickaxe_at_bench', ID)]

def craft_stone_pickaxe_at_bench (state, ID): #稿子 use for mining ore
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_pickaxe_at_bench', ID)]

def craft_iron_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_pickaxe_at_bench', ID)]

def craft_furnace_at_bench (state, ID): #熔矿炉 somewhere you use to melt metal
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 8), ('op_craft_furnace_at_bench', ID)]

def mining_for_coal_wooden (state, ID):
	return  [('op_mining_for_coal_wooden'), ID]

def mining_for_coal_iron (state, ID):
	return [('op_mining_for_coal_iron'), ID]

def mining_for_coal_stone (state, ID):
	return [('op_mining_for_coal_stone'), ID]

def mining_for_ore_iron (state, ID):
	return  [('op_mining_for_ore_iron'), ID]

def mining_for_ore_stone (state, ID):
	return  [('op_mining_for_ore_stone'), ID]

def mining_for_cobble_iron (state, ID):
	return [('op_mining_for_cobble_iron'), ID]

def mining_for_cobble_stone (state, ID):
	return [('op_mining_for_cobble_stone'), ID]

def mining_for_cobble_wooden (state, ID):
	return [('op_mining_for_cobble_wooden'), ID]

def crafting_for_plank (state, ID):
	return [('op_crafting_for_plank'), ID]

def crafting_for_stick (state, ID):
	return [('op_crafting_for_stick'), ID]

def crafting_for_bench (state, ID):
	return [('op_crafting_for_bench'), ID]

def craft_rail_at_bench (state, ID): #铁轨，扶手
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 1), ('have_enough', ID, 'ingot', 6), ('op_craft_rail_at_bench', ID)]

def craft_cart_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 5), ('op_craft_cart_at_bench', ID)]

def smelf_ore_in_furnace (state, ID):
	return [('have_enough', ID, 'furnace', 1), ('have_enough', ID, 'coal', 1), ('have_enough', ID, 'ore', 1), ('op_smelf_ore_in_furnace', ID)]

# your code here

pyhop.declare_methods ('produce_wood', punch_for_wood)
pyhop.declare_methods ('produce_wooden_axe', craft_wooden_axe_at_bench)

'''end recipe methods'''

# declare state
state = pyhop.State('state')
state.wood = {'agent': 0}
state.time = {'agent': 4}
# state.time = {'agent': 46}
state.wooden_axe = {'agent': 0}
state.made_wooden_axe = {'agent': False}
# your code here 

# pyhop.print_operators()
# pyhop.print_methods()

pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=3)
# pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 12)], verbose=3)
