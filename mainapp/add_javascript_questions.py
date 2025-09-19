from mainapp.models import Question

def add_questions():
    # ------------------ 30 JavaScript Questions ------------------
    Question.objects.create(
        text="Which keyword is used to declare a constant in JavaScript?",
        option1="var",
        option2="let",
        option3="const",
        option4="define",
        answer="const",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which company developed JavaScript?",
        option1="Microsoft",
        option2="Netscape",
        option3="Google",
        option4="Oracle",
        answer="Netscape",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which symbol is used for single-line comments in JavaScript?",
        option1="//",
        option2="<!-- -->",
        option3="#",
        option4="**",
        answer="//",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method is used to add an element at the end of an array?",
        option1="push()",
        option2="pop()",
        option3="shift()",
        option4="unshift()",
        answer="push()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which operator is used for strict equality comparison?",
        option1="==",
        option2="===",
        option3="=",
        option4="!==",
        answer="===",
        category="JavaScript"
    )

    Question.objects.create(
        text="What is the output of `typeof NaN`?",
        option1="number",
        option2="NaN",
        option3="undefined",
        option4="object",
        answer="number",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method converts a JSON string to a JavaScript object?",
        option1="JSON.parse()",
        option2="JSON.stringify()",
        option3="JSON.object()",
        option4="JSON.toObject()",
        answer="JSON.parse()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method converts a JavaScript object to a JSON string?",
        option1="JSON.parse()",
        option2="JSON.stringify()",
        option3="JSON.object()",
        option4="JSON.toString()",
        answer="JSON.stringify()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which function is used to execute code after a specified delay?",
        option1="setInterval()",
        option2="setTimeout()",
        option3="delay()",
        option4="wait()",
        answer="setTimeout()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method removes the last element from an array?",
        option1="pop()",
        option2="push()",
        option3="shift()",
        option4="unshift()",
        answer="pop()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method removes the first element from an array?",
        option1="pop()",
        option2="push()",
        option3="shift()",
        option4="unshift()",
        answer="shift()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which keyword is used to declare a block-scoped variable?",
        option1="var",
        option2="let",
        option3="const",
        option4="block",
        answer="let",
        category="JavaScript"
    )

    Question.objects.create(
        text="What will `console.log(2 + '2')` output?",
        option1="4",
        option2="'4'",
        option3="'22'",
        option4="Error",
        answer="'22'",
        category="JavaScript"
    )

    Question.objects.create(
        text="What will `console.log(2 * '2')` output?",
        option1="4",
        option2="22",
        option3="'4'",
        option4="NaN",
        answer="4",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which keyword is used to create a class in JavaScript?",
        option1="class",
        option2="Class",
        option3="function",
        option4="object",
        answer="class",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which event occurs when a user clicks on an element?",
        option1="onclick",
        option2="onmouseover",
        option3="onchange",
        option4="onhover",
        answer="onclick",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method returns the length of an array?",
        option1="length()",
        option2="size()",
        option3="arr.length",
        option4="count()",
        answer="arr.length",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which object is the global object in browsers?",
        option1="window",
        option2="global",
        option3="document",
        option4="self",
        answer="window",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method finds the index of an element in an array?",
        option1="find()",
        option2="indexOf()",
        option3="search()",
        option4="locate()",
        answer="indexOf()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method is used to combine two arrays?",
        option1="concat()",
        option2="combine()",
        option3="merge()",
        option4="append()",
        answer="concat()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which keyword is used to handle exceptions in JavaScript?",
        option1="try",
        option2="catch",
        option3="throw",
        option4="finally",
        answer="try",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which keyword is used with try to catch exceptions?",
        option1="try",
        option2="catch",
        option3="throw",
        option4="finally",
        answer="catch",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method stops the default action of an event?",
        option1="preventDefault()",
        option2="stopPropagation()",
        option3="stopEvent()",
        option4="cancel()",
        answer="preventDefault()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which operator is used to assign a value to a variable?",
        option1="==",
        option2="===",
        option3="=",
        option4="=>",
        answer="=",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which keyword is used to define an asynchronous function?",
        option1="async",
        option2="await",
        option3="defer",
        option4="asynch",
        answer="async",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method is used to create a new array with all elements that pass a test?",
        option1="map()",
        option2="filter()",
        option3="reduce()",
        option4="forEach()",
        answer="filter()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method executes a provided function once for each array element?",
        option1="map()",
        option2="filter()",
        option3="reduce()",
        option4="forEach()",
        answer="forEach()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method reduces an array to a single value?",
        option1="map()",
        option2="filter()",
        option3="reduce()",
        option4="forEach()",
        answer="reduce()",
        category="JavaScript"
    )

    Question.objects.create(
        text="Which method returns a new array with the results of calling a function on every element?",
        option1="map()",
        option2="filter()",
        option3="reduce()",
        option4="forEach()",
        answer="map()",
        category="JavaScript"
    )

    print("✅ 30 JavaScript Questions added successfully!")
