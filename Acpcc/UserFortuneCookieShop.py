# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFortuneCookieShop(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFortuneCookieShop()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFortuneCookieShop(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFortuneCookieShop
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFortuneCookieShop
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def StockedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def DisplayedCookieLabels(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # UserFortuneCookieShop
    def DisplayedCookieLabelsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def DisplayedCookieLabelsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # UserFortuneCookieShop
    def DisplayedCookieStates(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def DisplayedCookieStatesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def DisplayedCookieStatesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def DisplayedCookieStatesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # UserFortuneCookieShop
    def NowPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def FilledPointCardNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def EatCookieLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserFortuneCookieShop
    def EatCookiePurchaseType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemCountsPerCookie(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def EatLottedItemCountsPerCookieAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemCountsPerCookieLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemCountsPerCookieIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # UserFortuneCookieShop
    def EatLottedItemIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserFortuneCookieShop
    def EatLottedItemIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # UserFortuneCookieShop
    def EatLottedItemQuantities(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def EatLottedItemQuantitiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemQuantitiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemQuantitiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # UserFortuneCookieShop
    def EatBonusItemIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserFortuneCookieShop
    def EatBonusItemIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # UserFortuneCookieShop
    def EatBonusItemQuantities(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def EatBonusItemQuantitiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemQuantitiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemQuantitiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # UserFortuneCookieShop
    def EatOmenMessageIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserFortuneCookieShop
    def EatOmenMessageIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatOmenMessageIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatOmenMessageIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # UserFortuneCookieShop
    def EatEatingId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def PresentedGroupNos(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserFortuneCookieShop
    def PresentedGroupNosAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # UserFortuneCookieShop
    def PresentedGroupNosLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def PresentedGroupNosIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # UserFortuneCookieShop
    def EatLottedItemNewFlags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def EatLottedItemNewFlagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemNewFlagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatLottedItemNewFlagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0

    # UserFortuneCookieShop
    def EatBonusItemNewFlags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserFortuneCookieShop
    def EatBonusItemNewFlagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemNewFlagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieShop
    def EatBonusItemNewFlagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # UserFortuneCookieShop
    def EatCookieRouteType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def EatCookieExpiredAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def TotalPointsDuringEat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def SentPostItemsCountByEat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieShop
    def IsEatMulti(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserFortuneCookieShopStart(builder):
    builder.StartObject(23)

def Start(builder):
    UserFortuneCookieShopStart(builder)

def UserFortuneCookieShopAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserFortuneCookieShopAddId(builder, id)

def UserFortuneCookieShopAddStockedAt(builder, stockedAt):
    builder.PrependInt64Slot(1, stockedAt, 0)

def AddStockedAt(builder, stockedAt):
    UserFortuneCookieShopAddStockedAt(builder, stockedAt)

def UserFortuneCookieShopAddDisplayedCookieLabels(builder, displayedCookieLabels):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(displayedCookieLabels), 0)

def AddDisplayedCookieLabels(builder, displayedCookieLabels):
    UserFortuneCookieShopAddDisplayedCookieLabels(builder, displayedCookieLabels)

def UserFortuneCookieShopStartDisplayedCookieLabelsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDisplayedCookieLabelsVector(builder, numElems):
    return UserFortuneCookieShopStartDisplayedCookieLabelsVector(builder, numElems)

def UserFortuneCookieShopAddDisplayedCookieStates(builder, displayedCookieStates):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(displayedCookieStates), 0)

def AddDisplayedCookieStates(builder, displayedCookieStates):
    UserFortuneCookieShopAddDisplayedCookieStates(builder, displayedCookieStates)

def UserFortuneCookieShopStartDisplayedCookieStatesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartDisplayedCookieStatesVector(builder, numElems):
    return UserFortuneCookieShopStartDisplayedCookieStatesVector(builder, numElems)

def UserFortuneCookieShopAddNowPoint(builder, nowPoint):
    builder.PrependInt32Slot(4, nowPoint, 0)

def AddNowPoint(builder, nowPoint):
    UserFortuneCookieShopAddNowPoint(builder, nowPoint)

def UserFortuneCookieShopAddFilledPointCardNumber(builder, filledPointCardNumber):
    builder.PrependInt32Slot(5, filledPointCardNumber, 0)

def AddFilledPointCardNumber(builder, filledPointCardNumber):
    UserFortuneCookieShopAddFilledPointCardNumber(builder, filledPointCardNumber)

def UserFortuneCookieShopAddEatCookieLabel(builder, eatCookieLabel):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(eatCookieLabel), 0)

def AddEatCookieLabel(builder, eatCookieLabel):
    UserFortuneCookieShopAddEatCookieLabel(builder, eatCookieLabel)

def UserFortuneCookieShopAddEatCookiePurchaseType(builder, eatCookiePurchaseType):
    builder.PrependUint8Slot(7, eatCookiePurchaseType, 0)

def AddEatCookiePurchaseType(builder, eatCookiePurchaseType):
    UserFortuneCookieShopAddEatCookiePurchaseType(builder, eatCookiePurchaseType)

def UserFortuneCookieShopAddEatLottedItemCountsPerCookie(builder, eatLottedItemCountsPerCookie):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(eatLottedItemCountsPerCookie), 0)

def AddEatLottedItemCountsPerCookie(builder, eatLottedItemCountsPerCookie):
    UserFortuneCookieShopAddEatLottedItemCountsPerCookie(builder, eatLottedItemCountsPerCookie)

def UserFortuneCookieShopStartEatLottedItemCountsPerCookieVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartEatLottedItemCountsPerCookieVector(builder, numElems):
    return UserFortuneCookieShopStartEatLottedItemCountsPerCookieVector(builder, numElems)

def UserFortuneCookieShopAddEatLottedItemIds(builder, eatLottedItemIds):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(eatLottedItemIds), 0)

def AddEatLottedItemIds(builder, eatLottedItemIds):
    UserFortuneCookieShopAddEatLottedItemIds(builder, eatLottedItemIds)

def UserFortuneCookieShopStartEatLottedItemIdsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartEatLottedItemIdsVector(builder, numElems):
    return UserFortuneCookieShopStartEatLottedItemIdsVector(builder, numElems)

def UserFortuneCookieShopAddEatLottedItemQuantities(builder, eatLottedItemQuantities):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(eatLottedItemQuantities), 0)

def AddEatLottedItemQuantities(builder, eatLottedItemQuantities):
    UserFortuneCookieShopAddEatLottedItemQuantities(builder, eatLottedItemQuantities)

def UserFortuneCookieShopStartEatLottedItemQuantitiesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartEatLottedItemQuantitiesVector(builder, numElems):
    return UserFortuneCookieShopStartEatLottedItemQuantitiesVector(builder, numElems)

def UserFortuneCookieShopAddEatBonusItemIds(builder, eatBonusItemIds):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(eatBonusItemIds), 0)

