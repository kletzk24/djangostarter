from django.shortcuts import render
from django.http import Http404
from .models import Computed
from django.utils import timezone

# Create your views here.

# Computation function
# Computes the square of the given value.
# If the square of value has been computed before, it retrieves
# it from the database. Otherwise it computes the square and 
# stores it into the database.
# URL pattern: path('compute/<str:value>', views.compute, name='compute')
def compute(request, value):
    try:
        input = int(value)
        precomputed = Computed.objects.filter(input=input)
        if precomputed.count() == 0:  # square has not been computed
            # Compute the square
            answer = input * input
            time_computed = timezone.now()
            # Create a Computed object and store it
            computed = Computed(
                input=input, 
                output=answer,
                time_computed=time_computed
            )
            computed.save() # Saves the object into the database
        else: 
            # Retrieve the precomputed value
            computed = precomputed.first()
        
        # Return the result page
        return render (
            request,
            "basic/compute.html", # Template html file; contains placeholders for output
            {
                'input': input,
                'output': computed.output,
                'time_computed': computed.time_computed.strftime("%m-%d-%Y %H:%M:%S UTC")
            }
        )
    except:
        raise Http404(f"Invalid input: {value}")

# isprime function
# checks the given value if the value is prime
# if the value is prime, it will say so
# if the value is not prime, it will state it's divisors
# DOES NOT STORE VALUES
# URL pattern: path('isprime/<str:value>', views.isprime, name='isprime')
def isprime(request, value):
    try:
        # initiate variables
        input = int(value) # inputted value
        primecheck = True # prime flag
        divisors = [] # list of collected divisors
        result = "" # string to be built

        # check if prime
        for num in range(2, input):
            if (((input/num)%1)==0):
                primecheck = False
                divisors.append(num)
        
        # initiate a new variable
        time_computed = timezone.now() # records when the result was completed

        # build string message for output
        if (primecheck):
            # value is prime
            result += str(input) + " is a prime number since it has no divisors"
        else:
            # value is not prime
            result += str(input) + " is not a prime number since "
            
            if (len(divisors) == 1):
                # special case for 1 divisor, no plural grammer
                result += str(divisors[0]) + " is a divisor"

            if (len(divisors) == 2):
                # special case for 2 divisors, puts 'and' between two divisors
                result += str(divisors[0]) + " and " + str(divisors[1]) + " are divisors"

            else:
                # standard case, will have a grammer's list format
                for num in divisors:
                    if num != divisors[-1]:
                        # normal commas for list
                        result += str(num) + ", "

                    else: 
                        # no comma and ends in and for last divisor
                        result += "and " + str(num)

                result += " are divisors"


        # Return the result page
        return render (
            request,
            "basic/isprime.html",
            {
                'input': input,
                'output': result,
                'time_computed': time_computed.strftime("%m-%d-%Y %H:%M:%S UTC")
            }
        )
    except:
        raise Http404(f"Invalid input: {value}")
    