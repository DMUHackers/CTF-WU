#Ducks
[The ducks](http://ducks.sctf.michaelz.xyz/) and I have a unfinished score to settle.

## Solution
1. On accessing the website we are presented with a password box and link to the source code

2. The source code has the following lines of interest

   ```
    <?php if ($_SERVER["REQUEST_METHOD"] == "POST") { ?>
        <?php
        extract($_POST);
        if ($pass == $thepassword_123) { ?>
            <div class="alert alert-success">
                <code><?php echo $theflag; ?></code>
            </div>
        <?php } ?>
    <?php } ?>
    ```

3. Next I entered a password and captured the post request in Burp

4. Seeing that the password was being sent as "pass" I guessed that I had to ammended the request to also send "thepassword_123" and resent, which gave us the flag `sctf{maybe_i_shouldn't_have_extracted_everything_huh}`
