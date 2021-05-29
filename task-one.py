print("Zadanie 1 \n")

bakery = 'piekarnia'
grocery_store = 'warzywniak'

bakery_items = ['chleb', 'pączek', 'bułki']
grocery_items = ['marchew', 'seler', 'rukola']

bakery_items_capitalise = \
    [bakery_words.capitalize() for bakery_words in bakery_items]

grocery_items_capitalise = \
    [grocery_words.capitalize() for grocery_words in grocery_items]

shoping_dict = {
    bakery: bakery_items_capitalise,
    grocery_store: grocery_items_capitalise
}