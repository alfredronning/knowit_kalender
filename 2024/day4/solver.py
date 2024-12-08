from PIL import Image

def extract_lsb(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size
    lsb_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            lsb_r = (r & 1) * 255
            lsb_g = (g & 1) * 255
            lsb_b = (b & 1) * 255
            lsb_img.putpixel((x, y), (lsb_r, lsb_g, lsb_b))
    lsb_img.save(output_path)

input_image = "santa.png"
output_image = "res.png"
extract_lsb(input_image, output_image)

