# Direct-Mapped-cache-python-implementation

  ## About project:
  Implementaion of direct mapped cache with 256 lines and varying words per line (1->16) using python, where each word is of 32 bits size.

## Aim:
To observe and study the change in hit ratio for differing conditions such as number of words per line, number of lines, number of instructions.

## mem_gen.py:
In mem_gen.py, we are implementing a main memory file with 1000000 entries (since creating a file with 2<sup>36</sup> entries will become too big; 11.64 GB to be exact).
Hence, we whenever we want to access memory beyond 10<sup>6</sup>, we are doing instr_no%10<sup>6</sup>

## memory.dat:
Contains 10<sup>6</sup> random entries between 0 and 255.

## cache.py:
mem list contains entries of main memory
cache list is used to find whether the memory instruction is a hit or a miss
cache_data list contains data stored in cache
after reading all instructions from input trace files gives an output file output.txt

## output.txt:
tells us whether each instruction is a miss or hit and what and where the data is read/stored, i.e. in cache/memory.

## hit ratio vs number of instructions plot
![Alt text](hit_ratio_ni.png?raw=true "hit ratio varying with number of instructions")

## hit ratio vs number of words per line plot
![Alt text](hit_ratio_wp.png?raw=true "hit ratio varying with change in number of words per line")

## Done by:
### 1.C P Vikram Adithya
### 2.Parithimalan A
### 3.Sriram G

