#Cookies
My mom put a password on the cookie jar :(

Will you help me get a cookie?

## Solution
1. Download the Jar file
2. run it through http://www.javadecompilers.com
3. in the decompiler we see the following line

   ```
  String answer = "fdf87a05e2169b88a8db5a1ebc15fa50";
  if (md5.equals(answer)) {
      System.out.println("success! it's working!");
  }
  ```
4. Running that MD5 through a reverser gets us `thisisaverystrongpassword`
5. Then we just run the jar and enter the password `thisisaverystrongpassword` which gives us the flag `sctf{g3t_y0ur_h4nd_0ut_0f_my_c00k13_j4r!}`
