#include <stdio.h>

void print_reversed(const char* str) {
  if (*str) {
    print_reversed(str + 1);
    printf("%c", *str);
  }
}

int main() {
  print_reversed("abcdef");
  printf("\n");
}