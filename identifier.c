//To determine whether a character entered is in lowercase, uppercase, digit or a special character.

#include <stdio.h>
int main()
{
    char c;
    printf("Enter a character: ");
    scanf("%c",&c);
    if(c>='A' && c<='Z')
        printf("Uppercase");
    else if(c>='a' && c<='z')
        printf("Lowercase");
    else if(c>='0' && c<='9')
        printf("Digit");
    else
        printf("Symbol");
}

