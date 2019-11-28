# Direct-Mapped-cache-python-implementation

## About project:
Implementaion of direct mapped cache with 256 lines and varying words per line (1->16) using python, where each word is of 32 bits size.

## Aim:
To observe and study the change in hit ratio for differing conditions such as number of words per line, number of lines, number of instructions.

## mem_gen.py:
In mem_gen.py, we are implementing a main memory file with 1000000 entries (since creating a file with 2<sup>36</sup> entries will become too big; 11.64 GB to be exact).
Hence, we whenever we want to access memory beyond 10<sup>6</sup>, we are doing [integer value of memory address]%10<sup>6</sup>.

## memory.dat:
Contains 10<sup>6</sup> random entries between 0 and 255.

## cache.py:
mem list contains entries of main memory
cache list is used to find whether the memory instruction is a hit or a miss
cache_data list contains data stored in cache
after reading all instructions from input trace files gives an output file output.txt.

## output.txt:
tells us whether each instruction is a miss or hit and what and where the data is read/stored, i.e. in cache/memory.
![Alt text](output_file_screenshot.png?raw=true "sample output screenshot")

## Pre-requisites for running the code:
1. Keep all files in same directory
2. Run the code using python3
3. Run mem_gen.py before running cache.py

## Getting the output:
1. Run cache.py
2. One shall get two .png files, namely hit_ratio_ni and hit_ratio_wp, saved in the directory
3. output.txt file, containing details about cache hit/miss is generated in the working directory

## Plots:

### hit ratio varying with number of instructions plot (words per line of cache fixed as 16)
![Alt text](hit_ratio_ni.png?raw=true "hit ratio varying with number of instructions")

### hit ratio varying with number of words per line plot
![Alt text](hit_ratio_wp.png?raw=true "hit ratio varying with change in number of words per line")

## Errors and their possible reasons:
1. discrepancy in data of cache vs memory
### Possible reason:
we believe, that this discrepancy is arising due to us using %10<sup>6</sup> of address, thus changing the tag and maybe the index of where the data is going to be stored at. The block and byte offset remain unaffected by this change.
This doesn't affect cache hit/miss ratio as we have implemented that seperately, without the need of main memory.
The only reason as to why we didn't use a main memory of 2<sup>32</sup> entries, is because it's size is too big (**11.64 GB!!**)
We believe, that if a proper main memory with 2<sup>36</sup> entires is used (don't forget to remove %10<sup>6</sup> in cache.py), then there will not exist any discrepancy between data used and data stored.

## Done by:
### 1. C P Vikram Adithya
### 2. Parithimalan A
### 3. Sriram G
