class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        ans = []
        dict = collections.defaultdict(int)
        for word in words:
            dict[word] += 1

        wordLen = len(words[0])
        for i in range(wordLen):
            index = i
            count = 0
            tempDict = collections.defaultdict(int)

            for j in range(i, len(s) - wordLen + 1, wordLen):
                str = s[j: j + wordLen]
                if str in dict.keys():
                    tempDict[str] += 1
                    count += 1
                    while tempDict[str] > dict[str]:
                        tempDict[s[index: index + wordLen]] -= 1
                        count -= 1
                        index += wordLen
                    if count == len(words):
                        ans.append(index)
                        tempDict[s[index: index + wordLen]] -= 1
                        count -= 1
                        index += wordLen
                else:
                    tempDict.clear()
                    count = 0
                    index = j + wordLen

        return ans
