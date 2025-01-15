# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserActivityListedInfoOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserActivityListedInfoOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserActivityListedInfoOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserActivityListedInfoOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserActivityListedInfoOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserActivityListedInfoOneSlot
    def KeyName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserActivityListedInfoOneSlot
    def OtherPlayerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserActivityListedInfoOneSlot
    def CreateAtTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserActivityListedInfoOneSlot
    def OtherPositionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityListedInfoOneSlot
    def OtherActionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityListedInfoOneSlot
    def NpcPositionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityListedInfoOneSlot
    def NpcActionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserActivityListedInfoOneSlotStart(builder):
    builder.StartObject(8)

def Start(builder):
    UserActivityListedInfoOneSlotStart(builder)

def UserActivityListedInfoOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserActivityListedInfoOneSlotAddId(builder, id)

def UserActivityListedInfoOneSlotAddKeyName(builder, keyName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(keyName), 0)

def AddKeyName(builder, keyName):
    UserActivityListedInfoOneSlotAddKeyName(builder, keyName)

def UserActivityListedInfoOneSlotAddOtherPlayerId(builder, otherPlayerId):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(otherPlayerId), 0)

def AddOtherPlayerId(builder, otherPlayerId):
    UserActivityListedInfoOneSlotAddOtherPlayerId(builder, otherPlayerId)

def UserActivityListedInfoOneSlotAddCreateAtTime(builder, createAtTime):
    builder.PrependInt64Slot(3, createAtTime, 0)

def AddCreateAtTime(builder, createAtTime):
    UserActivityListedInfoOneSlotAddCreateAtTime(builder, createAtTime)

def UserActivityListedInfoOneSlotAddOtherPositionId(builder, otherPositionId):
    builder.PrependInt32Slot(4, otherPositionId, 0)

def AddOtherPositionId(builder, otherPositionId):
    UserActivityListedInfoOneSlotAddOtherPositionId(builder, otherPositionId)

def UserActivityListedInfoOneSlotAddOtherActionId(builder, otherActionId):
    builder.PrependInt32Slot(5, otherActionId, 0)

def AddOtherActionId(builder, otherActionId):
    UserActivityListedInfoOneSlotAddOtherActionId(builder, otherActionId)

def UserActivityListedInfoOneSlotAddNpcPositionId(builder, npcPositionId):
    builder.PrependInt32Slot(6, npcPositionId, 0)

def AddNpcPositionId(builder, npcPositionId):
    UserActivityListedInfoOneSlotAddNpcPositionId(builder, npcPositionId)

def UserActivityListedInfoOneSlotAddNpcActionId(builder, npcActionId):
    builder.PrependInt32Slot(7, npcActionId, 0)

def AddNpcActionId(builder, npcActionId):
    UserActivityListedInfoOneSlotAddNpcActionId(builder, npcActionId)

def UserActivityListedInfoOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserActivityListedInfoOneSlotEnd(builder)
