from mainapp.models import Question


def add_questions():
    # ------------------ 30 Bootstrap Questions ------------------
    Question.objects.create(
        text="Which class is used to create a responsive container in Bootstrap?",
        option1=".container",
        option2=".container-fluid",
        option3=".row",
        option4=".col",
        answer=".container",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a full-width container in Bootstrap?",
        option1=".container",
        option2=".container-fluid",
        option3=".row",
        option4=".col",
        answer=".container-fluid",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a primary button?",
        option1=".btn-primary",
        option2=".btn-main",
        option3=".btn-default",
        option4=".button-primary",
        answer=".btn-primary",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used for a secondary button?",
        option1=".btn-secondary",
        option2=".btn-default",
        option3=".btn-light",
        option4=".btn-alt",
        answer=".btn-secondary",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a success button?",
        option1=".btn-success",
        option2=".btn-primary",
        option3=".btn-safe",
        option4=".btn-green",
        answer=".btn-success",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class makes images responsive in Bootstrap?",
        option1=".img-responsive",
        option2=".img-fluid",
        option3=".responsive-img",
        option4=".img-scale",
        answer=".img-fluid",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to make a navbar dark themed?",
        option1=".navbar-dark",
        option2=".navbar-light",
        option3=".navbar-dark-theme",
        option4=".navbar-black",
        answer=".navbar-dark",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to make a navbar light themed?",
        option1=".navbar-dark",
        option2=".navbar-light",
        option3=".navbar-light-theme",
        option4=".navbar-white",
        answer=".navbar-light",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a row in Bootstrap grid?",
        option1=".row",
        option2=".col",
        option3=".grid",
        option4=".container",
        answer=".row",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to define a column in Bootstrap grid?",
        option1=".col",
        option2=".row",
        option3=".grid-col",
        option4=".column",
        answer=".col",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to hide elements on small devices?",
        option1=".d-none .d-sm-block",
        option2=".hidden-sm",
        option3=".hide-sm",
        option4=".invisible-sm",
        answer=".d-none .d-sm-block",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class adds spacing between elements in Bootstrap?",
        option1=".margin",
        option2=".padding",
        option3=".m-3",
        option4=".space",
        answer=".m-3",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class adds padding in Bootstrap?",
        option1=".p-3",
        option2=".pad-3",
        option3=".padding",
        option4=".spacing",
        answer=".p-3",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create an alert box in Bootstrap?",
        option1=".alert",
        option2=".notification",
        option3=".message",
        option4=".alert-box",
        answer=".alert",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a success alert?",
        option1=".alert-success",
        option2=".alert-primary",
        option3=".alert-safe",
        option4=".alert-green",
        answer=".alert-success",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a danger alert?",
        option1=".alert-danger",
        option2=".alert-error",
        option3=".alert-red",
        option4=".alert-fail",
        answer=".alert-danger",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to make tables responsive in Bootstrap?",
        option1=".table-responsive",
        option2=".table-fluid",
        option3=".responsive-table",
        option4=".table-wrap",
        answer=".table-responsive",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used for striped tables in Bootstrap?",
        option1=".table-striped",
        option2=".table-striped-rows",
        option3=".striped",
        option4=".row-striped",
        answer=".table-striped",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a modal?",
        option1=".modal",
        option2=".popup",
        option3=".dialog",
        option4=".modal-box",
        answer=".modal",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used for progress bars in Bootstrap?",
        option1=".progress",
        option2=".progress-bar",
        option3=".bar-progress",
        option4=".loading-bar",
        answer=".progress",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used for a badge in Bootstrap?",
        option1=".badge",
        option2=".label",
        option3=".tag",
        option4=".counter",
        answer=".badge",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to style a breadcrumb navigation?",
        option1=".breadcrumb",
        option2=".nav-breadcrumb",
        option3=".bread-nav",
        option4=".crumbs",
        answer=".breadcrumb",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to create a responsive embed for videos?",
        option1=".embed-responsive",
        option2=".video-responsive",
        option3=".responsive-video",
        option4=".video-embed",
        answer=".embed-responsive",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to add a card component?",
        option1=".card",
        option2=".panel",
        option3=".box",
        option4=".container-card",
        answer=".card",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to make a card header?",
        option1=".card-header",
        option2=".card-top",
        option3=".header-card",
        option4=".card-title",
        answer=".card-header",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to add a card body?",
        option1=".card-body",
        option2=".card-content",
        option3=".body-card",
        option4=".card-main",
        answer=".card-body",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to make a responsive column in Bootstrap 4?",
        option1=".col-sm",
        option2=".col-md",
        option3=".col-lg",
        option4=".col-xl",
        answer=".col-sm",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to add shadows to Bootstrap elements?",
        option1=".shadow",
        option2=".box-shadow",
        option3=".shadow-lg",
        option4=".shadow-sm",
        answer=".shadow",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to float an element to the right?",
        option1=".float-right",
        option2=".float-end",
        option3=".align-right",
        option4=".right-align",
        answer=".float-right",
        category="Bootstrap",
    )

    Question.objects.create(
        text="Which class is used to float an element to the left?",
        option1=".float-left",
        option2=".float-start",
        option3=".align-left",
        option4=".left-align",
        answer=".float-left",
        category="Bootstrap",
    )

    print("✅ 30 Bootstrap Questions added successfully!")
