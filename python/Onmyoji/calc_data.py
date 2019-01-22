import os
import json
import sys
from functools import reduce
from itertools import product
from itertools import chain
from multiprocessing import Pool
from functools import partial
from fixed_data import *


# load data from json file to be calculated by the algorithm 
def get_data(filename):
	if os.path.splitext(filename)[1] != '.json':
		print("Wrong file type, should be a json file")
		return

	else:
		try:
			with open(filename) as content:
				data = json.load(content)
			yuhun_all = dict()
			num = 1
			percentage_list = [u'攻击加成', u'防御加成', u'暴击', u'暴击伤害', u'生命加成', u'效果命中', u'效果抵抗']
			for entry in data:
				if isinstance(entry, dict):
					for element in entry:
						if element in percentage_list:
							entry[element] *= 100
					yuhun_all[num] = entry
					num += 1
			return yuhun_all
		except FileNotFoundError:
			print("Wrong file or file path")


# split data into positions for ease of calculation
def get_data_loc(yuhun):
	if yuhun is None:
		print("No data to be splited")
		return
	else:
		yuhun_loc = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
		for num, data in yuhun.items():
			if isinstance(data, dict):
				loc = data[u'位置']
				yuhun_loc[loc].append({num: data})
		return yuhun_loc


# User input to filter out main possible properties of a single location
# type and min are lists
def filter_prop_single(yuhun_list, main_prop, yuhun_min):
	new = []
	for yuhun in yuhun_list:
		for key, data in yuhun.items():
			i = 0
			while i < len(main_prop):
				if main_prop[i] in data:
					if data[main_prop[i]] >= yuhun_min[i]:
						new.append({key: data})
				i += 1

	return new


# filter by types
def filter_type(yuhun_list, yuhun_type):
	new = []
	for yuhun in yuhun_list:
		for key, data in yuhun.items():
			i = 0
			while i < len(yuhun_type):
				if data[u'御魂类型'] == yuhun_type[i]:
					new.append({key: data})
					break
				i += 1
	return new


# filter by whether the yuhun is +15 6 star
def filter_max(yuhun_list):
	new = []
	for yuhun in yuhun_list:
		for key, data in yuhun.items():
			if data[u'御魂等级'] == 15 and data[u'御魂星级'] == 6:
				new.append({key: data})
	return new


# filter single yuhun that are not good enough
# [暴击， 爆伤， 攻击加成， 速度， 生命加成， 效果抵抗， 效果命中]
def cal_effective(yuhun, effective_list):
	baoji = baoshang = gongji = sudu = shengming = dikang = mingzhong = 0
	if u'暴击' in yuhun:
		baoji = yuhun[u'暴击']
		if baoji >= 55:
			baoji = baoji - 55
		baoji = baoji / 2.66
	if u'暴击伤害' in yuhun:
		baoshang = yuhun[u'暴击伤害']
		if baoshang >= 89:
			baoshang = baoshang - 89
		baoshang = baoshang / 3.66
	if u'攻击加成' in yuhun:
		gongji = yuhun[u'攻击加成']
		if gongji >= 55:
			gongji = gongji - 55
		gongji = gongji / 2.66
	if u'速度' in yuhun:
		sudu = yuhun[u'速度']
		if sudu >= 57:
			sudu = sudu - 57
		sudu = sudu / 2.66
	if u'生命加成' in yuhun:
		shengming = yuhun[u'生命加成']
		if shengming >= 55:
			shengming = shengming - 55
		shengming = shengming / 2.66
	if u'效果抵抗' in yuhun:
		dikang = yuhun[u'效果抵抗']
		if dikang >= 55:
			dikang = dikang - 55
		dikang = dikang / 3.66
	if u'效果命中' in yuhun:
		mingzhong = yuhun[u'效果命中']
		if mingzhong >= 55:
			mingzhong = mingzhong - 55
		mingzhong = mingzhong / 3.66
	result = baoji * effective_list[0] + baoshang * effective_list[1] + gongji * effective_list[2] + sudu * \
			 effective_list[3] + shengming * effective_list[4] + dikang * effective_list[5] + mingzhong * \
			 effective_list[6]
	return result


# one whole position with effect
def filter_effective(yuhun_list, effective_list, effective):
	new = []
	for yuhun in yuhun_list:
		for key, data in yuhun.items():
			result = cal_effective(data, effective_list)
			if result >= effective:
				new.append({key: data})
	return new


