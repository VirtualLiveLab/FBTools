from pickle import TRUE
from pyfbsdk import*



def getTargetModel(target):
    result = []
    for i in FBSystem().Scene.RootModel.Children:
        if i.Name == target:
            result.append(i)

    return result[0]

def containActor(name:str) ->FBActor:
    for actor in FBSystem().Scene.Actors:
        if actor.Name == name:
            return True

    return False
def getActor(name:str) -> FBActor:
    result = []
    for actor in FBSystem().Scene.Actors:
        if actor.Name == name:
            result.append(actor)

    return result[0]

def createActor() -> FBActor:
    actorName = "NewActor"
    actor = FBActor(actorName)
    return actor

def createMarkerSet() -> FBMarkerSet:
    markerSetName = "NewMarkerSet"
    markerSet = FBMarkerSet(markerSetName) 
    return markerSet

# マーカセットに追加する
def AddTracker(markerSet : FBMarkerSet, tracker : FBModel, nodeId : FBSkeletonNodeId):
    trackers = [tracker]
    for child in tracker.Children:
        if child.Name.startswith("Marker1") or child.Name.startswith("Marker2") or child.Name.startswith("Marker3"):
            trackers.append(child)
    for t in trackers:
        markerSet.SetReferenceModel(t)
        markerSet.AddMarker(nodeId, t, False)


# Modelの子オブジェクトにあるオブジェクトを返す
def find(model : FBModel, name : str):
    names = [ i.Name for i in model.Children]
    index = names.index(name)
    tracker = model.Children[index]
    return tracker
