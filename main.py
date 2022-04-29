
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
      
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MeD={}):
    # TODO -  implement memoization
    memo = len(S), len(T)
  
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
      if memo in MeD:
        return MeD[memo]
        
      if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
      else:
          MeD[memo] = (1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))
    return MeD[memo]
      

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
  s, t = ''
  c = 0
  memo = len(S), len(T)
  if (S == ''):
    s = ('{}'.format('-'*len(T)))
    c = len(t)
  elif (T == ''):
    t = ('{}'.format('-'*len(S)))
    c = len(s)
  else:
    
    
  

  
  return s, t, c
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

print(test_MED())