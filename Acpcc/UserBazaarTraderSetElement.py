# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserBazaarTraderSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserBazaarTraderSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserBazaarTraderSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserBazaarTraderSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserBazaarTraderSetElement
    def PlayerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserBazaarTraderSetElement
    def BuyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserBazaarTraderSetElement
    def LastBuyAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserBazaarTraderSetElementStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserBazaarTraderSetElementStart(builder)

def UserBazaarTraderSetElementAddPlayerId(builder, playerId):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(playerId), 0)

def AddPlayerId(builder, playerId):
    UserBazaarTraderSetElementAddPlayerId(builder, playerId)

def UserBazaarTraderSetElementAddBuyCount(builder, buyCount):
    builder.PrependInt32Slot(1, buyCount, 0)

def AddBuyCount(builder, buyCount):
    UserBazaarTraderSetElementAddBuyCount(builder, buyCount)

def UserBazaarTraderSetElementAddLastBuyAt(builder, lastBuyAt):
    builder.PrependInt64Slot(2, lastBuyAt, 0)

def AddLastBuyAt(builder, lastBuyAt):
    UserBazaarTraderSetElementAddLastBuyAt(builder, lastBuyAt)

def UserBazaarTraderSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserBazaarTraderSetElementEnd(builder)
