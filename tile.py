from PIL import Image
import random

width = 1200
height = 400
seed = 75
images = [
    {
        "path" : "bidoof.png",
        "amount" : 300, 
        "scale" : .35
    } #,
    # {
    #     "path" : "shiny.png", 
    #     "amount" : 1, 
    #     "scale" : .6
    # },
]

def tile(images, width, height, seed=random.random()):

    def defineOrder(images):
        order = [images[0]] * images[0]["amount"]
        for i in range(len(images) - 1):
            image = images[i + 1]
            for n in range(image["amount"]):
                order.insert(random.randint(0, len(order)), image)
        return order
    
    random.seed(seed)
    base = Image.new(mode="RGBA", size=(width, height), color=(255,255,255,255))

    for current in defineOrder(images):
        
        current["amount"] = current["amount"] - 1
        image = Image.open(current["path"])
        image.thumbnail((image.width, image.height * current["scale"]), Image.ANTIALIAS)

        x = random.randint(0 - image.size[0],width)
        y = random.randint(0 - image.size[1],height)

        for xoff in range(3):
            for yoff in range(3):
                    base.paste(image, (x + width * (xoff - 1), y + height * (yoff - 1)), image)

    base.save("output.png")

if __name__ == "__main__":
    tile(images, width, height, seed)