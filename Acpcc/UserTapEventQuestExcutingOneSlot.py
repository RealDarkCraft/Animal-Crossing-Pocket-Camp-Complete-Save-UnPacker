# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventQuestExcutingOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventQuestExcutingOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventQuestExcutingOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventQuestExcutingOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventQuestExcutingOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventQuestExcutingOneSlot
    def NpcQuestExcutingNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserTapEventQuestExcutingOneSlotStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserTapEventQuestExcutingOneSlotStart(builder)

def UserTapEventQuestExcutingOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserTapEventQuestExcutingOneSlotAddId(builder, id)

def UserTapEventQuestExcutingOneSlotAddNpcQuestExcutingNum(builder, npcQuestExcutingNum):
    builder.PrependInt32Slot(1, npcQuestExcutingNum, 0)

def AddNpcQuestExcutingNum(builder, npcQuestExcutingNum):
    UserTapEventQuestExcutingOneSlotAddNpcQuestExcutingNum(builder, npcQuestExcutingNum)

def UserTapEventQuestExcutingOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventQuestExcutingOneSlotEnd(builder)