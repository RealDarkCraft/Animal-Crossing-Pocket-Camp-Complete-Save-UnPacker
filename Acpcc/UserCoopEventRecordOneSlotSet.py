# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCoopEventRecordOneSlotSet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCoopEventRecordOneSlotSet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCoopEventRecordOneSlotSet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCoopEventRecordOneSlotSet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCoopEventRecordOneSlotSet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCoopEventRecordOneSlotSet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserCoopEventRecordOneSlotSetElement import UserCoopEventRecordOneSlotSetElement
            obj = UserCoopEventRecordOneSlotSetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCoopEventRecordOneSlotSet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserCoopEventRecordOneSlotSet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UserCoopEventRecordOneSlotSetStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserCoopEventRecordOneSlotSetStart(builder)

def UserCoopEventRecordOneSlotSetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserCoopEventRecordOneSlotSetAddId(builder, id)

def UserCoopEventRecordOneSlotSetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserCoopEventRecordOneSlotSetAddElements(builder, elements)

def UserCoopEventRecordOneSlotSetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserCoopEventRecordOneSlotSetStartElementsVector(builder, numElems)

def UserCoopEventRecordOneSlotSetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCoopEventRecordOneSlotSetEnd(builder)