# User input filter main property of loc2, loc4 and loc6
def filter_all(yuhun_loc, l2_type, l2_min, l4_type, l4_min, l6_type, l6_min, effective_list, effective, attack_only,
			   health_only):
	print('before filter by loc prop and type %s' % str([len(d) for d in yuhun_loc.values()]))

	for loc, data in yuhun_loc.items():
		yuhun_loc[loc] = filter_max(yuhun_loc[loc])
		if loc == 6 or loc == 2 or loc == 4:  # don't limit #6 as it's the most difficult part
			yuhun_loc[loc] = filter_effective(yuhun_loc[loc], effective_list, effective - 3)
		else:
			yuhun_loc[loc] = filter_effective(yuhun_loc[loc], effective_list, effective)
		if attack_only:
			yuhun_loc[loc] = filter_type(yuhun_loc[loc], ATTACK_YUHUN_TYPE)
		if health_only:
			yuhun_loc[loc] = filter_type(yuhun_loc[loc], HEALTH_YUHUN_TYPE)

	if l2_type:
		yuhun_loc[2] = filter_prop_single(yuhun_loc[2], l2_type, l2_min)
	if l4_type:
		yuhun_loc[4] = filter_prop_single(yuhun_loc[4], l4_type, l4_min)
	if l6_type:
		yuhun_loc[6] = filter_prop_single(yuhun_loc[6], l6_type, l6_min)
	print('after filter by loc prop and type %s' % str([len(d) for d in yuhun_loc.values()]))

	return yuhun_loc


# give a set of yuhuns, get the number and types of yuhuns
def get_comb_type(yuhun_comb):
	result = {}
	for key, yuhun in yuhun_comb.items():
		yuhun_type = yuhun.get(u'御魂类型')
		if yuhun_type not in result:
			result[yuhun_type] = 1
		else:
			result[yuhun_type] += 1
	return result


# given a set of 6 yuhuns, get the full detail of the comb 
def cal_comb_property(yuhun_comb):
	result = {}
	all_yuhun_prop = YUHUN_PROP_LIST[3::]
	yuhun_increase = YUHUN_INCREASE
	result = {k: 0 for k in all_yuhun_prop}
	# first ignore the yuhun bonus
	for key, yuhun in yuhun_comb.items():
		for each_type in all_yuhun_prop:
			if (yuhun.get(each_type)):
				result[each_type] += yuhun.get(each_type)
	# add properties given by sets of yuhun bonus
	type_comb = get_comb_type(yuhun_comb)
	for type_name, number in type_comb.items():
		if number >= 2:
			times = 1
			if number == 6:
				times = 2
			prop_type = yuhun_increase[type_name].get(u'加成类型')
			if prop_type:
				result[prop_type] += times * yuhun_increase[type_name].get(u'加成数值')
	return result


# form all possible combinations based on user input
def form_all_combs(yuhun_list, type_list):
	# init
	total_comb = 0
	result = []
	if type_list == {}:
		# no type requests(sanjian)
		total_comb = reduce(lambda x, y: x * y, map(len, yuhun_list.values()))
		print("Total combinations: ", total_comb)
		return product(*yuhun_list.values()), total_comb
	main_type = None
	minor_type = None
	for yuhun_type, num in type_list.items():
		if type_list[yuhun_type] == 4:
			main_type = yuhun_type
		if type_list[yuhun_type] == 2:
			minor_type = yuhun_type
		if type_list[yuhun_type] == 6:
			main_type = yuhun_type
			minor_type = yuhun_type
	main_yuhun = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
	minor_yuhun = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
	other_yuhun = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

	temp_type = []
	if minor_type in INCREASE_LIST:
		for name, data in YUHUN_INCREASE.items():
			if data["加成类型"] == minor_type:
				temp_type.append(name)
		minor_type = temp_type
	else:
		minor_type = [minor_type]

	other_type = []
	for name, data in YUHUN_INCREASE.items():
		if name != main_type:
			other_type.append(name)

	for i in range(1, 7):
		main_yuhun[i] = filter_type(yuhun_list[i], [main_type])
		if minor_type:
			minor_yuhun[i] = filter_type(yuhun_list[i], minor_type)
		other_yuhun[i] = filter_type(yuhun_list[i], other_type)

	total_comb += reduce(lambda x, y: x * y, map(len, main_yuhun.values()))
	result.append(product(*main_yuhun.values()))

	# 4+2
	for i in range(1, 7):
		for j in range(i + 1, 7):
			temp_yuhun = {x: main_yuhun[x] for x in range(1, 7)}
			if minor_type:
				temp_yuhun[i] = minor_yuhun[i]
				temp_yuhun[j] = minor_yuhun[j]
			else:
				temp_yuhun[i] = other_yuhun[i]
				temp_yuhun[j] = other_yuhun[j]
			total_comb += reduce(lambda x, y: x * y, map(len, temp_yuhun.values()))
			result.append(product(*temp_yuhun.values()))

	# 5+1
	if not minor_type:
		for i in range(1, 7):
			temp_yuhun = main_yuhun
			temp_yuhun[i] = other_yuhun[i]
			total_comb += reduce(lambda x, y: x * y, map(len, temp_yuhun.values()))
			result.append(product(*temp_yuhun.values()))

	print("Total combinations: ", total_comb)
	return chain(*result), total_comb


