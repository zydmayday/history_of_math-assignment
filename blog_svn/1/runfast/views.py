# coding: utf-8
from django.shortcuts import render
from runfastgame import RunFast, Player
import simplejson
import datetime
import runfast.models as rm

# Create your views here.

players = {}
runfast = None

def _getGameInfo(playerName):
	'''
	获得游戏的一些信息
	return 玩家的list，自己的手牌，当前打出的牌，当前该谁走，上把谁走的
	return cp, cards, cc, cn, wpn
	'''
	global runfast
	player = runfast.getPlayer(playerName)
	cards = player.getCurrentCards()
	cp = runfast.getPlayers()
	cn = None
	wpn = None
	cc = runfast.getCurrentCard()
	currentTurn = runfast.getCurrentTurn()
	if currentTurn == -1:
		cn = ''
	else:
		cn = cp[currentTurn].getName()
	whoPlayed = runfast.getWhoPlayed()
	if whoPlayed == -1:
		wpn = ''
	else:
		wpn = cp[whoPlayed].getName()
	return cp, cards, cc, cn, wpn

def _isLegal(cards, playerName):
	'''
	走牌是否合法
	'''
	global runfast
	currentTurn = runfast.getCurrentTurn()
	player = runfast.getPlayer(playerName)
	playerCards = player.getCurrentCards()
	currentCard = runfast.getCurrentCard()
	currentType = runfast.getCurrentType()
	cardsCanPlay = []
	# 如果是第一轮走牌，必须带红桃三
	if not runfast.getCurrentCard():
		if '3A' not in cards:
			return False, cards, 'SINGLE'
	# 如果上一轮就是他走的话，那就重新走牌
	if currentTurn == runfast.getWhoPlayed():
		cardsCanPlay = player.getCardsCanPlay()
	else:
		cardsCanPlay = player.getCardsCanPlay(currentCard, currentType)

	playedCards = [playerCards.index(c) for c in cards]
	playedCards.sort()
	playedType = ''
	isLegal = False
	for type in cardsCanPlay.keys():
		for ccp in cardsCanPlay[type]:
			ccp.sort()
			if playedCards == ccp:
				isLegal = True
				playedType = type
				break
	return isLegal, cards, playedType

def _isMyTurn(playerName):
	myTurn = runfast.isPlayerTurn(playerName)
	return myTurn

def _moveToNext(playedCards, playedType, playerName):
	'''
	走牌合法的话，去掉该player的对应手牌，判断游戏是否结束，若不结束则进行到下一个状态
	'''
	global runfast
	player = runfast.getPlayer(playerName)
	player.removeCards(playedCards)

	if runfast.gameOver():
		return True
	else:
		runfast.moveToNext(playedCards, playedType)
		return False

def _passToNext():
	global runfast
	return runfast.passToNext()

def _renderGameHtml(request, playerName, cp, cards, cc, cn, wpn, msg, myTurn, isLegal):
	return render(request, 'runfast_game.html', {'playerName': playerName, 'cp': cp, 'cards': cards, 'msg':'', 'myTurn': myTurn, 'cc': cc, 'cn': cn, 'wpn': wpn, 'myTurn': myTurn, 'isLegal': isLegal})

def _isOver():
	global runfast
	return runfast.gameOver()

def _renderOverHtml(request):
	global runfast
	winner = None
	losers = []
	players = runfast.getPlayers()
	for p in players:
		cc = p.getCurrentCards()
		if cc:
			losers.append({'name': p.getName(), 'cards': cc})
		else:
			winner = p.getName()
	return render(request, 'runfast_over.html', {'cp': players, 'winner': winner, 'losers': losers})

def _save():
	global runfast
	players = runfast.getPlayers()
	name = ''
	winner = ''
	for p in players:
		if not p.getCurrentCards():
			winner = p.getName()
		name += '(' + p.getName() + ') ' 
	rf = rm.RunFast(name=name, time=datetime.datetime.now(), winner=winner)
	rf.save()

def _reset():
	global runfast
	global players
	runfast = None
	players = {}



def home(request):
	return render(request, 'runfast_home.html', {'msg': ''})

def join(request):
	global players
	if len(players.keys()) == 3:
		# TODO 最后设置成可以观战的模式
		return render(request, 'runfast_home_ajax.html', {'msg': '不好意思，人满了！'})
	playerName = request.POST['playerName']
	if playerName in players.keys():
		return render(request, 'runfast_home_ajax.html', {'msg': '不好意思，改名字已被使用！'})

	p = Player(playerName)
	players[playerName] = p
	cp = [players[p] for p in players.keys()]
	# 如果时候人齐了，就可以开始游戏了
	if len(players.keys()) == 3:
		global runfast
		runfast = RunFast(cp)
		runfast.shuffle()
		runfast.dealCards()
		for p in runfast.getPlayers():
			p.sortCards()
		runfast.setCurrentTurn(runfast.chooseWhoStart()[0])
	return render(request, 'runfast_joined.html', {'playerName': playerName, 'cp': cp, 'msg': ''})


def game(request):
	global players
	playerName = request.POST['playerName']
	msg = ''
	isLegal = False
	html = ''
	if len(players.keys()) == 3:
		# 开始游戏
		cp, cards, cc, cn, wpn = _getGameInfo(playerName)
		myTurn = _isMyTurn(playerName)
		if _isOver():
			html = _renderOverHtml()
		html = _renderGameHtml(request, playerName, cp, cards, cc, cn, wpn, msg, myTurn, isLegal)
		return html	
	else:
		cp = [players[p] for p in players.keys()]
		html = render(request, 'runfast_joined.html', {'playerName': playerName, 'cp': cp, 'msg': '等待其他玩家加入...', 'cards': []})
		return html

def play(request):
	cards = request.POST.getlist('cards[]')
	playerName = request.POST['playerName']
	isLegal, playedCards, playedType = _isLegal(cards, playerName)
	msg = ''
	html = ''
	if isLegal:
		# 如果出牌合理
		isOver = _moveToNext(playedCards, playedType, playerName)
		cp, cards, cc, cn, wpn = _getGameInfo(playerName)
		myTurn = _isMyTurn(playerName)
		if isOver:
			html = _renderOverHtml(request)
			_save()
			_reset()
		else:
			html = _renderGameHtml(request, playerName, cp, cards, cc, cn, wpn, msg, myTurn, isLegal)
	else:
		cp, cards, cc, cn, wpn = _getGameInfo(playerName)
		msg = '出牌不合法！'
		myTurn = _isMyTurn(playerName)
		html = _renderGameHtml(request, playerName, cp, cards, cc, cn, wpn, msg, myTurn, isLegal)
	return html	

def passTurn(request):
	playerName = request.POST['playerName']
	msg = ''
	myTurn = False
	isLegal = True
	passOk = _passToNext()
	if not passOk:
		myTurn = True
	cp, cards, cc, cn, wpn = _getGameInfo(playerName)
	html = _renderGameHtml(request, playerName, cp, cards, cc, cn, wpn, msg, myTurn, isLegal)
	return html

def reset(request):
	msg = request.POST['msg']
	print msg
	_reset()
	return render(request, 'runfast_home.html', {'msg': ''})
	



if __name__ == '__main__':
	players = {}