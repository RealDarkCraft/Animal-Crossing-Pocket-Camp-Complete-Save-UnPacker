# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMembershipSeenContentSet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMembershipSeenContentSet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMembershipSeenContentSet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMembershipSeenContentSet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMembershipSeenContentSet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMembershipSeenContentSet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserMembershipSeenContentSetElement import UserMembershipSeenContentSetElement
            obj = UserMembershipSeenContentSetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserMembershipSeenContentSet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserMembershipSeenContentSet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UserMembershipSeenContentSetStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserMembershipSeenContentSetStart(builder)

def UserMembershipSeenContentSetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserMembershipSeenContentSetAddId(builder, id)

def UserMembershipSeenContentSetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserMembershipSeenContentSetAddElements(builder, elements)

def UserMembershipSeenContentSetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserMembershipSeenContentSetStartElementsVector(builder, numElems)

def UserMembershipSeenContentSetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMembershipSeenContentSetEnd(builder)