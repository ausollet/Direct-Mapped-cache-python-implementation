# Direct-Mapped-cache-python-implementation

## About project:
Implementaion of direct mapped cache with 256 lines and varying words per line (1->16) using python, where each word is of 32 bits size.

## Aim:
To observe and study the change in hit ratio for differing conditions such as number of words per line, number of lines, number of instructions.

## Working:
In mem_gen.py, we are implementing a main memory file with 1000000 entries (since creating a file with 2<sup>36</sup> entries will become too big; 11.64 GB to be exact).
Hence, we whenever we want to access memory beyond 10^6, we are doing instr_no%10<sup>6</sup>

## hit ratio vs number of instructions plot
![Alt text](hit_ratio_ni.png?raw=true "hit ratio varying with number of instructions")

## hit ratio vs number of words per line plot
![Alt text](hit_ratio_wp.png?raw=true "hit ratio varying with change in number of words per line")

