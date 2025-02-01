import random

val = random.randint(1,10)
# val2 = random.randfloat(0,1)
print(val)
# print(val2)

colors = ['Red','Black','White']
# returns an array with k values chosen randomly from colors
results = random.choices(colors,k =5);
print(results)

col2 = ["Blue","Yellow","Green"];
#asigning weights to every value to decide their probability if getting selected
res2 = random.choices(col2,weights=[5,3,2],k=10);
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(res2)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

deck = list(range(1,53));
print(deck)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
random.shuffle(deck)
print(deck)
# picking a random sample of size 5 from deck
hand = random.sample(deck,k=5);
print(hand)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava",
    "William", "Sophia", "James", "Isabella", "Oliver",
    "Mia", "Benjamin", "Charlotte", "Elijah", "Amelia",
    "Lucas", "Harper", "Mason", "Evelyn", "Logan",
    "Abigail", "Alexander", "Emily", "Ethan", "Elizabeth",
    "Jacob", "Mila", "Michael", "Ella", "Daniel",
    "Avery", "Henry", "Sofia", "Jackson", "Camila",
    "Sebastian", "Aria", "Aiden", "Scarlett", "Matthew",
    "Victoria", "Samuel", "Madison", "David", "Luna",
    "Joseph", "Grace", "Carter", "Chloe", "Owen"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris",
    "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall",
    "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]

cities = [
    "New York", "London", "Paris", "Tokyo", "Berlin",
    "Sydney", "Toronto", "Moscow", "Dubai", "Singapore",
    "Los Angeles", "Rome", "Beijing", "Mumbai", "Cairo",
    "Bangkok", "Madrid", "Seoul", "Amsterdam", "Istanbul",
    "Chicago", "Hong Kong", "São Paulo", "Barcelona", "Vienna",
    "San Francisco", "Toronto", "Shanghai", "Mexico City", "Miami"
]

street_names = [
    "Main Street", "First Avenue", "Maple Avenue", "Oak Street", "Elm Street",
    "Park Avenue", "Cedar Lane", "Pine Street", "Washington Street", "Lakeview Drive",
    "Sunset Boulevard", "Hillcrest Road", "Broadway", "Church Street", "Willow Lane",
    "Highland Avenue", "Riverside Drive", "Forest Road", "Spring Street", "Meadow Lane",
    "Victoria Road", "King Street", "Queen Street", "Union Street", "Market Street",
    "Grove Street", "Chestnut Avenue", "Birch Street", "Magnolia Drive", "Jefferson Avenue"
]

#generate new addresses and emails using random functions
for num in range(100):
    first = random.choice(names)
    last = random.choice(last_names)

    phone = f'{random.randint(100,999)}--333--{random.randint(1000,9999)}'

    street_num = random.randint(10,999);
    street = random.choice(street_names)
    city = random.choice(cities)
    zip_code = random.randint(10000,99999)
    address = f'{street_num} {street}, {city}, {zip_code}'
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(address)
    email = f"{first}_{last}_{random.randint(1,200)}@bogus.email";
    
    print(email)