#include <stdio.h>
#include <string.h>
int main()
{
  char word[] = "Hello, World!";
  for (int i = 0; i < strlen(word); ++i) {
    printf("%c", word[i]);
  }
  return 0;
}
