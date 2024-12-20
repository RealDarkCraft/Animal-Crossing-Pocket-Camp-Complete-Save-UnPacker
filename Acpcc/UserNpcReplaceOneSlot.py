# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserNpcReplaceOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserNpcReplaceOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserNpcReplaceOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserNpcReplaceOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserNpcReplaceOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserNpcReplaceOneSlot
    def NpcLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserNpcReplaceOneSlot
    def NpcActualArea(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserNpcReplaceOneSlot
    def UiIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserNpcReplaceOneSlot
    def IsGuestLock(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserNpcReplaceOneSlotStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserNpcReplaceOneSlotStart(builder)

def UserNpcReplaceOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserNpcReplaceOneSlotAddId(builder, id)

def UserNpcReplaceOneSlotAddNpcLabel(builder, npcLabel):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(npcLabel), 0)

def AddNpcLabel(builder, npcLabel):
    UserNpcReplaceOneSlotAddNpcLabel(builder, npcLabel)

def UserNpcReplaceOneSlotAddNpcActualArea(builder, npcActualArea):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(npcActualArea), 0)

def AddNpcActualArea(builder, npcActualArea):
    UserNpcReplaceOneSlotAddNpcActualArea(builder, npcActualArea)

def UserNpcReplaceOneSlotAddUiIndex(builder, uiIndex):
    builder.PrependUint8Slot(3, uiIndex, 0)

def AddUiIndex(builder, uiIndex):
    UserNpcReplaceOneSlotAddUiIndex(builder, uiIndex)

def UserNpcReplaceOneSlotAddIsGuestLock(builder, isGuestLock):
    builder.PrependBoolSlot(4, isGuestLock, 0)

def AddIsGuestLock(builder, isGuestLock):
    UserNpcReplaceOneSlotAddIsGuestLock(builder, isGuestLock)

def UserNpcReplaceOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserNpcReplaceOneSlotEnd(builder)