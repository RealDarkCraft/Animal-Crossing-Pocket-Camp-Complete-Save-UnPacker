# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftPeddler(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftPeddler()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftPeddler(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftPeddler
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftPeddler
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftPeddler
    def EndLotteryIntervalUnixTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserCraftPeddler
    def IsSeenFooterPeddlerIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCraftPeddler
    def IsSeenFooterPaintingIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserCraftPeddlerStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserCraftPeddlerStart(builder)

def UserCraftPeddlerAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserCraftPeddlerAddId(builder, id)

def UserCraftPeddlerAddEndLotteryIntervalUnixTime(builder, endLotteryIntervalUnixTime):
    builder.PrependInt64Slot(1, endLotteryIntervalUnixTime, 0)

def AddEndLotteryIntervalUnixTime(builder, endLotteryIntervalUnixTime):
    UserCraftPeddlerAddEndLotteryIntervalUnixTime(builder, endLotteryIntervalUnixTime)

def UserCraftPeddlerAddIsSeenFooterPeddlerIcon(builder, isSeenFooterPeddlerIcon):
    builder.PrependBoolSlot(2, isSeenFooterPeddlerIcon, 0)

def AddIsSeenFooterPeddlerIcon(builder, isSeenFooterPeddlerIcon):
    UserCraftPeddlerAddIsSeenFooterPeddlerIcon(builder, isSeenFooterPeddlerIcon)

def UserCraftPeddlerAddIsSeenFooterPaintingIcon(builder, isSeenFooterPaintingIcon):
    builder.PrependBoolSlot(3, isSeenFooterPaintingIcon, 0)

def AddIsSeenFooterPaintingIcon(builder, isSeenFooterPaintingIcon):
    UserCraftPeddlerAddIsSeenFooterPaintingIcon(builder, isSeenFooterPaintingIcon)

def UserCraftPeddlerEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftPeddlerEnd(builder)