def AddEatBonusItemIds(builder, eatBonusItemIds):
    UserFortuneCookieShopAddEatBonusItemIds(builder, eatBonusItemIds)

def UserFortuneCookieShopStartEatBonusItemIdsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartEatBonusItemIdsVector(builder, numElems):
    return UserFortuneCookieShopStartEatBonusItemIdsVector(builder, numElems)

def UserFortuneCookieShopAddEatBonusItemQuantities(builder, eatBonusItemQuantities):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(eatBonusItemQuantities), 0)

def AddEatBonusItemQuantities(builder, eatBonusItemQuantities):
    UserFortuneCookieShopAddEatBonusItemQuantities(builder, eatBonusItemQuantities)

def UserFortuneCookieShopStartEatBonusItemQuantitiesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartEatBonusItemQuantitiesVector(builder, numElems):
    return UserFortuneCookieShopStartEatBonusItemQuantitiesVector(builder, numElems)

def UserFortuneCookieShopAddEatOmenMessageIds(builder, eatOmenMessageIds):
    builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(eatOmenMessageIds), 0)

def AddEatOmenMessageIds(builder, eatOmenMessageIds):
    UserFortuneCookieShopAddEatOmenMessageIds(builder, eatOmenMessageIds)

def UserFortuneCookieShopStartEatOmenMessageIdsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartEatOmenMessageIdsVector(builder, numElems):
    return UserFortuneCookieShopStartEatOmenMessageIdsVector(builder, numElems)

