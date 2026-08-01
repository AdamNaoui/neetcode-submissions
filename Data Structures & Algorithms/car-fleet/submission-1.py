class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed=list(zip(position,speed))
        position_and_speed.sort(key=lambda x:x[0])
        res=0
        while position_and_speed:
            p,s=position_and_speed.pop()
            final_time_ref=(target-p)/s
            res+=1
            print("NEW FLEET",p,s)

            while position_and_speed and final_time_ref>=(target-position_and_speed[-1][0])/position_and_speed[-1][1]:
                print(position_and_speed[-1])
                position_and_speed.pop()
           
        return res
        