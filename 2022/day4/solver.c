#include <stdio.h>
#include <math.h>

// Cache alle log(base), går fra 5.7 til 5.1 sec med "fast" optimalisering.
float logs[] = {log(2),log(3),log(4),log(5),log(6),log(7),log(8),log(9),log(10),log(11),log(12),log(13),log(14),log(15),log(16)};

int palidromInBase(int n, int base){
    int digits_1 = log(n)/logs[base-2];
    for(int i=0; i<=digits_1/2; i++){
        int div = pow(base, digits_1-i*2);
        if (n/div != n%base) return 0;
        n = n%div/base;
    }
    return 1;
}

int multiPalidrom(int n){
    int count = 0;
    for(int base=2; base<=16; base++){
        if (palidromInBase(n, base)) count++;
        if (count == 3) return 1;
    }
    return 0;
}

int main(){
    int count = 0;
    for(int n=1; n<10000000; n++){
        if (multiPalidrom(n)) count+=n;
    }
    printf("%i\n", count);
    return 0;
}

