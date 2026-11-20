candy = ("Jolly Ranchers", "Sour Patch Kids", "Lifesaver Gummies", "Airheads")
flavors = ("Green Apple", "Blue Raspberry", "Orange", "Pineapple", "Cherry")

candy_options = {
    candy[0] + " " + flavors[1],
    candy[1] + " " + flavors[2],
    candy[2] + " " + flavors[0],
}

print("Today's candy options include:")
print(candy_options)
