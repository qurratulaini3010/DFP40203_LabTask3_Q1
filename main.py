import os

computer = [
    {"Product": "Laptop Asus F15 Gaming",
     "Description": "Armed for combat, the TUF Gaming F15 features up to a 10th Gen Intel® Core™ i7 CPU with "
                    "6 cores and 12 threads to tear through serious gaming, streaming, and heavy duty "
                    "multitasking.",
     "Specification 1": "10TH GEN INTEL®CORE™ I7 CPU",
     "Specification 2": "NVIDIA® GEFORCE®GTX 1660 TI GPU",
     "Specification 3": "1TB SSD NVME PCIE"}
]

reviews = [
    {"review": "This laptop is great"}
]


def displayinfo():
    print("Product:", computer[0]["Product"])
    print("Product Description:", computer[0]["Description"])
    print("Product Specifications:", computer[0]["Specification 1"])
    print("Product Specifications:", computer[0]["Specification 2"])
    print("Product Specifications:", computer[0]["Specification 3"])


def displayreview():
    i = 0
    for i in range(0, len(reviews)):
        print(f"review:", reviews[i]["review"])
        i += 1


def savereview():
    review = input("Please input the reviews")
    if review:
        revie = {"review": review}
        reviews.append(revie)
        textreviews()


def textreviews():
    if not os.path.exists("reviews"):
        os.makedirs("reviews")

    with os.scandir("reviews") as directory:
        for entry in directory:
            if entry.is_file():
                os.remove(entry)
    for review in reviews:
        for comp in computer:
            with open(f"reviews/{comp['Product']}.txt", "w") as review_file:
                review_file.write(f"{comp['Product']}: {review['review']}\n")


displayinfo()
print("")
displayreview()
print("")
savereview()
