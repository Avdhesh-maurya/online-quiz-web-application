from mainapp.models import Question


def add_questions():
    # ------------------ 30 Easy Java Questions ------------------
    Question.objects.create(
        text="Which keyword is used to define a class in Java?",
        option1="class",
        option2="Class",
        option3="define",
        option4="object",
        answer="class",
        category="Java",
    )

    Question.objects.create(
        text="Which method is the entry point of a Java program?",
        option1="start()",
        option2="main()",
        option3="run()",
        option4="init()",
        answer="main()",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to create an object in Java?",
        option1="create",
        option2="new",
        option3="object",
        option4="init",
        answer="new",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used for inheritance in Java?",
        option1="implements",
        option2="extends",
        option3="inherits",
        option4="super",
        answer="extends",
        category="Java",
    )

    Question.objects.create(
        text="Which of these is not a primitive data type in Java?",
        option1="int",
        option2="boolean",
        option3="String",
        option4="char",
        answer="String",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to define a constant in Java?",
        option1="final",
        option2="const",
        option3="static",
        option4="constant",
        answer="final",
        category="Java",
    )

    Question.objects.create(
        text="Which operator is used to compare two values for equality?",
        option1="=",
        option2="==",
        option3="===",
        option4="!=",
        answer="==",
        category="Java",
    )

    Question.objects.create(
        text="Which of the following is used for comments in Java?",
        option1="// for single-line, /* */ for multi-line",
        option2="<!-- -->",
        option3="#",
        option4="**",
        answer="// for single-line, /* */ for multi-line",
        category="Java",
    )

    Question.objects.create(
        text="Which loop is guaranteed to execute at least once?",
        option1="for loop",
        option2="while loop",
        option3="do-while loop",
        option4="for-each loop",
        answer="do-while loop",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to inherit from an interface?",
        option1="extends",
        option2="implements",
        option3="inherits",
        option4="interface",
        answer="implements",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to define a method that does not return a value?",
        option1="void",
        option2="null",
        option3="empty",
        option4="none",
        answer="void",
        category="Java",
    )

    Question.objects.create(
        text="Which of these is used to create a single-line comment?",
        option1="//",
        option2="/* */",
        option3="<!-- -->",
        option4="#",
        answer="//",
        category="Java",
    )

    Question.objects.create(
        text="Which of the following is a valid identifier in Java?",
        option1="1variable",
        option2="myVariable",
        option3="my-variable",
        option4="class",
        answer="myVariable",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to prevent inheritance of a class?",
        option1="stop",
        option2="final",
        option3="private",
        option4="static",
        answer="final",
        category="Java",
    )

    Question.objects.create(
        text="Which access modifier allows a member to be accessed only within the same class?",
        option1="private",
        option2="protected",
        option3="public",
        option4="default",
        answer="private",
        category="Java",
    )

    Question.objects.create(
        text="Which access modifier allows access from the same package and subclasses?",
        option1="private",
        option2="protected",
        option3="public",
        option4="default",
        answer="protected",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to create a subclass in Java?",
        option1="extends",
        option2="implements",
        option3="inherits",
        option4="super",
        answer="extends",
        category="Java",
    )

    Question.objects.create(
        text="Which of the following is used to handle exceptions in Java?",
        option1="try-catch",
        option2="handle",
        option3="throw-exception",
        option4="error",
        answer="try-catch",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to explicitly throw an exception?",
        option1="throw",
        option2="throws",
        option3="exception",
        option4="catch",
        answer="throw",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to declare a variable that cannot be modified?",
        option1="final",
        option2="const",
        option3="static",
        option4="immutable",
        answer="final",
        category="Java",
    )

    Question.objects.create(
        text="Which class is the parent of all classes in Java?",
        option1="Object",
        option2="Class",
        option3="Parent",
        option4="Main",
        answer="Object",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to call the constructor of a parent class?",
        option1="super",
        option2="this",
        option3="parent",
        option4="base",
        answer="super",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to create a thread in Java?",
        option1="Thread",
        option2="Runnable",
        option3="extends Thread",
        option4="implements Runnable",
        answer="Thread",
        category="Java",
    )

    Question.objects.create(
        text="Which package is automatically imported in every Java program?",
        option1="java.util",
        option2="java.lang",
        option3="java.io",
        option4="java.sql",
        answer="java.lang",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to access the current object in Java?",
        option1="this",
        option2="super",
        option3="self",
        option4="current",
        answer="this",
        category="Java",
    )

    Question.objects.create(
        text="Which of the following is a loop used to iterate over arrays or collections?",
        option1="for-each loop",
        option2="while loop",
        option3="do-while loop",
        option4="switch loop",
        answer="for-each loop",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to stop execution of a loop or switch statement?",
        option1="break",
        option2="continue",
        option3="stop",
        option4="exit",
        answer="break",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to skip the current iteration of a loop?",
        option1="break",
        option2="continue",
        option3="skip",
        option4="pass",
        answer="continue",
        category="Java",
    )

    Question.objects.create(
        text="Which data type is used to store true or false values?",
        option1="int",
        option2="boolean",
        option3="char",
        option4="double",
        answer="boolean",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to create an array in Java?",
        option1="array",
        option2="[]",
        option3="new",
        option4="create",
        answer="new",
        category="Java",
    )

    Question.objects.create(
        text="Which of these methods is used to get the length of an array?",
        option1="length()",
        option2="size()",
        option3="length",
        option4="count()",
        answer="length",
        category="Java",
    )

    Question.objects.create(
        text="Which keyword is used to define a static method in Java?",
        option1="static",
        option2="final",
        option3="void",
        option4="const",
        answer="static",
        category="Java",
    )

    # ------------------ 30 PHP Questions ------------------
    Question.objects.create(
        text="What does PHP stand for?",
        option1="Personal Home Page",
        option2="Private Home Page",
        option3="PHP: Hypertext Preprocessor",
        option4="Pretext Hyper Processor",
        answer="PHP: Hypertext Preprocessor",
        category="PHP",
    )

    Question.objects.create(
        text="Which symbol is used to declare a variable in PHP?",
        option1="$",
        option2="&",
        option3="#",
        option4="%",
        answer="$",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to output text in PHP?",
        option1="echo",
        option2="print",
        option3="Both echo and print",
        option4="printf",
        answer="Both echo and print",
        category="PHP",
    )

    Question.objects.create(
        text="Which of the following is used to end a PHP statement?",
        option1=".",
        option2=";",
        option3=":",
        option4=",",
        answer=";",
        category="PHP",
    )

    Question.objects.create(
        text="Which of the following is used to concatenate strings in PHP?",
        option1="+",
        option2=".",
        option3="&",
        option4="concat()",
        answer=".",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to get the length of a string?",
        option1="strlen()",
        option2="size()",
        option3="length()",
        option4="strlength()",
        answer="strlen()",
        category="PHP",
    )

    Question.objects.create(
        text="Which of the following is used to include files in PHP?",
        option1="include",
        option2="require",
        option3="Both include and require",
        option4="insert",
        answer="Both include and require",
        category="PHP",
    )

    Question.objects.create(
        text="Which superglobal array holds form data sent using the POST method?",
        option1="$_POST",
        option2="$_GET",
        option3="$_REQUEST",
        option4="$_FORM",
        answer="$_POST",
        category="PHP",
    )

    Question.objects.create(
        text="Which superglobal array holds form data sent using the GET method?",
        option1="$_POST",
        option2="$_GET",
        option3="$_REQUEST",
        option4="$_FORM",
        answer="$_GET",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to check if a variable is set?",
        option1="isset()",
        option2="empty()",
        option3="exist()",
        option4="defined()",
        answer="isset()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to remove whitespace from the beginning and end of a string?",
        option1="trim()",
        option2="strip()",
        option3="strip_tags()",
        option4="clean()",
        answer="trim()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to convert a string to uppercase?",
        option1="strtoupper()",
        option2="toupper()",
        option3="uppercase()",
        option4="upper()",
        answer="strtoupper()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to convert a string to lowercase?",
        option1="strtolower()",
        option2="tolower()",
        option3="lowercase()",
        option4="lower()",
        answer="strtolower()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to generate a random number in PHP?",
        option1="rand()",
        option2="random()",
        option3="mt_rand()",
        option4="Both rand() and mt_rand()",
        answer="Both rand() and mt_rand()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to start a session in PHP?",
        option1="session_start()",
        option2="start_session()",
        option3="session_begin()",
        option4="begin_session()",
        answer="session_start()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to destroy a session in PHP?",
        option1="session_destroy()",
        option2="destroy_session()",
        option3="end_session()",
        option4="close_session()",
        answer="session_destroy()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to get the current date in PHP?",
        option1="date()",
        option2="time()",
        option3="current_date()",
        option4="now()",
        answer="date()",
        category="PHP",
    )

    Question.objects.create(
        text="Which operator is used to concatenate strings in PHP?",
        option1="+",
        option2=".",
        option3="&",
        option4="concat()",
        answer=".",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to check if a variable is empty?",
        option1="empty()",
        option2="isset()",
        option3="isnull()",
        option4="check_empty()",
        answer="empty()",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to redirect to another page in PHP?",
        option1="redirect()",
        option2="header()",
        option3="goto()",
        option4="move()",
        answer="header()",
        category="PHP",
    )

    Question.objects.create(
        text="Which operator is used for equality comparison in PHP?",
        option1="=",
        option2="==",
        option3="===",
        option4="!=",
        answer="==",
        category="PHP",
    )

    Question.objects.create(
        text="Which of the following is used to comment multiple lines in PHP?",
        option1="//",
        option2="/* */",
        option3="<!-- -->",
        option4="#",
        answer="/* */",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to include and evaluate a specified file during execution?",
        option1="include()",
        option2="require()",
        option3="include_once()",
        option4="All of the above",
        answer="All of the above",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to get the length of an array in PHP?",
        option1="count()",
        option2="sizeof()",
        option3="Both count() and sizeof()",
        option4="length()",
        answer="Both count() and sizeof()",
        category="PHP",
    )

    Question.objects.create(
        text="Which superglobal array contains information about headers, paths, and script locations?",
        option1="$_SERVER",
        option2="$_REQUEST",
        option3="$_ENV",
        option4="$_GLOBAL",
        answer="$_SERVER",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to replace text in a string?",
        option1="str_replace()",
        option2="replace()",
        option3="substr_replace()",
        option4="change()",
        answer="str_replace()",
        category="PHP",
    )

    Question.objects.create(
        text="Which of these is a PHP loop structure?",
        option1="for",
        option2="while",
        option3="do-while",
        option4="All of the above",
        answer="All of the above",
        category="PHP",
    )

    Question.objects.create(
        text="Which function is used to get the type of a variable in PHP?",
        option1="gettype()",
        option2="typeof()",
        option3="var_type()",
        option4="type()",
        answer="gettype()",
        category="PHP",
    )

    Question.objects.create(
        text="Which keyword is used to declare a constant in PHP?",
        option1="define()",
        option2="const",
        option3="constant",
        option4="final",
        answer="const",
        category="PHP",
    )

    Question.objects.create(
        text="Which of the following is used to terminate a PHP script?",
        option1="stop",
        option2="exit",
        option3="end",
        option4="quit",
        answer="exit",
        category="PHP",
    )

    print("✅ 30 PHP Questions added successfully!")
