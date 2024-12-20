# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserDealerSeenSlotMasterSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserDealerSeenSlotMasterSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserDealerSeenSlotMasterSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserDealerSeenSlotMasterSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserDealerSeenSlotMasterSetElement
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserDealerSeenSlotMasterSetElement
    def MasterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserDealerSeenSlotMasterSetElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserDealerSeenSlotMasterSetElementStart(builder)

def UserDealerSeenSlotMasterSetElementAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserDealerSeenSlotMasterSetElementAddId(builder, id)

def UserDealerSeenSlotMasterSetElementAddMasterId(builder, masterId):
    builder.PrependUint32Slot(1, masterId, 0)

def AddMasterId(builder, masterId):
    UserDealerSeenSlotMasterSetElementAddMasterId(builder, masterId)

def UserDealerSeenSlotMasterSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserDealerSeenSlotMasterSetElementEnd(builder)