# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFurniturePuzzleProgress(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFurniturePuzzleProgress()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFurniturePuzzleProgress(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFurniturePuzzleProgress
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFurniturePuzzleProgress
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFurniturePuzzleProgress
    def LessonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFurniturePuzzleProgress
    def MedalNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFurniturePuzzleProgress
    def NewState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserFurniturePuzzleProgress
    def MaxScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserFurniturePuzzleProgressStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserFurniturePuzzleProgressStart(builder)

def UserFurniturePuzzleProgressAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserFurniturePuzzleProgressAddId(builder, id)

def UserFurniturePuzzleProgressAddLessonId(builder, lessonId):
    builder.PrependUint32Slot(1, lessonId, 0)

def AddLessonId(builder, lessonId):
    UserFurniturePuzzleProgressAddLessonId(builder, lessonId)

def UserFurniturePuzzleProgressAddMedalNum(builder, medalNum):
    builder.PrependInt32Slot(2, medalNum, 0)

def AddMedalNum(builder, medalNum):
    UserFurniturePuzzleProgressAddMedalNum(builder, medalNum)

def UserFurniturePuzzleProgressAddNewState(builder, newState):
    builder.PrependUint8Slot(3, newState, 0)

def AddNewState(builder, newState):
    UserFurniturePuzzleProgressAddNewState(builder, newState)

def UserFurniturePuzzleProgressAddMaxScore(builder, maxScore):
    builder.PrependInt32Slot(4, maxScore, 0)

def AddMaxScore(builder, maxScore):
    UserFurniturePuzzleProgressAddMaxScore(builder, maxScore)

def UserFurniturePuzzleProgressEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFurniturePuzzleProgressEnd(builder)