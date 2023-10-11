coffe_counnter = 0
command = input()
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffe_counnter += 1
        else:
            coffe_counnter += 2
    command = input()
if coffe_counnter > 5:
    print("You need extra sleep")
else:
    print(coffe_counnter)