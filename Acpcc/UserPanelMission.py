# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserPanelMission(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserPanelMission()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserPanelMission(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserPanelMission
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserPanelMission
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserPanelMission
    def PanelSet(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserPanelMission
    def IsNew(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserPanelMission
    def IsSeen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserPanelMission
    def PausePageFeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserPanelMission
    def ImageLogList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # UserPanelMission
    def ImageLogListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserPanelMission
    def ImageLogListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def UserPanelMissionStart(builder):
    builder.StartObject(6)

def Start(builder):
    UserPanelMissionStart(builder)

def UserPanelMissionAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserPanelMissionAddId(builder, id)

def UserPanelMissionAddPanelSet(builder, panelSet):
    builder.PrependUint32Slot(1, panelSet, 0)

def AddPanelSet(builder, panelSet):
    UserPanelMissionAddPanelSet(builder, panelSet)

def UserPanelMissionAddIsNew(builder, isNew):
    builder.PrependBoolSlot(2, isNew, 0)

def AddIsNew(builder, isNew):
    UserPanelMissionAddIsNew(builder, isNew)

def UserPanelMissionAddIsSeen(builder, isSeen):
    builder.PrependBoolSlot(3, isSeen, 0)

def AddIsSeen(builder, isSeen):
    UserPanelMissionAddIsSeen(builder, isSeen)

def UserPanelMissionAddPausePageFeed(builder, pausePageFeed):
    builder.PrependBoolSlot(4, pausePageFeed, 0)

def AddPausePageFeed(builder, pausePageFeed):
    UserPanelMissionAddPausePageFeed(builder, pausePageFeed)

def UserPanelMissionAddImageLogList(builder, imageLogList):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(imageLogList), 0)

def AddImageLogList(builder, imageLogList):
    UserPanelMissionAddImageLogList(builder, imageLogList)

def UserPanelMissionStartImageLogListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartImageLogListVector(builder, numElems):
    return UserPanelMissionStartImageLogListVector(builder, numElems)

def UserPanelMissionEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserPanelMissionEnd(builder)