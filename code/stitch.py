from PIL import Image

# stitches images together horizontally (useful for comparing upscaling comparisons)

if __name__ == "__name__":
  images = []

  while True:
    image = input("Enter the name of an image to stitch (type \"none\" to continue): ")
    
    if image == "none":
      break
    else:
      images.append(image)

  images = [Image.open(x) for x in images]
  widths, heights = zip(*(i.size for i in images))

  result_width = sum(widths)
  max_height = max(heights)

  stitched_image = Image.new('RGB', (result_width, max_height))

  current_x = 0

  for im in images:
    stitched_image.paste(im, (current_x, 0))
    current_x += im.size[0]

  stitched_image.save('out.jpg')