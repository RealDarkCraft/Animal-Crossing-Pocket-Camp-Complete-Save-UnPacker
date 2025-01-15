# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserLostItemQuest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserLostItemQuest()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserLostItemQuest(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserLostItemQuest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserLostItemQuest
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserLostItemQuest
    def Love(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserLostItemQuest
    def Bell(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserLostItemQuest
    def PrevTarget(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserLostItemQuest
    def CurrentTarget(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserLostItemQuest
    def AnythingUpdateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserLostItemQuest
    def QuestProgress(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserLostItemQuest
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserLostItemQuest
    def ItemState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserLostItemQuestStart(builder):
    builder.StartObject(9)

def Start(builder):
    UserLostItemQuestStart(builder)

def UserLostItemQuestAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserLostItemQuestAddId(builder, id)

def UserLostItemQuestAddLove(builder, love):
    builder.PrependInt32Slot(1, love, 0)

def AddLove(builder, love):
    UserLostItemQuestAddLove(builder, love)

def UserLostItemQuestAddBell(builder, bell):
    builder.PrependInt32Slot(2, bell, 0)

def AddBell(builder, bell):
    UserLostItemQuestAddBell(builder, bell)

def UserLostItemQuestAddPrevTarget(builder, prevTarget):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(prevTarget), 0)

def AddPrevTarget(builder, prevTarget):
    UserLostItemQuestAddPrevTarget(builder, prevTarget)

def UserLostItemQuestAddCurrentTarget(builder, currentTarget):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(currentTarget), 0)

def AddCurrentTarget(builder, currentTarget):
    UserLostItemQuestAddCurrentTarget(builder, currentTarget)

def UserLostItemQuestAddAnythingUpdateTime(builder, anythingUpdateTime):
    builder.PrependInt64Slot(5, anythingUpdateTime, 0)

def AddAnythingUpdateTime(builder, anythingUpdateTime):
    UserLostItemQuestAddAnythingUpdateTime(builder, anythingUpdateTime)

def UserLostItemQuestAddQuestProgress(builder, questProgress):
    builder.PrependInt32Slot(6, questProgress, 0)

def AddQuestProgress(builder, questProgress):
    UserLostItemQuestAddQuestProgress(builder, questProgress)

def UserLostItemQuestAddUniqueId(builder, uniqueId):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(uniqueId), 0)

def AddUniqueId(builder, uniqueId):
    UserLostItemQuestAddUniqueId(builder, uniqueId)

def UserLostItemQuestAddItemState(builder, itemState):
    builder.PrependInt32Slot(8, itemState, 0)

def AddItemState(builder, itemState):
    UserLostItemQuestAddItemState(builder, itemState)

def UserLostItemQuestEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserLostItemQuestEnd(builder)