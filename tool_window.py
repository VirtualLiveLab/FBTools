# *- coding: utf-8 -*-
from pyfbsdk import*
from pyfbsdk_additions import*
from mbtools import*
from snap_tracker import setMarkerSet

##############################################
### ここ変えてね
##############################################
bodyTrackerName = "BodyTracker"
# オフセット
offset_x = 0
offset_y = -30
offset_z = -20

##############################################
### 実装
##############################################


def addTargetUI():
    editUI.Text = "RecordTarget"
    x = FBAddRegionParam(50, FBAttachType.kFBAttachNone, "")
    y = FBAddRegionParam(20, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(100,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(30,FBAttachType.kFBAttachNone,"")
    
    window.AddRegion("TargetUI","TargetUI", x, y, w, h)
    window.SetControl("TargetUI",editUI)
    return editUI


def onCreateActorBtnClick(control,event):

    actor = createActor()

    model = getTargetModel(editUI.Text)
    tracker = find(model, bodyTrackerName)

    # Actorのポジションを移動
    pos = FBVector3d()
    tracker.GetVector(pos)
    pos += FBVector3d(offset_x, offset_y, offset_z)
    # scale = FBVector3d(0.1, 0.1, 0.1)
    # actor.SetDefinitionScaleVector(FBSkeletonNodeId.kFBSkeletonHipsIndex, scale)
    actor.SetActorTranslation(pos) 
    FBMessageBox("Create Actor",control.Caption,"OK")
 

def onMarkerSetBtnClick(control,event):
    app = FBApplication()
    if not app.CurrentActor is None:
        name = app.CurrentActor.Name
        isSet = setMarkerSet(editUI.Text, name)
        if isSet:
            FBMessageBox("Create MarkerSet",control.Caption,"OK")


#####################
### Actor
#####################

def addActorUI():
    x = FBAddRegionParam(50, FBAttachType.kFBAttachNone, "")
    y = FBAddRegionParam(60, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(100,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(30,FBAttachType.kFBAttachNone,"")
    window.AddRegion("BtnLyt1","BtnLyt1", x, y, w, h)
    caBtn=FBButton()
    caBtn.Caption="Create Actor"
    window.SetControl("BtnLyt1",caBtn)
    caBtn.OnClick.Add(onCreateActorBtnClick)
#####################
### MarkerSet
#####################
def addMarkerSetUI():
    x = FBAddRegionParam(50, FBAttachType.kFBAttachNone, "")
    y = FBAddRegionParam(100, FBAttachType.kFBAttachNone, "")
    w = FBAddRegionParam(100,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(30,FBAttachType.kFBAttachNone,"")
    window.AddRegion("BtnLyt2","BtnLyt2", x, y, w, h)
    msBtn=FBButton()
    msBtn.Caption="Create MarkerSet"
    window.SetControl("BtnLyt2",msBtn)
    # イベントの設定
    msBtn.OnClick.Add(onMarkerSetBtnClick)


editUI = FBEdit()
window=FBCreateUniqueTool("Tool Window")
addTargetUI()
addActorUI()
addMarkerSetUI()
# ウィンドウサイズの指定
window.StartSizeX = 200
window.StartSizeY = 200

ShowTool(window)
