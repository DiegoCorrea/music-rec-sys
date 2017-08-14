from math import sqrt
import os
from euclidean import euclideanDistance

# A partir de um usuario base
# Pega o valor da similaridade desse usuario com todos os outros
def getSimilarity(evaluationTable, userBase, limit=30):
    similarity = [(euclideanDistance(evaluationTable, userBase, userCompare), userCompare)
                    for userCompare in evaluationTable if userCompare != userBase]

    similarity.sort()
    similarity.reverse()

    return similarity[0:limit]

def getUserRecommendations(evaluationTable, userBase, limit=30):
    totais = {}
    similaritySum = {}

    for userCompare in evaluationTable:
        if userCompare == userBase: continue

        similarity = euclideanDistance(evaluationTable, userBase, userCompare)

        if similarity <= 0: continue

        for item in evaluationTable[userCompare]:
            if item not in evaluationTable[userBase]:
                totais.setdefault(item, 0)
                totais[item] += evaluationTable[userCompare][item] * similarity
                similaritySum.setdefault(item, 0)
                similaritySum[item] += similarity

    rankings = [(total/similaritySum[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()

    return rankings[0:limit]

def makeSimilarityTable(evaluationTable):
    similarityTable = {}

    for item in evaluationTable:
        scores = getSimilarity(evaluationTable, item)
        similarityTable[item] = scores

    return similarityTable

def getItemRecommendations(evaluationTable, itensSimilarity, userBase, limit=30):
    userItens = evaluationTable[userBase]
    scores = {}
    totalSimilarity = {}

    for (item, score) in userItens.items():
        for(similarity, unassistedItem) in itensSimilarity[item]:
            if unassistedItem in userItens: continue

            scores.setdefault(unassistedItem, 0)
            scores[unassistedItem] += similarity * score
            totalSimilarity.setdefault(unassistedItem, 0)
            totalSimilarity[unassistedItem] += similarity

    rankings = [(score/totalSimilarity[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()

    return rankings[0:limit]

def loadBigBase():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(fileDir, 'data')

    itens = {}
    for line in open(path + '/bigSongEntry.seed'):
        (song_id, title) = line.split(',')[0:2]
        itens[song_id] = title

    userBase = {}
    for line in open(path + '/bigUserEntry.seed'):
        (user_id, song_id, play_count) = line.split('\t')
        userBase.setdefault(user_id, {})
        userBase[user_id][itens[song_id]] = int(play_count)

    return userBase

def loadSmallBase():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(fileDir, 'data')

    itens = {}
    for line in open(path + '/smallSongEntry.seed'):
        (song_id, title) = line.split(',')[0:2]
        itens[song_id] = title

    userBase = {}
    for line in open(path + '/smallUserEntry.seed'):
        (user_id, song_id, play_count) = line.split('\t')
        userBase.setdefault(user_id, {})
        userBase[user_id][itens[song_id]] = int(play_count)

    return userBase

def makeItemEvaluationBase(evaluationTable):
    evaluationTableTransposed = {}

    for user in evaluationTable:
        for item in evaluationTable[user]:
            evaluationTableTransposed.setdefault(item, {})
            evaluationTableTransposed[item].setdefault(user, evaluationTable[user][item])

    return evaluationTableTransposed
