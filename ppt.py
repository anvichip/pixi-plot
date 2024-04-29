from pptx import Presentation
from pptx.util import Inches, Pt

def add_slide(prs, image_path, text):
    slide_layout = prs.slide_layouts[6]  # Use the layout for title and content
    slide = prs.slides.add_slide(slide_layout)

    left_inch = (prs.slide_width - Inches(6)) / 2
    top_inch = (prs.slide_height - Inches(5)) / 2

    # Add image
    slide.shapes.add_picture(image_path, left_inch, top_inch, Inches(6), Inches(4.5))

    # Add text box below image
    txBox = slide.shapes.add_textbox(left_inch, top_inch + Inches(4.5), Inches(6), Inches(1))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(24)  # Increase font size to 24 points
    p.alignment = 1  # Center alignment

def ppt_main(existing_pptx, image_paths, texts):
    prs = Presentation(existing_pptx)
    
    for image_path, text in zip(image_paths, texts):
        add_slide(prs, image_path, text)

    prs.save('output.pptx')


existing_pptx = "template_ppt.pptx"
image_paths = ["generated-1.png", "generated-1.png", "generated-1.png"]  # List of image paths
texts = ["Text 1", "Text 2", "Text 3"]  # List of corresponding texts

ppt_main(existing_pptx, image_paths, texts)
