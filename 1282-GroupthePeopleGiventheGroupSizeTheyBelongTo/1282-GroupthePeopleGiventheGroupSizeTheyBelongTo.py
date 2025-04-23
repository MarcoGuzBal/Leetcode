# Last updated: 4/23/2025, 12:03:12 AM
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hashmap = {}

        # Iterate through groupSizes
        # If the size already exists, append the list that is not full
        # If it doesnt exist, create a list for that value

        for size, value in enumerate(groupSizes):
            print(hashmap)
            if value in hashmap:
                List = hashmap[value]
                for group in List:
                    if len(group) < value:
                        group.append(size)
                        break
                else: 
                    hashmap[value].append([size])
            else:
                hashmap[value] = []
                hashmap[value].append([size])

        result = []
        for groups in hashmap.values():
            result.extend(groups)

        return result


       