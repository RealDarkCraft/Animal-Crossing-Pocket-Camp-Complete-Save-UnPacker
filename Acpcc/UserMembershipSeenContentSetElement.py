# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMembershipSeenContentSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMembershipSeenContentSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMembershipSeenContentSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMembershipSeenContentSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMembershipSeenContentSetElement
    def MembershipMenuButtonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserMembershipSeenContentSetElementStart(builder):
    builder.StartObject(1)

def Start(builder):
    UserMembershipSeenContentSetElementStart(builder)

def UserMembershipSeenContentSetElementAddMembershipMenuButtonId(builder, membershipMenuButtonId):
    builder.PrependUint32Slot(0, membershipMenuButtonId, 0)

def AddMembershipMenuButtonId(builder, membershipMenuButtonId):
    UserMembershipSeenContentSetElementAddMembershipMenuButtonId(builder, membershipMenuButtonId)

def UserMembershipSeenContentSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMembershipSeenContentSetElementEnd(builder)