def print_big(letter):
    bigletters = {
        'a' : '  *  \n * * \n*****\n*   *\n*   *',
        'b' : '***\n*  *\n***\n*  *\n***',
        'c' : '  ***\n *   \n*    \n *   \n  ***',
        'd' : '***  \n*  * \n*   *\n*  * \n***',
        'e' : '*****\n*    \n***  \n*    \n*****'
    }

    print(bigletters[letter])
print_big('e')