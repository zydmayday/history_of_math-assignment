# coding: utf-8
# 梦幻金花的玩法：
# 每个人发六张牌，分别配成1,2,3张，三种组合。
# 每一组分别比大小
# 第一组K最大，A最小
# 第二组，数字牌记点，人头牌为半点，十点半为最大，超过的算输
# 第三组，类似炸金花，三个A最大，其次同花顺，其次同花，其次顺清，再次对子，以此类推
# 翻倍：第一组K翻倍，第二组十点半翻倍，第三组同花顺翻两倍，豹子翻三倍

# 目标：设计一个算法，来判断如何配牌赢的概率最大
# 分析：6张牌一共有6*5*4一共120种组合。从配出的组合中抽取特征量，建立方程，算出此组合的评估值。
# 通过不断的和自己进行比赛，更新特征量的参数，得出最优解。
# 每一轮下来，都会计算分数，通过计算的分数可以对参数进行调整。

# features: [ 第一组值大于7， 第二组值大于7，第三组存在对子， 第三组存在同花，第三组存在顺子，第三组存在同花顺，第三组存在豹子，第一组牌有K，第二组是10点半, 第二组爆了 ]

# 1. 建立发牌模型

import random
import copy

class FantasySix:

	def __init__(self, playerNumber = 2):
		self.playerNumber = playerNumber
		# self.cards = [
		# 	[1,2,3,4,5,6,7,8,9,10,11,12,13], # 红桃
		# 	[1,2,3,4,5,6,7,8,9,10,11,12,13], # 草花
		# 	[1,2,3,4,5,6,7,8,9,10,11,12,13], # 方块
		# 	[1,2,3,4,5,6,7,8,9,10,11,12,13], # 黑桃
		# ]
		self.cards = [
		{'A': 1},{'A': 2},{'A': 3},{'A': 4},{'A': 5},{'A': 6},{'A': 7},{'A': 8},{'A': 9},{'A': 10},{'A': 11},{'A': 12},{'A': 13},
		{'B': 1},{'B': 2},{'B': 3},{'B': 4},{'B': 5},{'B': 6},{'B': 7},{'B': 8},{'B': 9},{'B': 10},{'B': 11},{'B': 12},{'B': 13},
		{'C': 1},{'C': 2},{'C': 3},{'C': 4},{'C': 5},{'C': 6},{'C': 7},{'C': 8},{'C': 9},{'C': 10},{'C': 11},{'C': 12},{'C': 13},
		{'D': 1},{'D': 2},{'D': 3},{'D': 4},{'D': 5},{'D': 6},{'D': 7},{'D': 8},{'D': 9},{'D': 10},{'D': 11},{'D': 12},{'D': 13}
		]
		# [
		# {'1': 1},{'1': 2},{'1': 3},{'1': 4},{'1': 5},{'1': 6},{'1': 7},{'1': 8},{'1': 9},{'1': 0},{'1': 'a'},{'1': 'b'},{'1': 'c'},
		# {'2': 1},{'2': 2},{'2': 3},{'2': 4},{'2': 5},{'2': 6},{'2': 7},{'2': 8},{'2': 9},{'2': 0},{'2': 'a'},{'2': 'b'},{'2': 'c'},
		# {'3': 1},{'3': 2},{'3': 3},{'3': 4},{'3': 5},{'3': 6},{'3': 7},{'3': 8},{'3': 9},{'3': 0},{'3': 'a'},{'3': 'b'},{'3': 'c'},
		# {'4': 1},{'4': 2},{'4': 3},{'4': 4},{'4': 5},{'4': 6},{'4': 7},{'4': 8},{'4': 9},{'4': 0},{'4': 'a'},{'4': 'b'},{'4': 'c'}
		# ]

	def resetCards(self):
		self.cards = [
		{'A': 1},{'A': 2},{'A': 3},{'A': 4},{'A': 5},{'A': 6},{'A': 7},{'A': 8},{'A': 9},{'A': 10},{'A': 11},{'A': 12},{'A': 13},
		{'B': 1},{'B': 2},{'B': 3},{'B': 4},{'B': 5},{'B': 6},{'B': 7},{'B': 8},{'B': 9},{'B': 10},{'B': 11},{'B': 12},{'B': 13},
		{'C': 1},{'C': 2},{'C': 3},{'C': 4},{'C': 5},{'C': 6},{'C': 7},{'C': 8},{'C': 9},{'C': 10},{'C': 11},{'C': 12},{'C': 13},
		{'D': 1},{'D': 2},{'D': 3},{'D': 4},{'D': 5},{'D': 6},{'D': 7},{'D': 8},{'D': 9},{'D': 10},{'D': 11},{'D': 12},{'D': 13}
		]

	def renderCards(self, cards):
		returnCards = [[],[],[],[],[],[]]
		for i, c in enumerate(cards):
			newCard = ''
			if c.keys()[0] == 'A':
				newCard += '1'
			elif c.keys()[0] == 'B':
				newCard += '2'
			elif c.keys()[0] == 'C':
				newCard += '3'
			elif c.keys()[0] == 'D':
				newCard += '4'
			if c.values()[0] == 10:
				newCard += '0'
			elif c.values()[0] == 11:
				newCard += 'a'
			elif c.values()[0] == 12:
				newCard += 'b'
			elif c.values()[0] == 13:
				newCard += 'c'
			else:
				newCard += str(c.values()[0])

			returnCards[i].append(newCard)
			returnCards[i].append(c)
		return returnCards


	def getTypes(self):
		types = []
		for index, t in enumerate(self.cards):
			if t != []:
				types.append(index)
		return types

	def getCards(self):
		return self.cards

	def getDuplicateValueList(self, list, value):
		returnList = []
		for index, t in enumerate(list):
			if t == value:
				returnList.append(index)
		return returnList

	# 发牌
	def dealCard(self):
		cards = self.cards
		dealCards = []

		for i in range(0, self.playerNumber):
			dealCard = []
			for j in range(0,6):
				card = cards[random.randint(0,len(cards)-1)]
				cards.remove(card)
				dealCard.append(card)
			dealCards.append(dealCard)

		return dealCards

	def changeScore(self, players, plist, s):
		for i in plist:
			players[i].addScore(s)

	def getResult(self, players):
		groups = []
		features = []
		for p in players:
			group = p.getGroup()
			groups.append(group)
			feature, groupNumbers = p.getFeatures(group)
			features.append(feature)

		# 整理牌组
		step1 = []
		step2 = []
		step3 = []
		for index, g in enumerate(groups):
			step1.append(players[index].getGroupNumbers()[0])
			step2.append(players[index].getGroupNumbers()[1] + players[index].getGroupNumbers()[2])
			step3.append(features[index][3:8])

		# 评估
		step1Winners = self.getDuplicateValueList(step1, max(step1))
		step1Losers = self.getDuplicateValueList(step1, min(step1))

		if len(step1Winners) == 6:
			step1Winners = []

		if len(step1Losers) == 6:
			step1Losers = []

		rate = 1
		for s1 in step1:
			if s1 == 13:
				rate *= 2

		# self.changeScore(players, step1Winners, 1)
		self.changeScore(players, step1Losers, -1 * rate)

		step2Losers = []
		isBoomed = False
		for index, s2 in enumerate(step2):
			if s2 > 10.5:
				isBoomed = True
				step2Losers.append(index)
				step2[index] = -1

		rate = 1
		for s2 in step2:
			if s2 == 10.5:
				rate *= 2

		# 如果是超过10点半，必须扣分
		self.changeScore(players, step2Losers, -2 * rate)
		
		step2Losers = []

		if not isBoomed:
			step2Losers = self.getDuplicateValueList(step2, min(step2))
		step2Winners = self.getDuplicateValueList(step2, max(step2))

		if len(step2Winners) == 6:
			step2Winners = []

		if len(step2Losers) == 6:
			step2Losers = []


		# self.changeScore(players, step2Winners, 2)
		self.changeScore(players, step2Losers, -2 * rate)

		step3Rank = []
		bestType = -1 # 最开始认定为最差的情况
		worstType = 4 
		for s3 in step3:
			if s3[0] == 1: # 对子
				bestType = 0
				worstType = 0
				step3Rank.append(0)
			elif s3[1] == 1: # 顺子
				bestType = 1
				if worstType > 1:
					worstType = 1
				step3Rank.append(1)
			elif s3[2] == 1: # 同花
				bestType = 2
				if worstType > 2:
					worstType = 2
				step3Rank.append(2)
			elif s3[3] == 1: # 同花顺
				bestType = 3
				if worstType > 3:
					worstType = 3
				step3Rank.append(3)
			elif s3[4] == 1: # 豹子
				bestType = 4
				step3Rank.append(4)
			else: # 单牌
				worstType = -1
				step3Rank.append(-1)

		step3Winners = self.getDuplicateValueList(step3Rank, max(step3Rank))
		step3Losers = self.getDuplicateValueList(step3Rank, min(step3Rank))

		if len(step3Winners) > 1:
			bestWinners = []
			bestCard3 = [0,0,0]
			for s3w in step3Winners:
				card3 = sorted(players[s3w].getGroupNumbers()[3:6])
				if bestType == 0:
					for index, c in enumerate(card3):
						if c == 1:
							card3[index] = 14
					if bestCard3[1] < card3[1]:
						bestWinners = [s3w]
						bestCard3 = card3
					elif bestCard3[1] == card3[1] and bestCard3[0] < card3[0] or bestCard3[1] == card3[1] and bestCard3[2] < card3[2]:
						bestWinners = [s3w]
						bestCard3 = card3
					elif bestCard3[1] == card3[1] and bestCard3[0] == card3[0] and bestCard3[2] == card3[2]:
						bestWinners.append(s3w)
						bestCard3 = card3
				elif bestType == -1:
					for index, c in enumerate(card3):
						if c == 1:
							card3[index] = 14
					if cmp(bestCard3, card3) == 0:
						bestWinners.append(s3w)
						bestCard3 = card3
					elif bestCard3[2] < card3[2]:
						bestWinners = [s3w]
						bestCard3 = card3
					elif bestCard3[2] == card3[2] and bestCard3[1] < card3[1]:
						bestWinners = [s3w]
						bestCard3 = card3
					elif bestCard3[2] == card3[2] and bestCard3[1] == card3[1] and bestCard3[0] < card3[0]:
						bestWinners = [s3w]
						bestCard3 = card3
				else:
					if bestCard3[2] < card3[2]:
						bestWinners = [s3w]
						bestCard3 = card3
					elif bestCard3[2] == card3[2]:
						bestWinners.append(s3w)
						bestCard3 = card3
			step3Winners = bestWinners
		if len(step3Losers) > 1:
			# bestWinners = [step3Winners[0]]
			bestLoser = []
			# bestWinnersCard3 = sorted(players[bestWinners[0]].getGroupNumbers()[3:6])
			bestLoserCard3 = [14,14,14]
			for s3w in step3Losers:
				card3 = sorted(players[s3w].getGroupNumbers()[3:6])
				if worstType == -1:
					for index, c in enumerate(card3):
						if c == 1:
							card3[index] = 14
					if cmp(bestLoserCard3, card3) == 0:
						bestLoser.append(s3w)
						bestLoserCard3 = card3
					elif bestLoserCard3[2] > card3[2]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
					elif bestLoserCard3[2] == card3[2] and bestLoserCard3[1] > card3[1]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
					elif bestLoserCard3[2] == card3[2] and bestLoserCard3[1] == card3[1] and bestLoserCard3[0] > card3[0]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
				elif worstType == 0:
					for index, c in enumerate(card3):
						if c == 1:
							card3[index] = 14
					if bestLoserCard3[1] > card3[1]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
					elif bestLoserCard3[1] == card3[1] and bestLoserCard3[0] > card3[0] or bestLoserCard3[1] == card3[1] and bestLoserCard3[2] > card3[2]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
					elif bestLoserCard3[1] == card3[1] and bestLoserCard3[0] == card3[0] and bestLoserCard3[2] == card3[2]:
						bestLoser.append(s3w)
						bestLoserCard3 = card3
				else:
					if bestLoserCard3[2] > card3[2]:
						bestLoser = [s3w]
						bestLoserCard3 = card3
					elif bestLoserCard3[2] == card3[2]:
						bestLoser.append(s3w)
						bestLoserCard3 = card3
			step3Losers = bestLoser

		if len(step3Losers) == 6:
			step3Losers = []
		if len(step3Winners) == 6:
			step3Winners = []

		rate = 1
		for s3 in step3:
			if s3[3] == 1:
				rate *= 2
			elif s3[4] == 1:
				rate *= 3

		# self.changeScore(players, step3Winners, 3)
		self.changeScore(players, step3Losers, -3 * rate)

	def getPlayersRank(self, playerlist):
		rank = [ [],[],[],[],[],[] ]
		rankP = []
		players = copy.deepcopy(playerlist)
		while len(players) > 0:
			topi = players[0]
			tops = players[0].getScore()
			for j in range(1, len(players)):
				if players[j].getScore() > tops:
					topi = players[j]
					tops = players[j].getScore()
			rankP.append(topi)
			players.remove(topi)

		nowRank = 0
		for i, p in enumerate(rankP):
			if rank[nowRank] != [] and rank[nowRank][0].getScore() != p.getScore():
				nowRank += 1
			rank[nowRank].append(p)
			p.setRank(nowRank)
		return rankP





