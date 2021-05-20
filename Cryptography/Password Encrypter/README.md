# Password Encrypter

This python program seems to take user input and does some encryption on this input and saves the encrypted text in a file.<br><br>

The encrypt function calls another function called debug in which it opens a file named '\x2e\x6c\x6f\x67'.<br>
Decoding this gives '.log'. This file is opened to write some data along with timestamp.<br><br>

Analysing the encrypt function, each letter in the user input is XOR'ed with value and multiplied with a constant.<br>
Finally it's base64 encoded.<br><br>

We can write a program to reverse this encryption process since if 'a XOR b = c' then 'a XOR c = b' and 'b XOR c = a'.

Use `my_password_decrypter.py` to decrypt the password and get the flag.
