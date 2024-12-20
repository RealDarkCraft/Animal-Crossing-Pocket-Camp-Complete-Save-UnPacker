# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventConversationEventOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventConversationEventOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventConversationEventOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventConversationEventOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventConversationEventOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventConversationEventOneSlot
    def NpcConversationEventCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventConversationEventOneSlot
    def PainPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventConversationEventOneSlot
    def AreaLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def UserTapEventConversationEventOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserTapEventConversationEventOneSlotStart(builder)

def UserTapEventConversationEventOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserTapEventConversationEventOneSlotAddId(builder, id)

def UserTapEventConversationEventOneSlotAddNpcConversationEventCount(builder, npcConversationEventCount):
    builder.PrependInt32Slot(1, npcConversationEventCount, 0)

def AddNpcConversationEventCount(builder, npcConversationEventCount):
    UserTapEventConversationEventOneSlotAddNpcConversationEventCount(builder, npcConversationEventCount)

def UserTapEventConversationEventOneSlotAddPainPoint(builder, painPoint):
    builder.PrependInt32Slot(2, painPoint, 0)

def AddPainPoint(builder, painPoint):
    UserTapEventConversationEventOneSlotAddPainPoint(builder, painPoint)

def UserTapEventConversationEventOneSlotAddAreaLabel(builder, areaLabel):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(areaLabel), 0)

def AddAreaLabel(builder, areaLabel):
    UserTapEventConversationEventOneSlotAddAreaLabel(builder, areaLabel)

def UserTapEventConversationEventOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventConversationEventOneSlotEnd(builder)
