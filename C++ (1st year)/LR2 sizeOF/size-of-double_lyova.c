#include <stdio.h>
#include <math.h>

int sizeOfDouble() {
    // mantissa
    double tmp = 1.0;
    double prevTmp;
    int mantissa = 0;
    do {
        prevTmp = tmp;
        tmp = tmp/2 + 1;
        mantissa++;
    } while (tmp != prevTmp);
    mantissa -= 2;

    // counter <- 2**(exponent-1) + mantissa
    // exponent-1 because exponent also has a sign bit
    tmp = 1;
    int counter = 1;
    do {
        counter++;
        tmp /= 2;
    } while (tmp > 0);

    // sign bit
    tmp = 1;
    int sign = (int)(tmp != -tmp);
    
    int exponent = round(log2(counter-mantissa))+1;
    int total = mantissa + exponent + sign;
    printf("total: %d\nmantissa: %d\nexponent: %d\nsign: %d\n", 
                                total, mantissa, exponent, sign);
    return total; 
}


int main() {
    sizeOfDouble();
    return 0;
}

