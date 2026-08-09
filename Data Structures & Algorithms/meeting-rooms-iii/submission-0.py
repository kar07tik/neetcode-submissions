import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:

        meetings.sort()

        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        used_rooms = []

        booking_count = [0] * n
        
        for start, end in meetings:

            while used_rooms and used_rooms[0][0] <= start:
                end_time, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)
            
            duration = end - start
            
            if available_rooms:

                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
 
                earliest_end, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (earliest_end + duration, room))
            
            booking_count[room] += 1
 
        return booking_count.index(max(booking_count))