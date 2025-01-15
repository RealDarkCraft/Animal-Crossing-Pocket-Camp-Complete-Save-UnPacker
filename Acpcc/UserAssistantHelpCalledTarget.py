# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserAssistantHelpCalledTarget(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserAssistantHelpCalledTarget()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserAssistantHelpCalledTarget(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserAssistantHelpCalledTarget
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserAssistantHelpCalledTarget
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAssistantHelpCalledTarget
    def AppearAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserAssistantHelpCalledTarget
    def NpcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAssistantHelpCalledTarget
    def QuestRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserAssistantHelpCalledTargetStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserAssistantHelpCalledTargetStart(builder)

def UserAssistantHelpCalledTargetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserAssistantHelpCalledTargetAddId(builder, id)

def UserAssistantHelpCalledTargetAddAppearAt(builder, appearAt):
    builder.PrependInt64Slot(1, appearAt, 0)

def AddAppearAt(builder, appearAt):
    UserAssistantHelpCalledTargetAddAppearAt(builder, appearAt)

def UserAssistantHelpCalledTargetAddNpcId(builder, npcId):
    builder.PrependUint32Slot(2, npcId, 0)

def AddNpcId(builder, npcId):
    UserAssistantHelpCalledTargetAddNpcId(builder, npcId)

def UserAssistantHelpCalledTargetAddQuestRank(builder, questRank):
    builder.PrependInt32Slot(3, questRank, 0)

def AddQuestRank(builder, questRank):
    UserAssistantHelpCalledTargetAddQuestRank(builder, questRank)

def UserAssistantHelpCalledTargetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserAssistantHelpCalledTargetEnd(builder)