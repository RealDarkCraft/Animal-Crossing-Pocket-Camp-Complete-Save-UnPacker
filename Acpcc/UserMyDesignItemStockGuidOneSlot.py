# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMyDesignItemStockGuidOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMyDesignItemStockGuidOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMyDesignItemStockGuidOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMyDesignItemStockGuidOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMyDesignItemStockGuidOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMyDesignItemStockGuidOneSlot
    def Guid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyDesignItemStockGuidOneSlot
    def MyDesignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def UserMyDesignItemStockGuidOneSlotStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserMyDesignItemStockGuidOneSlotStart(builder)

def UserMyDesignItemStockGuidOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserMyDesignItemStockGuidOneSlotAddId(builder, id)

def UserMyDesignItemStockGuidOneSlotAddGuid(builder, guid):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(guid), 0)

def AddGuid(builder, guid):
    UserMyDesignItemStockGuidOneSlotAddGuid(builder, guid)

def UserMyDesignItemStockGuidOneSlotAddMyDesignId(builder, myDesignId):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(myDesignId), 0)

def AddMyDesignId(builder, myDesignId):
    UserMyDesignItemStockGuidOneSlotAddMyDesignId(builder, myDesignId)

def UserMyDesignItemStockGuidOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMyDesignItemStockGuidOneSlotEnd(builder)