# 建立玩家模型
class Player:

	def __init__(self, rate=0.1):
		self.hypothesis = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
		self.rate = rate
		self.score = 0
		self.group = []
		self.groupNumbers = []
		self.card = None
		self.rank = -99

	def setCard(self, card):
		self.card = card
		self.group = []
		self.groupNumbers = []
		self.score = 0

	def setRank(self, rank):
		self.rank = rank

	def getRank(self):
		return self.rank

	def getCard(self):
		if not self.card:
			return None
		else:
			return self.card

	def getHypothesis(self):
		return self.hypothesis

	def setHypothesis(self, hypothesis):
		self.hypothesis = hypothesis

	def getRate(self):
		return self.rate

	def setGroup(self, group):
		features, groupNumbers = self.getFeatures(group)
		self.group = group
		self.setGroupNumbers(groupNumbers)

	def selectGroup(self):
		groups = self.getGroups()
		bestGroup = groups[0]
		features, groupNumbers = self.getFeatures(bestGroup)
		bestValue = self.getValue(features)
		self.setGroupNumbers(groupNumbers)

		for g in groups:
			features, groupNumbers = self.getFeatures(g)
			value = self.getValue(features)
			if value > bestValue:
				bestGroup = g
				bestValue = value
				self.setGroupNumbers(groupNumbers)
		self.group = bestGroup
		return bestGroup

	def getGroup(self):
		return self.group

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

	def addScore(self, score):
		self.score += score

	def setGroupNumbers(self, groupNumbers):
		self.groupNumbers = groupNumbers

	def getGroupNumbers(self):
		return self.groupNumbers

	# 当前手牌的所有可能性
	def getGroups(self):
		groups = []
		card = copy.deepcopy(self.getCard())
		for i in range(0, 120):
			groups.append([])
		for i in range(0,6):
			num1 = card[i]
			for j in range(0,5):
				card2 = copy.deepcopy(card)
				card2.remove(num1)
				num2 = card2[j]
				for k in range(0,4):
					card3 = copy.deepcopy(card2)
					card3.remove(num2)
					num3 = card3[k]
					card3.remove(num3)
					currentIndex = i*20+j*4+k
					groups[currentIndex].append(num1)
					groups[currentIndex].append(num2)
					groups[currentIndex].append(num3)
					for c in card3:
						groups[currentIndex].append(c)
		return groups

	def getFeatures(self, group):
		features = [1,0,0,0,0,0,0,0,0,0,0]
		groupNumbers = []
		groupTypes = []
		for g in group:
			groupNumbers.append(g.values()[0])
			groupTypes.append(g.keys()[0])

		# if groupNumbers[0] > 7:
		# 	features[1] = 1
		# else:
		# 	features[1] = 0
		features[1] = ( groupNumbers[0] - 7 ) / 7.0

		if groupNumbers[0] == 13:
			features[8] = 1

		if groupNumbers[1] > 10:
			groupNumbers[1] = 0.5
		if groupNumbers[2] > 10:
			groupNumbers[2] = 0.5
		step2Number = groupNumbers[1] + groupNumbers[2]

		if step2Number > 10.5:
			features[10] = 1
		else:
			features[2] = ( step2Number - 6 ) / 5.0

		if step2Number == 10.5:
			features[9] = 1

		sameNumberCount = 0
		if groupNumbers[3] == groupNumbers[4]:
			sameNumberCount += 1
		if groupNumbers[4] == groupNumbers[5]:
			sameNumberCount += 1
		if groupNumbers[3] == groupNumbers[5]:
			sameNumberCount += 1
		if sameNumberCount == 1:
			features[3] = 1
		elif sameNumberCount == 3:
			features[7] = 1

		if groupTypes[3] == groupTypes[4] and groupTypes[4] == groupTypes[5]:
			features[5] = 1

		card3 = sorted(groupNumbers[3:6])
		if card3[0] == card3[1] - 1 and card3[1] == card3[2] - 1 or card3 == [1,12,13]:
			features[4] = 1

		if features[4] == 1 and features[5] == 1:
			features[6] = 1

		return features, groupNumbers

	def getValue(self, features):
		value = 0
		h = self.hypothesis
		for i in range(0,8):
			value += h[i] * features[i]
		return value

	def selectRandom(self):
		groups = self.getGroups()
		print groups
		bestGroup = groups[random.randint(0, len(groups) - 1)]
		features, groupNumbers = self.getFeatures(bestGroup)
		self.setGroupNumbers(groupNumbers)

		return bestGroup