def single_process(yuhun_combo, shishen_info, user_request):
	yuhun_combo_dict = {}
	for each_yuhun in yuhun_combo:
		for key, data in each_yuhun.items():
			yuhun_combo_dict[key] = data
	combo_data = cal_comb_property(yuhun_combo_dict)
	crit = shishen_info[u"暴击"] + combo_data[u"暴击"]
	crit_dmg = shishen_info[u"暴击伤害"] + combo_data[u"暴击伤害"]
	base_attack = shishen_info[u"攻击"] * (1 + combo_data[u"攻击加成"] / 100) + combo_data[u"攻击"]
	base_health = shishen_info[u"生命"] * (1 + combo_data[u"生命加成"] / 100) + combo_data[u"生命"]
	attack_data = base_attack * crit_dmg / 100
	health_data = base_health * crit_dmg / 100
	speed = shishen_info[u"速度"] + combo_data[u"速度"]
	resistance = shishen_info[u"效果抵抗"] + combo_data[u"效果抵抗"]
	hit = shishen_info[u"效果命中"] + combo_data[u"效果命中"]
	res_hit = resistance + hit

	result = dict()
	combo = []
	for id, data in yuhun_combo_dict.items():
		combo.append(id)
	result["combo"] = combo
	result[u"总攻击"] = base_attack
	result[u"总生命"] = base_health
	result[u"暴击"] = crit
	result[u"暴击伤害"] = crit_dmg
	result[u"攻击x爆伤"] = attack_data
	result[u"生命x爆伤"] = health_data
	result[u"式神速度"] = speed
	result[u"式神抵抗"] = resistance
	result[u"式神命中"] = hit
	result[u"抵抗命中"] = res_hit
	result[u"速度"] = speed

	if u"暴击" in user_request:
		baoji = user_request[u"暴击"]
		if crit > baoji["up"] or crit < baoji["low"]:
			return
	if u"生命" in user_request:
		shengming = user_request[u"生命"]
		if base_health > shengming["up"] or base_health < shengming["low"]:
			return
	if u"速度" in user_request:
		sudu = user_request[u"速度"]
		if speed > sudu["up"] or speed < sudu["low"]:
			return
	if u"攻击x爆伤" in user_request:
		gongbao = user_request[u"攻击x爆伤"]
		if attack_data > gongbao["up"] or attack_data < gongbao["low"]:
			return
	if u"生命x爆伤" in user_request:
		shengbao = user_request[u"生命x爆伤"]
		if health_data > shengbao["up"] or health_data < shengbao["low"]:
			return
	if u"效果抵抗" in user_request:
		dikang = user_request[u"效果抵抗"]
		if resistance > dikang["up"] or resistance < dikang["low"]:
			return
	if u"效果命中" in user_request:
		mingzhong = user_request[u"效果命中"]
		if hit > mingzhong["up"] or hit < mingzhong["low"]:
			return
	if u"命中抵抗" in user_request:
		dikmz = user_request[u"命中抵抗"]
		if res_hit > dikmz["up"] or res_hit < dikmz["low"]:
			return
	return result


# filter all combos given shishen_info and user_request
def filter_combo(yuhun_combo_list, shishen_info, user_request):
	p = Pool()
	x = partial(single_process, shishen_info=shishen_info, user_request=user_request)
	raw_list = p.map(x, yuhun_combo_list)
	p.close()
	p.join()
	raw_list = [x for x in raw_list if x is not None]
	result_list = []
	memory = []
	for result in raw_list:
		if result["combo"] not in memory:
			memory.append(result["combo"])
			result_list.append(result)
	return result_list



