# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMaterialDropInfoItemDropTimeOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMaterialDropInfoItemDropTimeOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMaterialDropInfoItemDropTimeOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMaterialDropInfoItemDropTimeOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMaterialDropInfoItemDropTimeOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMaterialDropInfoItemDropTimeOneSlot
    def LabelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMaterialDropInfoItemDropTimeOneSlot
    def StartTimerTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserMaterialDropInfoItemDropTimeOneSlot
    def RefreshTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserMaterialDropInfoItemDropTimeOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserMaterialDropInfoItemDropTimeOneSlotStart(builder)

def UserMaterialDropInfoItemDropTimeOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserMaterialDropInfoItemDropTimeOneSlotAddId(builder, id)

def UserMaterialDropInfoItemDropTimeOneSlotAddLabelType(builder, labelType):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(labelType), 0)

def AddLabelType(builder, labelType):
    UserMaterialDropInfoItemDropTimeOneSlotAddLabelType(builder, labelType)

def UserMaterialDropInfoItemDropTimeOneSlotAddStartTimerTime(builder, startTimerTime):
    builder.PrependInt64Slot(2, startTimerTime, 0)

def AddStartTimerTime(builder, startTimerTime):
    UserMaterialDropInfoItemDropTimeOneSlotAddStartTimerTime(builder, startTimerTime)

def UserMaterialDropInfoItemDropTimeOneSlotAddRefreshTime(builder, refreshTime):
    builder.PrependInt64Slot(3, refreshTime, 0)

def AddRefreshTime(builder, refreshTime):
    UserMaterialDropInfoItemDropTimeOneSlotAddRefreshTime(builder, refreshTime)

def UserMaterialDropInfoItemDropTimeOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMaterialDropInfoItemDropTimeOneSlotEnd(builder)