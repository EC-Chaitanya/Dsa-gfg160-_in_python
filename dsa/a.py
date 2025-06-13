from PIL import Image, ImageDraw, ImageFont

# Draw left-aligned text starting from (x, y)
def draw_text_left(draw, text, x, y, font_path, font_size, bold=False):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"⚠ Font not found: {font_path}. Using default. Error: {e}")
        font = ImageFont.load_default()

    if bold:
        for offset in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            draw.text((x + offset[0], y + offset[1]), text, font=font, fill="black")
    else:
        draw.text((x, y), text, font=font, fill="black")

# === File paths ===
base_image_path = r"C:/Users/kuhuy/Downloads/base image.png"
user_photo_path = r"C:/Users/kuhuy/Downloads/8219ee55c0e0eb433debacbe248d151d.jpg"
font_hindi = r"C:\Users\kuhuy\Downloads\Noto_Sans_Devanagari (1)\NotoSansDevanagari-VariableFont_wdth,wght.ttf"
font_eng = "arial.ttf"
font_bold = "arialbd.ttf"

# === User Data ===
name_hindi = "रणविजय यादव"
name_english = "Ranvijay Yadav"
dob = "02/12/2005"
gender = "पुरुष/Male"
aadhar_number = "1234 4567 6789"

# === Load base image ===
try:
    base_img = Image.open(base_image_path).convert("RGB")
except FileNotFoundError:
    print("❌ Base image not found.")
    exit()

draw = ImageDraw.Draw(base_img)

# === Paste user photo ===
photo_x, photo_y = 81, 219
photo_w, photo_h = 164, 194
try:
    user_img = Image.open(user_photo_path).resize((photo_w, photo_h))
    base_img.paste(user_img, (photo_x, photo_y))
except FileNotFoundError:
    print("❌ User photo not found.")
    exit()

# === Text starting point: right side of photo ===
text_x = photo_x + photo_w + 20   # small horizontal space after photo
text_y = photo_y                  # start aligned with top of photo
line_spacing = 35                # vertical spacing between text lines

# === Draw all text fields ===
# === Draw all text fields with correct fonts ===
draw_text_left(draw, name_hindi, text_x, text_y, font_path=font_hindi, font_size=30)  # ✅ Hindi font
draw_text_left(draw, name_english, text_x, text_y + line_spacing, font_path=font_eng, font_size=28)  # ✅ English font
draw_text_left(draw, f"जन्म तिथि/DOB : {dob}", text_x, text_y + 2 * line_spacing, font_path=font_hindi, font_size=26)  # ✅ Hindi font
draw_text_left(draw, "पुरुष/Male", text_x, text_y + 3 * line_spacing, font_path=font_hindi, font_size=26)  # ✅ Hindi font


# === Aadhaar number remains at bottom-right as defined ===
draw_text_left(draw, aadhar_number, 333, 618, font_path=font_bold, font_size=37, bold=True)

# === Save the output image ===
output_path = "final_output_image.jpg"
base_img.save(output_path)
print(f"✅ Final image saved successfully as: {output_path}")