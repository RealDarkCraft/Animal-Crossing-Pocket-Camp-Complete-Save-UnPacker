# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftPeddlerOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftPeddlerOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftPeddlerOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftPeddlerOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftPeddlerOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftPeddlerOneSlot
    def PeddlerSettingId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftPeddlerOneSlot
    def DisappearUnixTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserCraftPeddlerOneSlot
    def EndDisappearIntervalUnixTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserCraftPeddlerOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserCraftPeddlerOneSlotStart(builder)

def UserCraftPeddlerOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserCraftPeddlerOneSlotAddId(builder, id)

def UserCraftPeddlerOneSlotAddPeddlerSettingId(builder, peddlerSettingId):
    builder.PrependUint32Slot(1, peddlerSettingId, 0)

def AddPeddlerSettingId(builder, peddlerSettingId):
    UserCraftPeddlerOneSlotAddPeddlerSettingId(builder, peddlerSettingId)

def UserCraftPeddlerOneSlotAddDisappearUnixTime(builder, disappearUnixTime):
    builder.PrependInt64Slot(2, disappearUnixTime, 0)

def AddDisappearUnixTime(builder, disappearUnixTime):
    UserCraftPeddlerOneSlotAddDisappearUnixTime(builder, disappearUnixTime)

def UserCraftPeddlerOneSlotAddEndDisappearIntervalUnixTime(builder, endDisappearIntervalUnixTime):
    builder.PrependInt64Slot(3, endDisappearIntervalUnixTime, 0)

def AddEndDisappearIntervalUnixTime(builder, endDisappearIntervalUnixTime):
    UserCraftPeddlerOneSlotAddEndDisappearIntervalUnixTime(builder, endDisappearIntervalUnixTime)

def UserCraftPeddlerOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftPeddlerOneSlotEnd(builder)