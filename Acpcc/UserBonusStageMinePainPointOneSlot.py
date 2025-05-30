# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserBonusStageMinePainPointOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserBonusStageMinePainPointOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserBonusStageMinePainPointOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserBonusStageMinePainPointOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserBonusStageMinePainPointOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserBonusStageMinePainPointOneSlot
    def MineId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserBonusStageMinePainPointOneSlot
    def PainPointCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserBonusStageMinePainPointOneSlotStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserBonusStageMinePainPointOneSlotStart(builder)

def UserBonusStageMinePainPointOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserBonusStageMinePainPointOneSlotAddId(builder, id)

def UserBonusStageMinePainPointOneSlotAddMineId(builder, mineId):
    builder.PrependInt32Slot(1, mineId, 0)

def AddMineId(builder, mineId):
    UserBonusStageMinePainPointOneSlotAddMineId(builder, mineId)

def UserBonusStageMinePainPointOneSlotAddPainPointCount(builder, painPointCount):
    builder.PrependInt32Slot(2, painPointCount, 0)

def AddPainPointCount(builder, painPointCount):
    UserBonusStageMinePainPointOneSlotAddPainPointCount(builder, painPointCount)

def UserBonusStageMinePainPointOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserBonusStageMinePainPointOneSlotEnd(builder)
