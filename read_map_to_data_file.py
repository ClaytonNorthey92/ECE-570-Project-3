import json
from PIL import Image

if __name__=='__main__':
	image = Image.open('localmap.gif')
	pixels = image.load()
	(width, length) = image.size;
	valid_locations = []
	colors = []
	for w in range(width):
		for l in range(length):
			colors.append(pixels[w,l])
			if pixels[w,l] != 2:
				valid_locations.append('dot-{}-{}'.format(w, l))
	f = open('json_data.dat', 'w')
	f.write(json.dumps(valid_locations))
	print set(colors)
	f.close()
