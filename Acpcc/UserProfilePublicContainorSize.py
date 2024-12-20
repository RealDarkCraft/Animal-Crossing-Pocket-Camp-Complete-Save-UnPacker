# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserProfilePublicContainorSize(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserProfilePublicContainorSize()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserProfilePublicContainorSize(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserProfilePublicContainorSize
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserProfilePublicContainorSize
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserProfilePublicContainorSize
    def PurchaseCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserProfilePublicContainorSize
    def CurrentSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserProfilePublicContainorSizeStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserProfilePublicContainorSizeStart(builder)

def UserProfilePublicContainorSizeAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserProfilePublicContainorSizeAddId(builder, id)

def UserProfilePublicContainorSizeAddPurchaseCount(builder, purchaseCount):
    builder.PrependInt32Slot(1, purchaseCount, 0)

def AddPurchaseCount(builder, purchaseCount):
    UserProfilePublicContainorSizeAddPurchaseCount(builder, purchaseCount)

def UserProfilePublicContainorSizeAddCurrentSize(builder, currentSize):
    builder.PrependInt32Slot(2, currentSize, 0)

def AddCurrentSize(builder, currentSize):
    UserProfilePublicContainorSizeAddCurrentSize(builder, currentSize)

def UserProfilePublicContainorSizeEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserProfilePublicContainorSizeEnd(builder)