# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventSpFurnitureNpcTalkParamElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventSpFurnitureNpcTalkParamElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventSpFurnitureNpcTalkParamElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventSpFurnitureNpcTalkParamElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventSpFurnitureNpcTalkParamElement
    def NpcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventSpFurnitureNpcTalkParamElement
    def LongParam01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserTapEventSpFurnitureNpcTalkParamElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserTapEventSpFurnitureNpcTalkParamElementStart(builder)

def UserTapEventSpFurnitureNpcTalkParamElementAddNpcId(builder, npcId):
    builder.PrependUint32Slot(0, npcId, 0)

def AddNpcId(builder, npcId):
    UserTapEventSpFurnitureNpcTalkParamElementAddNpcId(builder, npcId)

def UserTapEventSpFurnitureNpcTalkParamElementAddLongParam01(builder, longParam01):
    builder.PrependInt64Slot(1, longParam01, 0)

def AddLongParam01(builder, longParam01):
    UserTapEventSpFurnitureNpcTalkParamElementAddLongParam01(builder, longParam01)

def UserTapEventSpFurnitureNpcTalkParamElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventSpFurnitureNpcTalkParamElementEnd(builder)