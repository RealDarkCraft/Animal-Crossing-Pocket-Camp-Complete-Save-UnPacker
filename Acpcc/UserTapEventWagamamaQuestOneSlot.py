# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventWagamamaQuestOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventWagamamaQuestOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventWagamamaQuestOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventWagamamaQuestOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventWagamamaQuestOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventWagamamaQuestOneSlot
    def NpcLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserTapEventWagamamaQuestOneSlot
    def ExecutingWagamamaQuestId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserTapEventWagamamaQuestOneSlot
    def WagamamaQuestStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserTapEventWagamamaQuestOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserTapEventWagamamaQuestOneSlotStart(builder)

def UserTapEventWagamamaQuestOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserTapEventWagamamaQuestOneSlotAddId(builder, id)

def UserTapEventWagamamaQuestOneSlotAddNpcLabel(builder, npcLabel):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(npcLabel), 0)

def AddNpcLabel(builder, npcLabel):
    UserTapEventWagamamaQuestOneSlotAddNpcLabel(builder, npcLabel)

def UserTapEventWagamamaQuestOneSlotAddExecutingWagamamaQuestId(builder, executingWagamamaQuestId):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(executingWagamamaQuestId), 0)

def AddExecutingWagamamaQuestId(builder, executingWagamamaQuestId):
    UserTapEventWagamamaQuestOneSlotAddExecutingWagamamaQuestId(builder, executingWagamamaQuestId)

def UserTapEventWagamamaQuestOneSlotAddWagamamaQuestStatus(builder, wagamamaQuestStatus):
    builder.PrependUint32Slot(3, wagamamaQuestStatus, 0)

def AddWagamamaQuestStatus(builder, wagamamaQuestStatus):
    UserTapEventWagamamaQuestOneSlotAddWagamamaQuestStatus(builder, wagamamaQuestStatus)

def UserTapEventWagamamaQuestOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventWagamamaQuestOneSlotEnd(builder)
