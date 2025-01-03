# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserBazaar(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserBazaar()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserBazaar(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserBazaar
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserBazaar
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserBazaar
    def SoldoutStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserBazaar
    def SoldoutCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserBazaarStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserBazaarStart(builder)

def UserBazaarAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserBazaarAddId(builder, id)

def UserBazaarAddSoldoutStatus(builder, soldoutStatus):
    builder.PrependInt32Slot(1, soldoutStatus, 0)

def AddSoldoutStatus(builder, soldoutStatus):
    UserBazaarAddSoldoutStatus(builder, soldoutStatus)

def UserBazaarAddSoldoutCount(builder, soldoutCount):
    builder.PrependInt32Slot(2, soldoutCount, 0)

def AddSoldoutCount(builder, soldoutCount):
    UserBazaarAddSoldoutCount(builder, soldoutCount)

def UserBazaarEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserBazaarEnd(builder)