class LMS:

	def __init__(self):
		pass

	def updateWeight(self, hypothesis, features, vTrain, vEst, rate):
		newHypothesis = []
		for index, wi in enumerate(hypothesis):
			newWi = wi + rate * (vTrain - vEst) * features[index]
			newHypothesis.append(newWi)
		return newHypothesis



# lms = LMS()
# fs = FantasySix(6)
# players = []

# for i in range(0,6):
# 	players.append(Player())

# playersScore = [0,0,0,0,0,0]
# loses = 0
# wins = 0

# for i in range(0, 200):

# 	dealCards = fs.dealCard()

# 	for index, p in enumerate(players):
# 		p.setCard(dealCards[index])
# 		# p.selectGroup()

# 	for j in range(0, 6):
# 		players[j].selectGroup()

# 	# players[1].selectGroup()

# 	fs.getResult(players)

# 	players = fs.getPlayersRank(players)

# 	for p in players:
# 		print p.getRank()
# 		print p.getScore()
# 		print p.getGroup()

# 	print '-----------'

# 	for index, p in enumerate(players):
# 		vTrain = 0
# 		if p.getRank() == 0:
# 			vTrain = 5
# 		elif p.getRank() == 1:
# 			vTrain = 0
# 		elif p.getRank() == 2:
# 			vTrain = -5
# 		elif p.getRank() == 3:
# 			vTrain = -10
# 		elif p.getRank() == 4:
# 			vTrain = -15
# 		elif p.getRank() == 5:
# 			vTrain = -20

