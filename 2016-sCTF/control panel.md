#Control Panel
Take control... of the flag on this [admin control panel](http://cpanel.sctf.michaelz.xyz/).

## Solution
1. Accessed the control panel and registered an account

2. I then logged into the account and was given the message `No flag for you. You're not an admin.` and in the HTML comments `Error: user.admin is not equal to true.`

3. I then logged out and went back to the registration page, I captured a registration request in Burp

4. From the error message I added `admin=true` to the registration post request and sent it

5. This logged me straight in and gave me the flag `sctf{TIL_noSql_cAn_bE_InjeKT3d_t0o}`
