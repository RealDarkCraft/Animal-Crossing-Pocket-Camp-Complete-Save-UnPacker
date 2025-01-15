# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserNpcEpisodeOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserNpcEpisodeOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserNpcEpisodeOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserNpcEpisodeOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserNpcEpisodeOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserNpcEpisodeOneSlot
    def IsFixed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcEpisodeOneSlot
    def IsSeen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcEpisodeOneSlot
    def IsNew(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserNpcEpisodeOneSlot
    def EpisodeNo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserNpcEpisodeOneSlot
    def IsCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserNpcEpisodeOneSlotStart(builder):
    builder.StartObject(6)

def Start(builder):
    UserNpcEpisodeOneSlotStart(builder)

def UserNpcEpisodeOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserNpcEpisodeOneSlotAddId(builder, id)

def UserNpcEpisodeOneSlotAddIsFixed(builder, isFixed):
    builder.PrependBoolSlot(1, isFixed, 0)

def AddIsFixed(builder, isFixed):
    UserNpcEpisodeOneSlotAddIsFixed(builder, isFixed)

def UserNpcEpisodeOneSlotAddIsSeen(builder, isSeen):
    builder.PrependBoolSlot(2, isSeen, 0)

def AddIsSeen(builder, isSeen):
    UserNpcEpisodeOneSlotAddIsSeen(builder, isSeen)

def UserNpcEpisodeOneSlotAddIsNew(builder, isNew):
    builder.PrependBoolSlot(3, isNew, 0)

def AddIsNew(builder, isNew):
    UserNpcEpisodeOneSlotAddIsNew(builder, isNew)

def UserNpcEpisodeOneSlotAddEpisodeNo(builder, episodeNo):
    builder.PrependUint32Slot(4, episodeNo, 0)

def AddEpisodeNo(builder, episodeNo):
    UserNpcEpisodeOneSlotAddEpisodeNo(builder, episodeNo)

def UserNpcEpisodeOneSlotAddIsCheck(builder, isCheck):
    builder.PrependBoolSlot(5, isCheck, 0)

def AddIsCheck(builder, isCheck):
    UserNpcEpisodeOneSlotAddIsCheck(builder, isCheck)

def UserNpcEpisodeOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserNpcEpisodeOneSlotEnd(builder)
