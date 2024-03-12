
print("---------- PART A ----------")

print("1. How many total combinations are possible? Show the math along with the code!")

dice_a = [1, 2, 3, 4, 5, 6]
dice_b = [1, 2, 3, 4, 5, 6]

combinations = []

for i in dice_a:
    for j in dice_b:
        combinations.append((i, j))

print(combinations)

print("math:\nAll different combinations possible = 6 * 6 = 36")

print(
    "2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!Hint: A 6 x 6 Matrix."
)

distribution= {}

for i in range(1,7):
    for j in range(1,7):
        if i+j not in distribution:
            distribution[i+j]=[]
        distribution[i+j].append((i,j))
  

print(distribution)

print(
    "3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2). Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain Sum = 2. Die A = Die B = 1."
)

sums = []

for i in dice_a:
    sum_row = []
    for j in dice_b:
        sum_row.append(i + j)
    sums.append(sum_row)

sums_probability = []

for i in range(2, 13):
    occurance = 0
    for row in sums:
        occurance += row.count(i)
    sums_probability.append(occurance)

print(sums_probability)

print("---------- PART B -----------")

print("----New pair formed-----")
def undoom_dice(org_Dice1,org_Dice2):
    def sum_of_dice(die_A, die_B):
        Dict = dict()
        for i in die_A:
            for j in die_B:
                sum = i + j
                if sum in Dict:
                    Dict[sum] += 1
                else:
                    Dict[sum] = 1
        return(Dict)



    def all_dice():
        array= []
        for x2 in range(2, 11):
            for x3 in range (x2, 11):
                for x4 in range (x3, 11):
                   for x5 in range (x4, 11):
                        for x6 in range (x5, 11):
                            array.append([1,x2,x3,x4,x5,x6])
        return array


    for die_A in all_dice():
         for die_B in all_dice():
           if max(die_A)<=4:
        # // die_A values <4
             if sum_of_dice(die_A, die_B) == sum_of_dice(org_Dice1, org_Dice2):
                print(die_A, die_B)

undoom_dice(dice_a,dice_b)