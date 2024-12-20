# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserBonusStage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserBonusStage()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserBonusStage(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserBonusStage
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserBonusStage
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserBonusStage
    def MyResourceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserBonusStage
    def MyResourceState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserBonusStage
    def MyResourceUnlocked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserBonusStageStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserBonusStageStart(builder)

def UserBonusStageAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserBonusStageAddId(builder, id)

def UserBonusStageAddMyResourceId(builder, myResourceId):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(myResourceId), 0)

def AddMyResourceId(builder, myResourceId):
    UserBonusStageAddMyResourceId(builder, myResourceId)

def UserBonusStageAddMyResourceState(builder, myResourceState):
    builder.PrependInt32Slot(2, myResourceState, 0)

def AddMyResourceState(builder, myResourceState):
    UserBonusStageAddMyResourceState(builder, myResourceState)

def UserBonusStageAddMyResourceUnlocked(builder, myResourceUnlocked):
    builder.PrependBoolSlot(3, myResourceUnlocked, 0)

def AddMyResourceUnlocked(builder, myResourceUnlocked):
    UserBonusStageAddMyResourceUnlocked(builder, myResourceUnlocked)

def UserBonusStageEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserBonusStageEnd(builder)