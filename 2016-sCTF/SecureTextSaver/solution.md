#Secure Text Saver
Will you test out my new program for me? It saves important info and keeps it away from prying eyes!

(See Jar in folder)

## Solution
1. Upload the Jar to an online decompiler, I used [this one](http://www.javadecompilers.com/)
2. Looking at the code we find this line `accounts.add(new Account("ztaylor54", "]!xME}behA8qjM~T".toCharArray()));`
3. From there we use those creditials to run the Jar and login
4. this gives us the flag `sctf{w0w_th4t_w45_pr377y_e45y}` 
