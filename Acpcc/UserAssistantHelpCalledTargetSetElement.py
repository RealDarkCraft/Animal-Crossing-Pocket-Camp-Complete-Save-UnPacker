# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserAssistantHelpCalledTargetSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserAssistantHelpCalledTargetSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserAssistantHelpCalledTargetSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserAssistantHelpCalledTargetSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserAssistantHelpCalledTargetSetElement
    def AppearAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserAssistantHelpCalledTargetSetElement
    def NpcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAssistantHelpCalledTargetSetElement
    def QuestRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserAssistantHelpCalledTargetSetElementStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserAssistantHelpCalledTargetSetElementStart(builder)

def UserAssistantHelpCalledTargetSetElementAddAppearAt(builder, appearAt):
    builder.PrependInt64Slot(0, appearAt, 0)

def AddAppearAt(builder, appearAt):
    UserAssistantHelpCalledTargetSetElementAddAppearAt(builder, appearAt)

def UserAssistantHelpCalledTargetSetElementAddNpcId(builder, npcId):
    builder.PrependUint32Slot(1, npcId, 0)

def AddNpcId(builder, npcId):
    UserAssistantHelpCalledTargetSetElementAddNpcId(builder, npcId)

def UserAssistantHelpCalledTargetSetElementAddQuestRank(builder, questRank):
    builder.PrependInt32Slot(2, questRank, 0)

def AddQuestRank(builder, questRank):
    UserAssistantHelpCalledTargetSetElementAddQuestRank(builder, questRank)

def UserAssistantHelpCalledTargetSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserAssistantHelpCalledTargetSetElementEnd(builder)