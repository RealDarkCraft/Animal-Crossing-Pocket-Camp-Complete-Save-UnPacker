# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventDrawingTalkDataOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventDrawingTalkDataOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventDrawingTalkDataOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventDrawingTalkDataOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventDrawingTalkDataOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def NpcIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def DrawResultCase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def DrawResultItemLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserTapEventDrawingTalkDataOneSlot
    def DrawResultItemAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def MessageFile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserTapEventDrawingTalkDataOneSlot
    def MessageLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserTapEventDrawingTalkDataOneSlot
    def LovePoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def DrawResultItemCampaignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def DrawResultItemSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventDrawingTalkDataOneSlot
    def MessagePriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserTapEventDrawingTalkDataOneSlotStart(builder):
    builder.StartObject(11)

def Start(builder):
    UserTapEventDrawingTalkDataOneSlotStart(builder)

def UserTapEventDrawingTalkDataOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserTapEventDrawingTalkDataOneSlotAddId(builder, id)

def UserTapEventDrawingTalkDataOneSlotAddNpcIndex(builder, npcIndex):
    builder.PrependInt32Slot(1, npcIndex, 0)

def AddNpcIndex(builder, npcIndex):
    UserTapEventDrawingTalkDataOneSlotAddNpcIndex(builder, npcIndex)

def UserTapEventDrawingTalkDataOneSlotAddDrawResultCase(builder, drawResultCase):
    builder.PrependInt32Slot(2, drawResultCase, 0)

def AddDrawResultCase(builder, drawResultCase):
    UserTapEventDrawingTalkDataOneSlotAddDrawResultCase(builder, drawResultCase)

def UserTapEventDrawingTalkDataOneSlotAddDrawResultItemLabel(builder, drawResultItemLabel):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(drawResultItemLabel), 0)

def AddDrawResultItemLabel(builder, drawResultItemLabel):
    UserTapEventDrawingTalkDataOneSlotAddDrawResultItemLabel(builder, drawResultItemLabel)

def UserTapEventDrawingTalkDataOneSlotAddDrawResultItemAmount(builder, drawResultItemAmount):
    builder.PrependInt32Slot(4, drawResultItemAmount, 0)

def AddDrawResultItemAmount(builder, drawResultItemAmount):
    UserTapEventDrawingTalkDataOneSlotAddDrawResultItemAmount(builder, drawResultItemAmount)

def UserTapEventDrawingTalkDataOneSlotAddMessageFile(builder, messageFile):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(messageFile), 0)

def AddMessageFile(builder, messageFile):
    UserTapEventDrawingTalkDataOneSlotAddMessageFile(builder, messageFile)

def UserTapEventDrawingTalkDataOneSlotAddMessageLabel(builder, messageLabel):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(messageLabel), 0)

def AddMessageLabel(builder, messageLabel):
    UserTapEventDrawingTalkDataOneSlotAddMessageLabel(builder, messageLabel)

def UserTapEventDrawingTalkDataOneSlotAddLovePoint(builder, lovePoint):
    builder.PrependInt32Slot(7, lovePoint, 0)

def AddLovePoint(builder, lovePoint):
    UserTapEventDrawingTalkDataOneSlotAddLovePoint(builder, lovePoint)

def UserTapEventDrawingTalkDataOneSlotAddDrawResultItemCampaignId(builder, drawResultItemCampaignId):
    builder.PrependInt32Slot(8, drawResultItemCampaignId, 0)

def AddDrawResultItemCampaignId(builder, drawResultItemCampaignId):
    UserTapEventDrawingTalkDataOneSlotAddDrawResultItemCampaignId(builder, drawResultItemCampaignId)

def UserTapEventDrawingTalkDataOneSlotAddDrawResultItemSize(builder, drawResultItemSize):
    builder.PrependInt32Slot(9, drawResultItemSize, 0)

def AddDrawResultItemSize(builder, drawResultItemSize):
    UserTapEventDrawingTalkDataOneSlotAddDrawResultItemSize(builder, drawResultItemSize)

def UserTapEventDrawingTalkDataOneSlotAddMessagePriority(builder, messagePriority):
    builder.PrependInt32Slot(10, messagePriority, 0)

def AddMessagePriority(builder, messagePriority):
    UserTapEventDrawingTalkDataOneSlotAddMessagePriority(builder, messagePriority)

def UserTapEventDrawingTalkDataOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventDrawingTalkDataOneSlotEnd(builder)