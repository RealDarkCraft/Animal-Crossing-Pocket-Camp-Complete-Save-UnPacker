# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserAtomosphereLoveLevelCap(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserAtomosphereLoveLevelCap()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserAtomosphereLoveLevelCap(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserAtomosphereLoveLevelCap
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserAtomosphereLoveLevelCap
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAtomosphereLoveLevelCap
    def Atomosphere(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserAtomosphereLoveLevelCap
    def LoveLevelCap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserAtomosphereLoveLevelCapStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserAtomosphereLoveLevelCapStart(builder)

def UserAtomosphereLoveLevelCapAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserAtomosphereLoveLevelCapAddId(builder, id)

def UserAtomosphereLoveLevelCapAddAtomosphere(builder, atomosphere):
    builder.PrependInt32Slot(1, atomosphere, 0)

def AddAtomosphere(builder, atomosphere):
    UserAtomosphereLoveLevelCapAddAtomosphere(builder, atomosphere)

def UserAtomosphereLoveLevelCapAddLoveLevelCap(builder, loveLevelCap):
    builder.PrependInt32Slot(2, loveLevelCap, 0)

def AddLoveLevelCap(builder, loveLevelCap):
    UserAtomosphereLoveLevelCapAddLoveLevelCap(builder, loveLevelCap)

def UserAtomosphereLoveLevelCapEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserAtomosphereLoveLevelCapEnd(builder)
