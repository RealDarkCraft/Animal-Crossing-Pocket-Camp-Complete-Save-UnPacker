# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserItemFortuneCookieSet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserItemFortuneCookieSet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserItemFortuneCookieSet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserItemFortuneCookieSet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserItemFortuneCookieSet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserItemFortuneCookieSet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserItemFortuneCookieSetElement import UserItemFortuneCookieSetElement
            obj = UserItemFortuneCookieSetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserItemFortuneCookieSet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserItemFortuneCookieSet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UserItemFortuneCookieSetStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserItemFortuneCookieSetStart(builder)

def UserItemFortuneCookieSetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserItemFortuneCookieSetAddId(builder, id)

def UserItemFortuneCookieSetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserItemFortuneCookieSetAddElements(builder, elements)

def UserItemFortuneCookieSetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserItemFortuneCookieSetStartElementsVector(builder, numElems)

def UserItemFortuneCookieSetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserItemFortuneCookieSetEnd(builder)