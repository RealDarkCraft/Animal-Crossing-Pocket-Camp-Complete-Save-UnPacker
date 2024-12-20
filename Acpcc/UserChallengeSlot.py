# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserChallengeSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserChallengeSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserChallengeSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserChallengeSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserChallengeSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserChallengeSlot
    def IsAchieve(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserChallengeSlot
    def ChallengeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserChallengeSlot
    def MissionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserChallengeSlot
    def Counter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserChallengeSlot
    def ValueArray(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # UserChallengeSlot
    def ValueArrayLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserChallengeSlot
    def ValueArrayIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # UserChallengeSlot
    def ExpiredTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserChallengeSlotStart(builder):
    builder.StartObject(7)

def Start(builder):
    UserChallengeSlotStart(builder)

def UserChallengeSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserChallengeSlotAddId(builder, id)

def UserChallengeSlotAddIsAchieve(builder, isAchieve):
    builder.PrependBoolSlot(1, isAchieve, 0)

def AddIsAchieve(builder, isAchieve):
    UserChallengeSlotAddIsAchieve(builder, isAchieve)

def UserChallengeSlotAddChallengeType(builder, challengeType):
    builder.PrependInt32Slot(2, challengeType, 0)

def AddChallengeType(builder, challengeType):
    UserChallengeSlotAddChallengeType(builder, challengeType)

def UserChallengeSlotAddMissionId(builder, missionId):
    builder.PrependUint32Slot(3, missionId, 0)

def AddMissionId(builder, missionId):
    UserChallengeSlotAddMissionId(builder, missionId)

def UserChallengeSlotAddCounter(builder, counter):
    builder.PrependInt32Slot(4, counter, 0)

def AddCounter(builder, counter):
    UserChallengeSlotAddCounter(builder, counter)

def UserChallengeSlotAddValueArray(builder, valueArray):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(valueArray), 0)

def AddValueArray(builder, valueArray):
    UserChallengeSlotAddValueArray(builder, valueArray)

def UserChallengeSlotStartValueArrayVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartValueArrayVector(builder, numElems):
    return UserChallengeSlotStartValueArrayVector(builder, numElems)

def UserChallengeSlotAddExpiredTime(builder, expiredTime):
    builder.PrependInt64Slot(6, expiredTime, 0)

def AddExpiredTime(builder, expiredTime):
    UserChallengeSlotAddExpiredTime(builder, expiredTime)

def UserChallengeSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserChallengeSlotEnd(builder)
