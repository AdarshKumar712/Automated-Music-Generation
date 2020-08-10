import numpy as np

#vocabulary
vocab = {'xxbos': 0,
 'xxpad': 1,
 'xxeos': 2,
 'xxsep': 3}

for i in range(128):
  vocab["n"+str(i)] = i+4

for i in range(256):
  vocab["d"+str(i)] = i+128+4

reverse_vocab = {0:'xxbos',
 1:'xxpad',
 2:'xxeos',
 3:'xxsep'}

for i in range(4, 128+4):
  reverse_vocab[i] = "n" + str(i-4)

for i in range(256):
  reverse_vocab[i+128+4] = "d"+str(i)


def convert_npenc(n, vocab, padd_bos=True):
  seq = []
  if padd_bos==True:
    seq = [0,1]
  for (x,y) in n:
    if(x==-1):
      seq.append(vocab["xxsep"])
    else:
      seq.append(vocab["n"+str(x)])
    seq.append(vocab["d"+str(y)])
  if padd_bos==True:
    seq.append(vocab["xxeos"])
  return seq


def deconvert_npenc(seq):
  n = []
  x = len(seq)
  j=0
  for i in range(0,x//2):
    n_1 = seq[j]-4
    d = seq[j+1] - 128-4
    if d<0:
      d = 2
      j+=1
    else:
      j+=2
    if n_1+4==0:
      continue
    elif n_1+4==2:
      break
    elif n_1+4==3:
      n_1=-1
      n.append(np.array([n_1,d]))
    else:
      n.append(np.array([n_1,d]))
    if(j==x-1):
        break
  return np.array(n)

def textify_seq(seq, reverse_vocab):
  text =[]
  for i in seq:
    text.append(reverse_vocab[i])
  return text