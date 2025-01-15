# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserQuestPainPointOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserQuestPainPointOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserQuestPainPointOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserQuestPainPointOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserQuestPainPointOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserQuestPainPointOneSlot
    def RewardBoxId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserQuestPainPointOneSlot
    def Point(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserQuestPainPointOneSlotStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserQuestPainPointOneSlotStart(builder)

def UserQuestPainPointOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserQuestPainPointOneSlotAddId(builder, id)

def UserQuestPainPointOneSlotAddRewardBoxId(builder, rewardBoxId):
    builder.PrependInt32Slot(1, rewardBoxId, 0)

def AddRewardBoxId(builder, rewardBoxId):
    UserQuestPainPointOneSlotAddRewardBoxId(builder, rewardBoxId)

def UserQuestPainPointOneSlotAddPoint(builder, point):
    builder.PrependInt32Slot(2, point, 0)

def AddPoint(builder, point):
    UserQuestPainPointOneSlotAddPoint(builder, point)

def UserQuestPainPointOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserQuestPainPointOneSlotEnd(builder)
