#include <ctype.h>
#include <string.h>

int getSumOfAlphabets(char *str){
    int size = strlen(str), ret = 0;
    for(int i = 0 ; i < size ; i++){
        if(isalpha((int)str[i])){
            ret++;
        }
    }
    return ret;
}

int getSumOfNumbers(char* str){
    int size = strlen(str), ret = 0;
    for(int i = 0 ; i < size ; i++){
        if(isdigit((int)str[i])){
            ret++;
        }
    }
    return ret;
}
