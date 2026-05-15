from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) #key:string val:[val,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        #add the value and the timestamp to the store
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        #get list of values for each person
        values = self.store.get(key,[])

        #binary search in window
        l,r = 0, len(values)-1
        #we want a specific point so they will eventually converge
        while l <=r :
            m = (l + r)//2
            #if we find the timestamp return it
            if values[m][1] == timestamp:
                return values[m][0]
            #if the item has a timestamp less than what we want
            #save it and move inwards, this will give us the closest 
            #if our value is not there
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            #but if its greater move left
            else:
                r = m - 1
        
        return res