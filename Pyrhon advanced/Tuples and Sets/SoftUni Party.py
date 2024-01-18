dUb = int(input())
passes = set() #set
for fart in range(dUb): #for-loop for the 2nd input and putting the info in the set
    pass_for_the_kvass = input()
    passes.add(pass_for_the_kvass)

pass_for_the_kvass = input()
while pass_for_the_kvass != "END":
    if pass_for_the_kvass in passes:
        passes.remove(pass_for_the_kvass)
    pass_for_the_kvass = input()

print(len(passes))
for pass_for_the_kvass in sorted(passes):
    print(pass_for_the_kvass)