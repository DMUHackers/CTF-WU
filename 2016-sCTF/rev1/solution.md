#Rev1
Let's start out with an easy, typical reversing problem.

The answer will not be in the typical sctf{flag} format, so when you do get it, you must put it into the format by doing sctf{flag_you_found}

#Solution
1. Get the strings used in the programme using `strings rev1`
2. Read through the output and you still see a line `h4x0r!!!H`
3. Cut off the odd "H" gives us `h4x0r!!!` which is the flag
