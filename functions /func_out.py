
words = ["happy","birthday","to","you"]


def smash(words):
    
    #words.append(input(print("Enter the worlds")))
    #words = ["john","is","going","home"]
    print("welcome to words prog")

    smashed = "".join(words)

    return smashed



def count(words):

    for _ in words:

        new = _.split(words)

        print(new)

    return new

