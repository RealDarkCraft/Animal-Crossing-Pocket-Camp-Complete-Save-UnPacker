# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMyDesignDBOneSlotSet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMyDesignDBOneSlotSet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMyDesignDBOneSlotSet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMyDesignDBOneSlotSet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMyDesignDBOneSlotSet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMyDesignDBOneSlotSet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserMyDesignDBOneSlotSetElement import UserMyDesignDBOneSlotSetElement
            obj = UserMyDesignDBOneSlotSetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserMyDesignDBOneSlotSet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserMyDesignDBOneSlotSet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UserMyDesignDBOneSlotSetStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserMyDesignDBOneSlotSetStart(builder)

def UserMyDesignDBOneSlotSetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserMyDesignDBOneSlotSetAddId(builder, id)

def UserMyDesignDBOneSlotSetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserMyDesignDBOneSlotSetAddElements(builder, elements)

def UserMyDesignDBOneSlotSetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserMyDesignDBOneSlotSetStartElementsVector(builder, numElems)

def UserMyDesignDBOneSlotSetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMyDesignDBOneSlotSetEnd(builder)