# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFacilityCheckOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFacilityCheckOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFacilityCheckOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFacilityCheckOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFacilityCheckOneSlotSetElement
    def FacilityId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFacilityCheckOneSlotSetElement
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def UserFacilityCheckOneSlotSetElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserFacilityCheckOneSlotSetElementStart(builder)

def UserFacilityCheckOneSlotSetElementAddFacilityId(builder, facilityId):
    builder.PrependUint32Slot(0, facilityId, 0)

def AddFacilityId(builder, facilityId):
    UserFacilityCheckOneSlotSetElementAddFacilityId(builder, facilityId)

def UserFacilityCheckOneSlotSetElementAddState(builder, state):
    builder.PrependUint8Slot(1, state, 0)

def AddState(builder, state):
    UserFacilityCheckOneSlotSetElementAddState(builder, state)

def UserFacilityCheckOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFacilityCheckOneSlotSetElementEnd(builder)
