# Caesar
- decrypts caesars cipher when partially decrypted word is provided in correct format
- I apologize to english users because this code uses czech for variables and comments and I didn't have the time to translate it yet.

### Quick description
- this script takes a .txt file as an input and outputs another .txt file. The input.txt file or whatever it's called, contains two lines. The first line contains the encrypted word. The second one contains partially decrypted word. The program reads those lines, and recurently moves the first line trough the entire alphabet. It then calculates how much does each output match and then it outputs the word that matches the most.
- there is a commented line that when uncommented, prints out a table that contains all the versions of the word moved through caesar cypher. It's basically kind of a brute force decryption that the program uses as I stated in the previous section.

### Usage
- use any basic console to run "python main.py vstup.txt" where "vstup.txt" contains the two lines with encrypted and partially encrypted words.
- "vstup.txt" is czech for "input.txt"
-
