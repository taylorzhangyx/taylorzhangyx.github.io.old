class Solution(object):
  def oneEditDistance(self, source, target):
    """
    input: string source, string target
    return: boolean
    """
    # write your solution here
    ls = len(source)
    lt = len(target)
    if lt > ls:
      return self.oneEditDistance(target, source)

    if abs(ls - lt) > 1:
      return False
    diffCount = 0

    si = ls-1
    ti = lt-1
    while ti >= 0 and si>=0:
      # compare the char at si
      if source[si] == target[ti]:
        si -= 1
        ti -= 1
        continue
      else:
        diffCount += 1
        if diffCount > 1:
          return False
        if si > ti:
          si-=1
        elif ti > si:
          ti-=1
        else:
          si-=1
          ti-=1
    return diffCount == 1 or (diffCount == 0 and abs(ti - si)==1)
