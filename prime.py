import gmpy2
import random

import time


def is_prime(num):
    return naive(num)


# Simple bruteforce primality test
def naive(number):
    if number == 2:
        return True
    if number % 2 == 0 or number < 2:
        return False

    i = 3

    rooted = gmpy2.floor(gmpy2.sqrt(number))
    print rooted
    while i <= rooted:
        if number % i == 0:
            return False
        i += 2
        if i % 10000000 == 1:
            print i

    return True


def miller_rabin_primality_test(number):
    """
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( special case )
    if we get the number 1 we return false and any other even
    number we will return false.
    """
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False

    ''' first we want to express n as : 2^s * r ( were r is odd ) '''

    ''' the odd part of the number '''
    odd_part_of_number = number - 1

    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0

    ''' while r is even divid by 2 to find the odd part '''
    while odd_part_of_number % 2 == 0:
        odd_part_of_number /= 2
        timesTwoDividNumber += 1

    '''
    since there are number that are cases of "strong liar" we
    need to check more then one number
    '''
    for time in range(3):

        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number) - 1
            if randomNumber != 0 and randomNumber != 1:
                break

        ''' randomNumberWithPower = randomNumber^odd_part_of_number mod number '''
        randomNumberWithPower = pow(randomNumber, odd_part_of_number, number)

        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1

            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)

                # inc the number of iteration
                iterationNumber += 1
            '''
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if randomNumberWithPower != (number - 1):
                return False

    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True


def fermat_primality_test(number):
    """ if number != 1 """
    if number > 1:
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            random_number = random.randint(2, number) - 1

            ''' Test if a^(n-1) = 1 mod n '''
            if pow(random_number, number - 1, number) != 1:
                return False

        return True
    else:
        ''' case number == 1 '''
        return False


start = time.clock()
print miller_rabin_primality_test(2 ** 19937 - 1)
end = time.clock()
print 'computes in %s' % (end - start)
print fermat_primality_test(2 ** 19937 - 1)
print 'computes in %s' % (time.clock() - end)
