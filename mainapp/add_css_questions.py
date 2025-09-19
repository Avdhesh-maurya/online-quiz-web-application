from mainapp.models import Question


def add_questions():
    # ------------------ 30 CSS Questions ------------------
    Question.objects.create(
        text="What does CSS stand for?",
        option1="Cascading Style Sheets",
        option2="Computer Style Sheets",
        option3="Creative Style System",
        option4="Colorful Style Sheets",
        answer="Cascading Style Sheets",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to change the text color in CSS?",
        option1="font-color",
        option2="color",
        option3="text-color",
        option4="fgcolor",
        answer="color",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to make text bold?",
        option1="font-weight",
        option2="text-weight",
        option3="font-style",
        option4="text-style",
        answer="font-weight",
        category="CSS",
    )

    Question.objects.create(
        text="Which property changes the background color of an element?",
        option1="background-color",
        option2="bgcolor",
        option3="color",
        option4="background-style",
        answer="background-color",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to change the font of an element?",
        option1="font-family",
        option2="text-font",
        option3="font-style",
        option4="text-family",
        answer="font-family",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to set the width of an element?",
        option1="width",
        option2="height",
        option3="size",
        option4="element-width",
        answer="width",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to set the height of an element?",
        option1="width",
        option2="height",
        option3="size",
        option4="element-height",
        answer="height",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to align text horizontally?",
        option1="text-align",
        option2="align",
        option3="horizontal-align",
        option4="text-position",
        answer="text-align",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to add space inside an element (padding)?",
        option1="margin",
        option2="padding",
        option3="spacing",
        option4="border",
        answer="padding",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to add space outside an element (margin)?",
        option1="margin",
        option2="padding",
        option3="spacing",
        option4="border",
        answer="margin",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to set the border color of an element?",
        option1="border-color",
        option2="color",
        option3="border-style",
        option4="border-width",
        answer="border-color",
        category="CSS",
    )

    Question.objects.create(
        text="Which property controls the style of the border?",
        option1="border-style",
        option2="border-width",
        option3="border-color",
        option4="border-radius",
        answer="border-style",
        category="CSS",
    )

    Question.objects.create(
        text="Which property rounds the corners of an element's border?",
        option1="border-radius",
        option2="border-style",
        option3="border-width",
        option4="border-corner",
        answer="border-radius",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to make text italic?",
        option1="font-style",
        option2="text-style",
        option3="font-variant",
        option4="text-transform",
        answer="font-style",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to change the font size?",
        option1="font-size",
        option2="text-size",
        option3="font-style",
        option4="text-style",
        answer="font-size",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to control the visibility of an element?",
        option1="visible",
        option2="display",
        option3="visibility",
        option4="hidden",
        answer="visibility",
        category="CSS",
    )

    Question.objects.create(
        text="Which property specifies how the content is positioned inside a flex container?",
        option1="justify-content",
        option2="align-items",
        option3="flex-direction",
        option4="flex-wrap",
        answer="justify-content",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to change the spacing between lines of text?",
        option1="line-height",
        option2="letter-spacing",
        option3="text-spacing",
        option4="word-spacing",
        answer="line-height",
        category="CSS",
    )

    Question.objects.create(
        text="Which property sets the spacing between characters in text?",
        option1="line-height",
        option2="letter-spacing",
        option3="text-spacing",
        option4="word-spacing",
        answer="letter-spacing",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to transform elements (e.g., rotate, scale)?",
        option1="transform",
        option2="transition",
        option3="animation",
        option4="translate",
        answer="transform",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to create smooth transitions for CSS properties?",
        option1="transform",
        option2="transition",
        option3="animation",
        option4="translate",
        answer="transition",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to animate elements in CSS?",
        option1="transform",
        option2="transition",
        option3="animation",
        option4="animate",
        answer="animation",
        category="CSS",
    )

    Question.objects.create(
        text="Which property specifies the type of list in a list element?",
        option1="list-type",
        option2="list-style-type",
        option3="list-style",
        option4="list-format",
        answer="list-style-type",
        category="CSS",
    )

    Question.objects.create(
        text="Which property specifies the image used as a background?",
        option1="background-image",
        option2="background",
        option3="bg-image",
        option4="image-src",
        answer="background-image",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to repeat a background image?",
        option1="background-repeat",
        option2="background-tiling",
        option3="background-repeat-style",
        option4="repeat-background",
        answer="background-repeat",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to position a background image?",
        option1="background-position",
        option2="background-align",
        option3="background-place",
        option4="bg-position",
        answer="background-position",
        category="CSS",
    )

    Question.objects.create(
        text="Which property sets the stacking order of elements?",
        option1="stack-index",
        option2="z-index",
        option3="layer-order",
        option4="order",
        answer="z-index",
        category="CSS",
    )

    Question.objects.create(
        text="Which property controls the overflow of content in an element?",
        option1="overflow",
        option2="content-overflow",
        option3="text-overflow",
        option4="clip",
        answer="overflow",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to create a shadow effect on text?",
        option1="text-shadow",
        option2="box-shadow",
        option3="shadow",
        option4="font-shadow",
        answer="text-shadow",
        category="CSS",
    )

    Question.objects.create(
        text="Which property is used to create a shadow effect on a box element?",
        option1="text-shadow",
        option2="box-shadow",
        option3="shadow",
        option4="element-shadow",
        answer="box-shadow",
        category="CSS",
    )

    print("✅ 30 CSS Questions added successfully!")
