##############################################
### module import
##############################################
from pyfbsdk import*
from mbtools import*

def setMarkerSet(TargetName : str, ActorName : str):
    
    ##############################################
    ### 実装
    ##############################################
    markerList = [ 
        [FBSkeletonNodeId.kFBSkeletonHeadIndex, "headTracker"], # 頭
        [FBSkeletonNodeId.kFBSkeletonChestIndex, "BodyTracker"], #胸
        [FBSkeletonNodeId.kFBSkeletonLeftElbowIndex, "LeftHandTracker"], #左手首
        [FBSkeletonNodeId.kFBSkeletonRightElbowIndex, "RightHandTracker"], #右手首
        [FBSkeletonNodeId.kFBSkeletonLeftShoulderIndex, "LeftElbowTracker"], #左肘
        [FBSkeletonNodeId.kFBSkeletonRightShoulderIndex, "RightElbowTracker"], #右肘
        [FBSkeletonNodeId.kFBSkeletonLeftKneeIndex, "LeftFootTracker"], #左足
        [FBSkeletonNodeId.kFBSkeletonRightKneeIndex, "RightFootTracker"], #右足
        [FBSkeletonNodeId.kFBSkeletonRightHipIndex, "RightKneeTracker"], #右膝
        [FBSkeletonNodeId.kFBSkeletonLeftHipIndex, "LeftKneeTracker"], #左膝
    ]
    
    # 複製したトラッカー
    markerList2 = [ 
        [FBSkeletonNodeId.kFBSkeletonHipsIndex, "HipTracker"], #胸   
        [FBSkeletonNodeId.kFBSkeletonLeftCollarIndex, "LeftShoulderTracker"], #左肩
        [FBSkeletonNodeId.kFBSkeletonRightCollarIndex, "RightShoulderTracker"] #右肩
    ]

    if not containActor(ActorName):
        return False
    
    model = getTargetModel(target=TargetName)
    actor = getActor(ActorName)
    markerSet = createMarkerSet()
    
    # Actorにマーカーセットを登録
    actor.MarkerSet = markerSet
    
    for m in markerList:
        nodeId = m[0]
        name = m[1]
        tracker = find(model, name)
    
        if tracker.Name == "BodyTracker":
            for m2 in markerList2:
                t2 = find(tracker, m2[1])
                AddTracker(markerSet, t2, m2[0])
    
    
        AddTracker(markerSet, tracker, nodeId)
    
    
    return True
    # Snap
    
    #actor.Snap(FBRecalcMarkerSetOffset.kFBRecalcMarkerSetOffsetTR)
