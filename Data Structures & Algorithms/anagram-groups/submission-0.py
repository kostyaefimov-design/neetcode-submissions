class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hesh = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in hesh:
                hesh[key] = []
            hesh[key].append(word)

        return list(hesh.values())