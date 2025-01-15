# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserAchievementUnlockedData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserAchievementUnlockedData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserAchievementUnlockedData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserAchievementUnlockedData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserAchievementUnlockedData
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAchievementUnlockedData
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserAchievementUnlockedData
    def UnlockedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserAchievementUnlockedDataStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserAchievementUnlockedDataStart(builder)

def UserAchievementUnlockedDataAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserAchievementUnlockedDataAddId(builder, id)

def UserAchievementUnlockedDataAddLabel(builder, label):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)

def AddLabel(builder, label):
    UserAchievementUnlockedDataAddLabel(builder, label)

def UserAchievementUnlockedDataAddUnlockedAt(builder, unlockedAt):
    builder.PrependInt64Slot(2, unlockedAt, 0)

def AddUnlockedAt(builder, unlockedAt):
    UserAchievementUnlockedDataAddUnlockedAt(builder, unlockedAt)

def UserAchievementUnlockedDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserAchievementUnlockedDataEnd(builder)
