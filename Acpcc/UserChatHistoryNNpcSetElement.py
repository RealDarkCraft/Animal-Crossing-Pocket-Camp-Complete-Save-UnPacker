# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserChatHistoryNNpcSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserChatHistoryNNpcSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserChatHistoryNNpcSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserChatHistoryNNpcSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserChatHistoryNNpcSetElement
    def NnpcTalkLotteryId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserChatHistoryNNpcSetElement
    def MentalIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserChatHistoryNNpcSetElement
    def LottedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserChatHistoryNNpcSetElementStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserChatHistoryNNpcSetElementStart(builder)

def UserChatHistoryNNpcSetElementAddNnpcTalkLotteryId(builder, nnpcTalkLotteryId):
    builder.PrependUint32Slot(0, nnpcTalkLotteryId, 0)

def AddNnpcTalkLotteryId(builder, nnpcTalkLotteryId):
    UserChatHistoryNNpcSetElementAddNnpcTalkLotteryId(builder, nnpcTalkLotteryId)

def UserChatHistoryNNpcSetElementAddMentalIndex(builder, mentalIndex):
    builder.PrependInt32Slot(1, mentalIndex, 0)

def AddMentalIndex(builder, mentalIndex):
    UserChatHistoryNNpcSetElementAddMentalIndex(builder, mentalIndex)

def UserChatHistoryNNpcSetElementAddLottedAt(builder, lottedAt):
    builder.PrependInt64Slot(2, lottedAt, 0)

def AddLottedAt(builder, lottedAt):
    UserChatHistoryNNpcSetElementAddLottedAt(builder, lottedAt)

def UserChatHistoryNNpcSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserChatHistoryNNpcSetElementEnd(builder)