# 		print vTrain
# 		f, n = p.getFeatures(p.getGroup())
# 		vEst = p.getValue(f)
# 		newHypothesis = lms.updateWeight(p.getHypothesis(), f, vTrain, vEst, p.getRate())
# 		p.setHypothesis(newHypothesis)

# 	for i, p in enumerate(players):
# 		playersScore[i] += p.getScore()

# 	# if players[5].getScore() <= -3:
# 	# 	print "lose"
# 	# 	loses += 1
# 	# else:
# 	# 	print "win"
# 	# 	wins += 1


# 	fs.resetCards()

# for p in players:
# 	print p.getHypothesis()

# print players[0].getFeatures([{'C': 13}, {'B': 10}, {'C': 11}, {'B': 12}, {'C': 3}, {'A': 11}])

# print playersScore
# print 'lose: ' + str(loses) + ' win: ' + str(wins)
# p1 = Player()
# p2 = Player()
# p3 = Player()
# p1.setCard([{'B': 10}, {'C': 6}, {'D': 10}, {'D': 13}, {'B': 3}, {'C': 13}])
# p2.setCard([{'B': 10}, {'A': 8}, {'B': 11}, {'A': 5}, {'D': 12}, {'B': 5}])
# p3.setCard([{'D': 3}, {'D': 6}, {'D': 8}, {'C': 1}, {'C': 2}, {'B': 4}])
# p1.selectGroup()
# print p1.getGroup()
# p2.selectGroup()
# print p2.getGroup()
# p3.selectGroup()
# print p3.getGroup()

# fs.getResult([p1, p2, p3])



# features = p1.getFeatures([{'C': 8}, {'B': 13}, {'C': 7}, {'A': 11}, {'A': 11}, {'A': 11}])
# print features
# print p1.getValue(features)

# print p1.card
# print p1.getGroups()
# print p1.getGroups()[0]
# print p1.getGroups()[0][0].values()
# print p1.getGroups()[0][0].keys()[0]

# l = [1,2,3,4,6,5]
# a = [5,2,1,9,6] 
# print sorted(l[3:6])

# c = [11,12,13]
# if c[0] == c[1] - 1 and c[1] == c[2] - 1 or c[0] == 1:
# 	print True

# testmax = [1,2,3,4,4]
# max = max(testmax)
# max_list = []
# for index, t in enumerate(testmax):
# 	if t == max:
# 		max_list.append(index)
# print max_list

# list1 = [1,2,3]
# list2 = [2,3,4]
# print cmp(list1, list1)
# print cmp([1,11,11], [3,3,6])

# print cmp([2,5,11], [3,8,9])

