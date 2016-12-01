# coding: utf-8
from django.shortcuts import render
import ast

from fantesysix.utils import FantasySix, Player, LMS
from fantesysix.models import History, Hypothesis, HistoryDealCards

fs = FantasySix(6)
lms = LMS()
player = Player()
program_players = []
for i in range(0,5):
	program_players.append(Player())


# Create your views here.
def home(request):
	fs.resetCards()
	dealCards = fs.dealCard()

	# HistoryDealCards.objects.create(deal_cards=dealCards)

	player.setCard(dealCards[0])
	for i in range(1, 6):
		# print dealCards[i]
		program_players[i-1].setCard(dealCards[i])
	hy = Hypothesis.objects.all().order_by('-time')[0].hypothesis
	# print hy
	for i in range(0,5):
		program_players[i].setHypothesis(ast.literal_eval(hy))
	dealCard = fs.renderCards(dealCards[0])
	program_cards = []
	for i in range(1, 6):
		program_cards.append([fs.renderCards(dealCards[i])])
	return render(request, 'fantesysix_home.html', {'dealCard': dealCard , 'program_cards': program_cards})

def judge(request):
	selected_cards = request.POST.getlist('selectedCards[]')
	# print selected_cards[0]
	l = []
	for sc in selected_cards:
		sc = ast.literal_eval(sc)
		l.append(sc)


	player.setGroup(l)
	# print player.getGroup()

	for i in range(0, 5):
		program_players[i].selectGroup()
		# print program_players[i].getGroup()

	# program_players.append(player)
	fs.getResult([program_players[0], program_players[1], program_players[2], program_players[3], program_players[4], player])
	
	player_cards = fs.renderCards(player.getGroup())
	player_score = player.getScore()
	program_cards = []
	program_scores = []

	for i in range(0,5):
		program_cards.append([ fs.renderCards(program_players[i].getGroup()), program_players[i].getScore()])
		program_scores.append(program_players[i].getScore())

	all_players = fs.getPlayersRank([program_players[0], program_players[1], program_players[2], program_players[3], program_players[4], player])
	
	newHypothesis = program_players[0].getHypothesis()

	for p in program_players:
		program_score = p.getScore()
		vTrain = 0
		if program_score == 0:
			vTrain = 10
		elif program_score >= -2:
			vTrain = 5
		elif program_score == -3:
			vTrain = -5
		else:
			vTrain = -10
		print p.getGroup()
		f, n = p.getFeatures(p.getGroup())
		vEst = p.getValue(f)
		newHypothesis = lms.updateWeight(newHypothesis, f, vTrain, vEst, p.getRate())
		p.setHypothesis(newHypothesis)
	

	History.objects.create(guest_card=player_cards, own_card=program_cards, guest_score=player_score, own_score=program_scores)

	Hypothesis.objects.create(hypothesis=newHypothesis)

	return render(request, 'fantesysix_home.html', {'dealCard': player_cards, 'program_cards': program_cards, 'player_score': player_score, 'program_scores': program_scores})