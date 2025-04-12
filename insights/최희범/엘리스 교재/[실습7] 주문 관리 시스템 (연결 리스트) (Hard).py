'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
연결리스트는 삭제, 추가가 빠르지만
데이터 길이가 길면 탐색에 시간이 오래걸림.
특정요소를 빠르게 하려면 어떻게 해야할까?
dic 구조, 즉 해쉬테이블 자료구조로 처리해보자

'''

class LinkedListElement :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext

class orderManager :
    def __init__(self) :
        self.start = None
        self.end = None
        self.elems = {} # 주문번호를 저장하는 딕셔너리

    def addOrder(self, orderId) :
        elem = LinkedListElement(orderId, None, None)

        self.elems[orderId] = elem # 주문 번호로 어떤 실제 객체가 있는지 알 수 있음

        if self.start == None and self.end == None:
            self.start = elem
            self.end = elem
        else:
            self.end.myNext = elem
            elem.myPrev =self.end
            self.end= elem


    def removeOrder(self, orderId) :
        if self.start == None and self.end == None:
            return

        cur = self.elems[orderId] # orderId를 키로 갖는 밸류를 cur에 넣음

        if self.start == cur and self.end == cur: # self.start, self.end 가 cur라면 둘 다 None으로 소멸시켜라
            self.start = None
            self.end = None
        
        elif self.start == cur:
            self.start = cur.myNext
            cur.myNext.myPrev = None
            # [cur] -> [cur.myNext]
        elif self.end == cur:
            self.end = cur.myPrev
            cur.myPrev.myNext = None
        else:
            cur.myPrev.myNext = cur.myNext
            cur.myNext.myPrev = cur.myPrev

    def getOrder(self, orderId) :
        cnt = 1
        cur = self.start

        while cur != None:
            if cur.data == orderId:
                return cnt
            cur = cur.myNext
            cnt += 1

        return -1

    # dic을 넣었더니 862.718 ms 로 속도가 11배 가량 개선되었다.
