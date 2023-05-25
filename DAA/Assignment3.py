#structure of idem which stores weight an corresponding value of item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

#main greedy function to solve problem
def fractionalKnapsack(W, arr):

    #sorting item on basis of ratio
    arr.sort(key=lambda x: (x.value/x.weight),reverse= True)

    #uncomment to see new order of Item with their ratio for item in arr
    #result value in knapsack
    finalvalue =0.0

    #looping through all items
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        else:
            finalvalue += item.value * W/item.weight
            break
    #returning final value
    return finalvalue

#drivers code
if __name__ == "__main__":

    #weight of knapsack
    W = 50
    arr = [Item(60,10), Item(100,20), Item(120,30)]

    #function call
    max_val = fractionalKnapsack(W,arr)
    print ('Maximum value we can obtain = {}'.format(max_val))