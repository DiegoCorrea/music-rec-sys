from math import sqrt
from euclidean import euclideanDistance
import recommendation

userRatingTable = recommendation.loadSmallBase()
musicRatingTable = recommendation.makeItemEvaluationBase(userRatingTable)
tableSimilarity = recommendation.makeSimilarityTable(musicRatingTable)


userRatingMus = recommendation.loadBigBase()
musicRatingMus = recommendation.makeItemEvaluationBase(userRatingMus)
lensSimilarity = recommendation.makeSimilarityTable(musicRatingMus)

def getRecommendationSmallTable():
    print ("\n*******************************************")
    print ("\n*******Recomendando itens ao Usuario*******")
    print ("\n*******************************************")

    print ("\nPara b80344d063b5ccb3212f76538f3d9e43d87dca9e: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'b80344d063b5ccb3212f76538f3d9e43d87dca9e')))
    print ("\n###########################################\n")

    print ("\nPara bd4c6e843f00bd476847fb75c47b4fb430a06856: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'bd4c6e843f00bd476847fb75c47b4fb430a06856')))
    print ("\n###########################################\n")

    print ("\nPara baf47ed8da24d607e50d8684cde78b923538640f: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'baf47ed8da24d607e50d8684cde78b923538640f')))
    print ("\n###########################################\n")


def getMusicRecommendation():
    print ("\n*******************************************")
    print ("\n*******Recomendando itens ao Usuario*******")
    print ("\n*******************************************")

    print ("\n-> Para b80344d063b5ccb3212f76538f3d9e43d87dca9e: \n")
    for (predict_play_count, name) in recommendation.getItemRecommendations(userRatingMus, lensSimilarity, 'b80344d063b5ccb3212f76538f3d9e43d87dca9e'):
        print ("Predição de predict_play_count: ", str(predict_play_count), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para bd4c6e843f00bd476847fb75c47b4fb430a06856: \n")
    for (predict_play_count, name) in recommendation.getItemRecommendations(userRatingMus, lensSimilarity, 'bd4c6e843f00bd476847fb75c47b4fb430a06856'):
        print ("Predição de predict_play_count: ", str(predict_play_count), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para baf47ed8da24d607e50d8684cde78b923538640f: \n")
    for (predict_play_count, name) in recommendation.getItemRecommendations(userRatingMus, lensSimilarity, 'baf47ed8da24d607e50d8684cde78b923538640f'):
        print ("Predição de predict_play_count: ", str(predict_play_count), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para 8937134734f869debcab8f23d77465b4caaa85df: \n")
    for (predict_play_count, name) in recommendation.getItemRecommendations(userRatingMus, lensSimilarity, '8937134734f869debcab8f23d77465b4caaa85df'):
        print ("Predição de predict_play_count: ", str(predict_play_count), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")