def UserFortuneCookieShopAddEatEatingId(builder, eatEatingId):
    builder.PrependUint32Slot(14, eatEatingId, 0)

def AddEatEatingId(builder, eatEatingId):
    UserFortuneCookieShopAddEatEatingId(builder, eatEatingId)

def UserFortuneCookieShopAddPresentedGroupNos(builder, presentedGroupNos):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(presentedGroupNos), 0)

def AddPresentedGroupNos(builder, presentedGroupNos):
    UserFortuneCookieShopAddPresentedGroupNos(builder, presentedGroupNos)

def UserFortuneCookieShopStartPresentedGroupNosVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPresentedGroupNosVector(builder, numElems):
    return UserFortuneCookieShopStartPresentedGroupNosVector(builder, numElems)

def UserFortuneCookieShopAddEatLottedItemNewFlags(builder, eatLottedItemNewFlags):
    builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(eatLottedItemNewFlags), 0)

def AddEatLottedItemNewFlags(builder, eatLottedItemNewFlags):
    UserFortuneCookieShopAddEatLottedItemNewFlags(builder, eatLottedItemNewFlags)

def UserFortuneCookieShopStartEatLottedItemNewFlagsVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartEatLottedItemNewFlagsVector(builder, numElems):
    return UserFortuneCookieShopStartEatLottedItemNewFlagsVector(builder, numElems)

def UserFortuneCookieShopAddEatBonusItemNewFlags(builder, eatBonusItemNewFlags):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(eatBonusItemNewFlags), 0)

def AddEatBonusItemNewFlags(builder, eatBonusItemNewFlags):
    UserFortuneCookieShopAddEatBonusItemNewFlags(builder, eatBonusItemNewFlags)

def UserFortuneCookieShopStartEatBonusItemNewFlagsVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartEatBonusItemNewFlagsVector(builder, numElems):
    return UserFortuneCookieShopStartEatBonusItemNewFlagsVector(builder, numElems)

def UserFortuneCookieShopAddEatCookieRouteType(builder, eatCookieRouteType):
    builder.PrependInt32Slot(18, eatCookieRouteType, 0)

def AddEatCookieRouteType(builder, eatCookieRouteType):
    UserFortuneCookieShopAddEatCookieRouteType(builder, eatCookieRouteType)

def UserFortuneCookieShopAddEatCookieExpiredAt(builder, eatCookieExpiredAt):
    builder.PrependInt64Slot(19, eatCookieExpiredAt, 0)

def AddEatCookieExpiredAt(builder, eatCookieExpiredAt):
    UserFortuneCookieShopAddEatCookieExpiredAt(builder, eatCookieExpiredAt)

def UserFortuneCookieShopAddTotalPointsDuringEat(builder, totalPointsDuringEat):
    builder.PrependInt32Slot(20, totalPointsDuringEat, 0)

def AddTotalPointsDuringEat(builder, totalPointsDuringEat):
    UserFortuneCookieShopAddTotalPointsDuringEat(builder, totalPointsDuringEat)

def UserFortuneCookieShopAddSentPostItemsCountByEat(builder, sentPostItemsCountByEat):
    builder.PrependUint8Slot(21, sentPostItemsCountByEat, 0)

def AddSentPostItemsCountByEat(builder, sentPostItemsCountByEat):
    UserFortuneCookieShopAddSentPostItemsCountByEat(builder, sentPostItemsCountByEat)

def UserFortuneCookieShopAddIsEatMulti(builder, isEatMulti):
    builder.PrependBoolSlot(22, isEatMulti, 0)

def AddIsEatMulti(builder, isEatMulti):
    UserFortuneCookieShopAddIsEatMulti(builder, isEatMulti)

def UserFortuneCookieShopEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFortuneCookieShopEnd(builder)
