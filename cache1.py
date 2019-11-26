import matplotlib.pyplot as plt
import math
import glob
import numpy as np

#lines=256
#words_per_line = np.linspace(1, 16, 1)

def getindex(hexa, ttl_lines, w):
    dec=int(hexa,16)
    add=format(dec,'032b')
    tag=32-int(math.log2(ttl_lines))-int(math.log2(w))-2
    add1='0b'+add[tag:tag+8]
    dec=int(add1,2)
    return dec

def gettag(hexa, ttl_lines, w):
    dec=int(hexa,16)
    add=format(dec,'032b')
    tag=32-int(math.log2(ttl_lines))-int(math.log2(w))-2
    add1='0b'+add[:tag]
    dec=int(add1,2)
    return dec

def getoffset(hexa, ttl_lines, w):
    dec=int(hexa,16)
    add=format(dec,'032b')
    offset = int(math.log2(w))+2
    add1 = '0b'+add[32-offset:32]
    add1 = format(int(add1, 2), '032b')
    return add1

def create_cache_data(w, ttl_lines):
  cd = []
  for i in range(ttl_lines):
    cd.append([])
    for j in range(w):
      cd[i].append([-1, -1, -1, -1])
  
  return cd

if __name__ == "__main__":
  lines=256 #number of lines of cache
  words_per_line = np.asarray([1,2,4,8,16])
  trace_files = [] #list of trace files to use. Can either use all trace files or define your own.
  hit_ratio_for_each_variation = {}
  hits_each={}
  if(len(trace_files)==0): #if list of trace files not defined, uses all trace files in current directory
    for File in glob.glob('*.trace'):
      trace_files.append(File)
  o = open('output.txt', 'w')
  
  for file_name in trace_files: #iterates through each trace file in list of trace files
    hit_ratio = [] #array of hit ratios
    for w in words_per_line:
      f=open(file_name,"r")
      m = open('memory.dat', 'r')
      o.write('FILE: '+file_name+' words per line: '+ str(w)+'\n\n')
      mem = m.readlines()
      instr=f.readlines()
      cache=[]
      cache_data = create_cache_data(w, lines)
      block_offset = []
      byte_offset = []
      tags=[]
      for i in range(lines):
        cache.append(False)
        tags.append(-1)
        cache_data.append([])
        for j in range(w):
          cache_data[i].append([])
      hits=0
      c=0
      hitpar=[]
      for i in instr:
        c+=1
        words=i.split(' ')
        hexa=words[1][2:]
        to_do = words[0][:]
        value = words[2][:]
        a = '0b'
        for i in range(32-int(math.log2(2))):
          a+='0'
        block_offset = int(a+getoffset(hexa, lines, w)[32-2-int(math.log2(w)):32-2], 2)
        byte_offset = int('0b000000000000000000000000000000'+getoffset(hexa, lines, w)[30:], 2)
        ind=getindex(hexa, lines, w)
        tag=gettag(hexa, lines, w)
        address = int('0x'+hexa, 16)
        mem[address%10**6] = value
        hexa = '0x'+hexa[0:30-int(math.log2(w))]
        for k in range(int(math.log2(w))+2):
          hexa+='0'
        hexa = int(hexa, 16)
        if cache[ind]==True:
          if tags[ind]==tag:
            hits=hits+1
            if to_do=='l':
              o.write('cache hit! required data read from cache: '+ str(cache_data[ind][block_offset][byte_offset])) #data read from cache
            elif to_do=='s':
              o.write('cache hit! given data already in cache: '+ str(cache_data[ind][block_offset][byte_offset])) #data in cache and memory
          else:
            tags[ind]=tag
            if to_do=='l':            
              o.write('cache miss! required data read from memory: '+str(mem[address%10**6])) #data read from memory
            elif to_do=='s':
              o.write('cache miss! given data has now been stored in cache and memory: '+str(mem[address%10**6])) #data has been stored in cache and memory
            for i in range(w):
              for j in range(4):
                cache_data[ind][i][j] = mem[hexa%10**6]
                hexa+=1
        else:
          cache[ind]=True
          tags[ind]=tag
          if to_do=='l':          
            o.write('cache miss! required data read from memory: '+str(mem[address%10**6])) #data read from memory
          elif to_do=='s':
            o.write('cache miss! given data has now been stored in cache and memory: '+str(mem[address%10**6])) #data has been stored in cache and memory
          for i in range(w):
            for j in range(4):
              cache_data[ind][i][j] = mem[hexa%10**6]
              hexa+=1
        hitpercentage=hits*100/c
        hitpar.append(hitpercentage)
      hit_ratio.append(hits*100/c)
      hits_each[file_name]=hitpar
    hit_ratio_for_each_variation[file_name]=hit_ratio
  for i in hit_ratio_for_each_variation.keys():
    plt.plot(np.log2(words_per_line), hit_ratio_for_each_variation[i], label = i) #plotting hit ratio for each file, while words_per_line varies from 1 to 16
  plt.xlim(0,5)
  plt.legend(loc='lower right')
  plt.title('Hit rate vs words per line')
  plt.xlabel('log2(Words per line)')
  plt.ylabel('Hit Rate')
  plt.savefig('hit_ratio_wp.png')
  plt.show()
  for i in hits_each.keys():
    plt.plot(range(len(hits_each[i])),hits_each[i],label=i)
  plt.xlim(0,8e5)
  plt.legend(loc='lower right')
  plt.title('Hit rate vs number of instructions')
  plt.xlabel('Number of Instructions')
  plt.ylabel('Hit Rate')
  plt.savefig('hit_ratio_ni.png')
  plt.show()
  o.close()
  m.close()