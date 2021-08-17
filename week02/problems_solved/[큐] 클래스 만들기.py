n = int(input("정수를 몇 개 저장할까요?: "))
a = [None]*n

cnt = 0
while True:
    a[cnt%n] = int(input(f"{cnt+1}번째 정수를 입력하세요: "))
    cnt += 1

    retry = input("계속 입력할까요?(Y/N): ")
    if retry in {'N', 'n'}:
        break

start_index = cnt - n

# 만약 입력을 n보다 적게 받은 경우
if start_index < 0:
    start_index = 0

while start_index < cnt:
    print(f"{start_index+1}번째 = {a[start_index%n]}")
    start_index+=1









# from typing import Any

# class FixedQueue:

#     class Empty(Exception):
#         pass

#     class Full(Exception):
#         pass

#     def __init__(self, capacity: int) -> None:
#         self.no = 0
#         self.front = 0
#         self.rear = 0
#         self.capacity = capacity
#         self.que = [None]*capacity

#     def __len__(self) -> int:
#         return self.no

#     def is_empty(self) -> bool:
#         return self.no <= 0

#     def is_full(self) -> bool:
#         return self.no >= self.capacity


#     def enque(self, x: Any) -> None:

#         if self.is_full():
#             raise FixedQueue.Full
        
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no += 1

#         if self.rear == self.capacity:
#             self.rear = 0
    
#     def deque(self) -> Any:

#         if self.is_empty():
#             raise FixedQueue.Empty
        
#         x = self.que[self.front]
#         # self.que[self.front] = None
#         self.front += 1
#         self.no -= 1
        
#         if self.front == self.capacity:
#             self.front = 0

#         return x
 
#     def peek(self) -> Any:

#         if self.is_empty():
#             raise FixedQueue.Empty

#         return self.que[self.front]

#     def find(self, value: Any) -> Any:

#         idx = -1

#         for i in range(len(self.no)):
#             if self.que[(i+self.front)%self.capacity] == value:
#                 idx = self.que[(i+self.front)%self.capacity]
#                 break

#         return idx

#     def count(self, value:Any) -> int:

#         cnt = 0

#         for i in range(len(self.no)):
#             idx = (i+self.front)%self.capacity
#             if self.que[idx] == value:
#                 cnt += 1
        
#         return cnt

#     def __contains__(self, value:Any) -> bool:

#         if self.count(value) == 0:
#             return False
        
#         return True
    
#     def clear(self) -> None:
#         self.no = 0
#         self.front = 0
#         self.rear = 0
    
#     def dump(self) -> None:

#         if self.is_empty():
#             print("The que is empty.")
#         else:
#             for i in range(len(self.no)):
#                 idx = (i+self.front)%self.capacity
#                 print(f"{self.que[idx]} ", end="")
#             print()
