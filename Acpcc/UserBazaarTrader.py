# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserBazaarTrader(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserBazaarTrader()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserBazaarTrader(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserBazaarTrader
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserBazaarTrader
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserBazaarTrader
    def PlayerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserBazaarTrader
    def BuyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserBazaarTrader
    def LastBuyAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserBazaarTraderStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserBazaarTraderStart(builder)

def UserBazaarTraderAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserBazaarTraderAddId(builder, id)

def UserBazaarTraderAddPlayerId(builder, playerId):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(playerId), 0)

def AddPlayerId(builder, playerId):
    UserBazaarTraderAddPlayerId(builder, playerId)

def UserBazaarTraderAddBuyCount(builder, buyCount):
    builder.PrependInt32Slot(2, buyCount, 0)

def AddBuyCount(builder, buyCount):
    UserBazaarTraderAddBuyCount(builder, buyCount)

def UserBazaarTraderAddLastBuyAt(builder, lastBuyAt):
    builder.PrependInt64Slot(3, lastBuyAt, 0)

def AddLastBuyAt(builder, lastBuyAt):
    UserBazaarTraderAddLastBuyAt(builder, lastBuyAt)

def UserBazaarTraderEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserBazaarTraderEnd(builder)