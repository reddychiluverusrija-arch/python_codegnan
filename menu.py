
menu={
    "monday":{
        "breakfast":"idly",
        "lunch":"rice and tomato",
        "dinner":"potato"
    },
    "tuesday":{
        "breakfast":"bonda",
        "lunch":"brinjal",
        "dinner":"carrot"
    },
    "wednesday":{
        "breakfast":"chapathi",
        "lunch":"bitter guard",
        "dinner":"egg"
    },
    "thursday":{
        "breakfast":"uthappa",
        "lunch":"dal",
        "dinner":"peas"
    },
    "friday":{
        "breakfast":"poori",
        "lunch":"vegtable rice",
        "dinner":"fried rice"
    },
    "saturday":{
        "breakfast":"dosa",
        "lunch":"bitter guard",
        "dinner":"cucumber"
    },
    "sunday":{
        "breakfast":"upma",
        "lunch":"spinach",
        "dinner":"chicken"
    }
}

day=(input("enter day:"))
meal=input("enter meal:")
print(menu[day][meal])

 