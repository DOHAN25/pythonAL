# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
# re.sub（정규 표현식, 대상 문자열 , 치환 문자）
# 정규 표현식 - 검색 패턴을 지정
# 대상 문자열 - 검색 대상이 되는 문자열
# 치환 문자 - 변경하고 싶은 문자
import collections
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
print(words)
counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


mostCommonWord(paragraph, banned)



