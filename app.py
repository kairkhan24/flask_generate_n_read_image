import uuid
from matplotlib import image as mpimage
from randimage import get_random_image, show_array
from flask import Flask, jsonify

app = Flask(__name__)

IMG_SIZE = (300, 300)


@app.route('/generate-image', methods=['GET'])
def generate_image():
	img = get_random_image(IMG_SIZE)
	mpimage.imsave('media/{}.png'.format(uuid.uuid4().hex), img)

	return jsonify({'success': True})






if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)