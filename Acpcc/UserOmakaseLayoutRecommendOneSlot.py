# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserOmakaseLayoutRecommendOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserOmakaseLayoutRecommendOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserOmakaseLayoutRecommendOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserOmakaseLayoutRecommendOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserOmakaseLayoutRecommendOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOmakaseLayoutRecommendOneSlot
    def RecommendRecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOmakaseLayoutRecommendOneSlot
    def RecommendFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserOmakaseLayoutRecommendOneSlotStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserOmakaseLayoutRecommendOneSlotStart(builder)

def UserOmakaseLayoutRecommendOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserOmakaseLayoutRecommendOneSlotAddId(builder, id)

def UserOmakaseLayoutRecommendOneSlotAddRecommendRecipeId(builder, recommendRecipeId):
    builder.PrependUint32Slot(1, recommendRecipeId, 0)

def AddRecommendRecipeId(builder, recommendRecipeId):
    UserOmakaseLayoutRecommendOneSlotAddRecommendRecipeId(builder, recommendRecipeId)

def UserOmakaseLayoutRecommendOneSlotAddRecommendFlag(builder, recommendFlag):
    builder.PrependUint32Slot(2, recommendFlag, 0)

def AddRecommendFlag(builder, recommendFlag):
    UserOmakaseLayoutRecommendOneSlotAddRecommendFlag(builder, recommendFlag)

def UserOmakaseLayoutRecommendOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserOmakaseLayoutRecommendOneSlotEnd(builder)