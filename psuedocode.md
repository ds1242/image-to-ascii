# Psuedocode Steps
 - Convert the input image to grayscale.
 - Split the image into M×N tiles.
 - Correct M (the number of rows) to match the image and font aspect ratio.
 - Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
 - Assemble rows of ASCII character strings and print them to a file to form the final image.

