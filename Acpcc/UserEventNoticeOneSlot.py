# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserEventNoticeOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserEventNoticeOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserEventNoticeOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserEventNoticeOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserEventNoticeOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserEventNoticeOneSlot
    def CampaignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserEventNoticeOneSlot
    def BeginNoticeCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserEventNoticeOneSlot
    def EndNoticeCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserEventNoticeOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserEventNoticeOneSlotStart(builder)

def UserEventNoticeOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserEventNoticeOneSlotAddId(builder, id)

def UserEventNoticeOneSlotAddCampaignId(builder, campaignId):
    builder.PrependUint32Slot(1, campaignId, 0)

def AddCampaignId(builder, campaignId):
    UserEventNoticeOneSlotAddCampaignId(builder, campaignId)

def UserEventNoticeOneSlotAddBeginNoticeCount(builder, beginNoticeCount):
    builder.PrependUint32Slot(2, beginNoticeCount, 0)

def AddBeginNoticeCount(builder, beginNoticeCount):
    UserEventNoticeOneSlotAddBeginNoticeCount(builder, beginNoticeCount)

def UserEventNoticeOneSlotAddEndNoticeCount(builder, endNoticeCount):
    builder.PrependUint32Slot(3, endNoticeCount, 0)

def AddEndNoticeCount(builder, endNoticeCount):
    UserEventNoticeOneSlotAddEndNoticeCount(builder, endNoticeCount)

def UserEventNoticeOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserEventNoticeOneSlotEnd(builder)