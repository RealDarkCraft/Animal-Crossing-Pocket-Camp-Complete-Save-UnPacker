# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserChatHistoryWithNpc(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserChatHistoryWithNpc()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserChatHistoryWithNpc(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserChatHistoryWithNpc
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserChatHistoryWithNpc
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserChatHistoryWithNpc
    def WithNpcLotteryId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserChatHistoryWithNpc
    def LottedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserChatHistoryWithNpcStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserChatHistoryWithNpcStart(builder)

def UserChatHistoryWithNpcAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserChatHistoryWithNpcAddId(builder, id)

def UserChatHistoryWithNpcAddWithNpcLotteryId(builder, withNpcLotteryId):
    builder.PrependUint32Slot(1, withNpcLotteryId, 0)

def AddWithNpcLotteryId(builder, withNpcLotteryId):
    UserChatHistoryWithNpcAddWithNpcLotteryId(builder, withNpcLotteryId)

def UserChatHistoryWithNpcAddLottedAt(builder, lottedAt):
    builder.PrependInt64Slot(2, lottedAt, 0)

def AddLottedAt(builder, lottedAt):
    UserChatHistoryWithNpcAddLottedAt(builder, lottedAt)

def UserChatHistoryWithNpcEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserChatHistoryWithNpcEnd(builder)