#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <time.h>

int main(void)
{
  char* actualPw = "swordfish"; //Of course
  char guess[20];
  printf ("Enter the password: ");
  fgets ( guess, 80, stdin );

  //Strip the \n, replace with 0
  guess[strcspn(guess, "\n")] = 0;
  printf("You entered [%s]\n",guess);
  if(strcmp(guess,actualPw)==0){
    printf("Password Correct\n");
  }else{
    printf("Password Incorrect\n");
  }
}
