# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ExtDiaryEntryOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ExtDiaryEntryOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsExtDiaryEntryOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ExtDiaryEntryOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ExtDiaryEntryOneSlot
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ExtDiaryEntryOneSlot
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # ExtDiaryEntryOneSlot
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # ExtDiaryEntryOneSlot
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ExtDiaryEntryOneSlot
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def ExtDiaryEntryOneSlotStart(builder):
    builder.StartObject(2)

def Start(builder):
    ExtDiaryEntryOneSlotStart(builder)

def ExtDiaryEntryOneSlotAddTimestamp(builder, timestamp):
    builder.PrependInt64Slot(0, timestamp, 0)

def AddTimestamp(builder, timestamp):
    ExtDiaryEntryOneSlotAddTimestamp(builder, timestamp)

def ExtDiaryEntryOneSlotAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)

def AddValue(builder, value):
    ExtDiaryEntryOneSlotAddValue(builder, value)

def ExtDiaryEntryOneSlotStartValueVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartValueVector(builder, numElems):
    return ExtDiaryEntryOneSlotStartValueVector(builder, numElems)

def ExtDiaryEntryOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return ExtDiaryEntryOneSlotEnd(builder)
