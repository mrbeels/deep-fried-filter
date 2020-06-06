from PIL import Image, ImageFilter, ImageEnhance

INPUT_IMG = input("Image name please, sir! (with extension) :D : ")
OUTPUT_IMG = f'deep-fried-{INPUT_IMG}'.lower()
BRIGHTNESS_FACTOR = 1.4
CONTRAST_FACTOR = 3
SHARPNESS_FACTOR = 3.5


class Augment():

    def import_image(self, input_img='noIMG'):
        self.im = Image.open(input_img)

    def add_brightness(self, output_img="output", factor=0):
        apply_brightness = ImageEnhance.Brightness(self.im)
        enhanced = apply_brightness.enhance(factor)
        enhanced.save(output_img)
        self.im = enhanced

    def add_contrast(self, output_img="output", factor=0):
        apply_contrast = ImageEnhance.Contrast(self.im)
        enhanced = apply_contrast.enhance(factor)
        enhanced.save(output_img)
        self.im = enhanced

    def add_sharpness(self, output_img="output", factor=0):
        apply_sharpen = ImageEnhance.Sharpness(self.im)
        enhanced = apply_sharpen.enhance(factor)
        enhanced.save(output_img)
        self.im = enhanced


if __name__ == "__main__":
    try:
        print(
            "You are using Mr Beel's Deep Fried Meme Filter! \nCheck out : https://github.com/mrbeels \n\n    ( ͡° ͜ʖ ͡°) ¯\_(ツ)_/¯ \n")
        image = Augment()
        image.import_image(INPUT_IMG)
        for i in range(2):
            for j in range(2):
                image.add_contrast(OUTPUT_IMG, CONTRAST_FACTOR)
                for i in range(1):
                    image.add_sharpness(OUTPUT_IMG, SHARPNESS_FACTOR)
            image.add_brightness(OUTPUT_IMG, BRIGHTNESS_FACTOR)
        print(f"Output is {OUTPUT_IMG} with factors: \n{BRIGHTNESS_FACTOR} for brightness \n{CONTRAST_FACTOR} for contrast \n{SHARPNESS_FACTOR} for sharpness")
    except FileNotFoundError:
        print('File not found! T.T')
    except ValueError:
        print('Try another file? T.T')
