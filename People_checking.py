
def people_in_family(num_people):
    if num_people<=7:
        return '34$'
    elif 14<=num_people<=15:
        return'68$'
    else:
        return'78$'

num_people=int(input("How much people are there in yuor family"))
total_payment= people_in_family(num_people)
print(f"Toatal payment:{total_payment}")
