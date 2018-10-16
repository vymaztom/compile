#include <stdlib.h>
#include <stdio.h>
#include "include/statistic.h"

char text[] =
"Toto jsou 2 vzorove vety, ktere budou zpracovavany Vasemi funkcemi.Auto Hyundai ix35 ma pres 120 konskych sil.";



int main(int argc, char const *argv[]) {
    printf("STRING for statistic:\n");
    printf("%s\n", text);
    printf("SUM of alphabets: %i\n",getSumOfAlphabets(text));
    printf("SUM of numbers  : %i\n",getSumOfNumbers(text));
    return 0;
}
