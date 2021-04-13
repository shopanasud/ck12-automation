from selenium.webdriver.common.by import By


class StudentTutorLocators(object):

    # Variables
    SUBJECTS = ["SCIENCE", "MATH"]
    SCIENCE_TOPICS = ['Earth Science', 'Life Science',
                      'Physical Science', 'Biology', 'Chemistry', 'Physics']
    MATH_TOPICS = ['Math Grade 6', 'Math Grade 7', 'Math Grade 8',
                   'Algebra', 'Geometry', 'Algebra II', 'Precalculus']
    BROWSE_ALL_FLEX = "FlexBooks® | CK-12 Foundation"

    TOPICS_TITLE = [
        [
            "CK-12 Earth Science for Middle School | CK-12 Foundation",
            "CK-12 Life Science for Middle School | CK-12 Foundation",
            "CK-12 Physical Science for Middle School | CK-12 Foundation",
            "CK-12 Biology for High School | CK-12 Foundation",
            "CK-12 Chemistry for High School | CK-12 Foundation",
            "CK-12 Interactive Physics for High School | CK-12 Foundation"
        ],
        [
            "CK-12 Interactive Middle School Math 6 | CK-12 Foundation",
            "CK-12 Interactive Middle School Math 7 | CK-12 Foundation",
            "CK-12 Interactive Middle School Math 8 | CK-12 Foundation",
            "CK-12 Interactive Algebra 1 | CK-12 Foundation",
            "CK-12 Interactive Geometry | CK-12 Foundation",
            "CK-12 Interactive Algebra 2 - 2019 | CK-12 Foundation",
            "CK-12 Precalculus Concepts 2.0 | CK-12 Foundation"
        ]
    ]
    STUDENT_TUTOR = 'Student Tutor | CK-12 Foundation'
    PAGE_TITLES = ['Student Sign Up | CK-12 Foundation',
                   'FlexBooks® | CK-12 Foundation',
                   'Teacher Assistant | CK-12 Foundation',
                   'Student Tutor | CK-12 Foundation']

    HEADERS = ['A FREE Digital Tutor for Every Student',
               'Assists Your Learning',
               'Answers Questions',
               'Checks Your Understanding',
               'Helps You with Assignments and Gets You Unstuck',
               'Guides Your Learning Journey',
               'Helps You with Self-Reflection',
               'Every Student Deserves a Tutor',
               'What Others Are Saying',
               'Start Learning with Flexi!',
               'Are you an educator?',
               'Get started with CK-12 today!']

    AVAILABLE_TEXT = ['Introducing Flexi',
                      'CK-12’s FlexBook® 2.0 is now integrated with Flexi, our AI-powered student tutor.',
                      'Take a Tour',
                      'Choose Your Subject',
                      'A tutor plays an important role in the learning journey of any student. Millions of students who use CK-12 cannot afford a traditional tutor.\n\nLike any great tutor, here’s what Flexi does:',
                      'Flexi makes learning a concept engaging and provides immediate feedback to help students learn complex topics with real world applications.',
                      'Flexi answers students’ questions and provides interactive examples to help them understand the underlying concepts.',
                      '*Currently only available for CK-12 Science FlexBook® 2.0 content',
                      'Flexi tests students’ knowledge of a concept by giving them relevant questions at their skill level.',
                      'Flexi supports students with the right amount of help via hints, content recommendations, and reinforcement of foundational concepts, helping fill knowledge gaps and improve assignment scores.',
                      'Flexi provides timely reminders of students’ upcoming assignments, topics they may have forgotten or missed, their next topic to learn, and any unfinished work, helping them stay on track.',
                      'Flexi helps students self-reflect to answer questions like:',
                      'How am I doing?', 'How can I improve?', 'What am I missing?',
                      'CK-12 is used by millions of students around the world.',
                      'Users Served', '137M+',
                      'Questions Answered', '792M+',
                      'Hours of Learning', '20M+',
                      'Find a subject below to start working with your student tutor!',
                      'Browse All FlexBooks®',
                      'Explore class-level insights and new time-saving teaching tools!',
                      'Take a Tour',
                      'Sign In / Sign Up']

    TESTIMONIAL_TEXT = ['This site has taught me many concepts in math. I want to review so that I will be ready for when I apply for a math position. This site teaches so much more than any other site that I have found.',
                        'Patricia', 'STUDENT',
                        'CK-12 has reinvigorated my love for knowledge and is my go to resource to practice and brush up on skills. Thanks to CK-12 I was able to relearn most of what I forgot and get back in school, thank you CK-12.',
                        'Ibrahin', 'STUDENT']
    MODAL_WIN_TEXT = ['Start Learning with Flexi!',
                      'Find a subject below to start working with your student tutor!',
                      'Browse All FlexBooks®', 'CLOSE']

    LINKS_AVAILABLE = {'Sign In / Sign Up': 'https://www.ck12.org/auth/signup/student',
                       'Browse All FlexBooks®': 'https://www.ck12.org/fbbrowse',
                       'Take a Tour': 'https://www.ck12.org/pages/teacher-assistant',
                       'Earth Science': 'https://flexbooks.ck12.org/cbook/ck-12-middle-school-earth-science-flexbook-2.0/',
                       'Life Science': 'https://flexbooks.ck12.org/cbook/ck-12-middle-school-life-science-2.0/',
                       'Physical Science': 'https://flexbooks.ck12.org/cbook/ck-12-middle-school-physical-science-flexbook-2.0/',
                       'Biology': 'https://flexbooks.ck12.org/cbook/ck-12-biology-flexbook-2.0/',
                       'Chemistry': 'https://flexbooks.ck12.org/cbook/ck-12-chemistry-flexbook-2.0/',
                       'Physics': 'https://flexbooks.ck12.org/cbook/ck-12-physics-flexbook-2.0/',
                       'Math Grade 6': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-middle-school-math-6-for-ccss/',
                       'Math Grade 7': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-middle-school-math-7-for-ccss/',
                       'Math Grade 8': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-middle-school-math-8-for-ccss/',
                       'Algebra': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-algebra-1-for-ccss/',
                       'Geometry': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-geometry-for-ccss/',
                       'Algebra II': 'https://flexbooks.ck12.org/cbook/ck-12-interactive-algebra-2-for-ccss/',
                       'Precalculus': 'https://flexbooks.ck12.org/cbook/ck-12-precalculus-concepts-2.0'}

    IMAGE_SOURCE = {'Earth Science': 'https://www.ck12.org/pages/student-tutor/images/earth-science.svg',
                    'Life Science': 'https://www.ck12.org/pages/student-tutor/images/life-science.svg',
                    'Physical Science': 'https://www.ck12.org/pages/student-tutor/images/physical-science.svg',
                    'Biology': 'https://www.ck12.org/pages/student-tutor/images/biology.svg',
                    'Chemistry': 'https://www.ck12.org/pages/student-tutor/images/chemistry.svg',
                    'Physics': 'https://www.ck12.org/pages/student-tutor/images/physics.svg',
                    'Math Grade 6': 'https://www.ck12.org/pages/student-tutor/images/Math6.svg',
                    'Math Grade 7': 'https://www.ck12.org/pages/student-tutor/images/Math7.svg',
                    'Math Grade 8': 'https://www.ck12.org/pages/student-tutor/images/Math8.svg',
                    'Algebra': 'https://www.ck12.org/pages/student-tutor/images/noun_Algebra_24030.svg',
                    'Geometry': 'https://www.ck12.org/pages/student-tutor/images/geometry.svg',
                    'Algebra II': 'https://www.ck12.org/pages/student-tutor/images/algebra_II.svg',
                    'Precalculus': 'https://www.ck12.org/pages/student-tutor/images/precalculus.svg',
                    'HEADER_LOGO': 'https://www.ck12.org/pages/student-tutor/images/logo_ck12.svg',
                    'TOUR_MOUSE': 'https://www.ck12.org/pages/student-tutor/images/noun_Mouse_Scroll.svg',
                    'CHOOSE_ARROW': 'https://www.ck12.org/pages/student-tutor/images/right-arrow-white.svg',
                    'HERO_SUBHEAD': 'https://www.ck12.org/pages/student-tutor/images/Student-Tutor-Hero-Graphic-v1h.svg',
                    'GENIE': 'https://www.ck12.org/pages/student-tutor/images/Genie.svg',
                    'ASSIST_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/airbagsim.gif',
                    'ASSIST_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/feature1_graphic.svg',
                    'ASSIST_BLOB': 'https://www.ck12.org/pages/student-tutor/images/purpleblog.svg',
                    'ANSWER_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/chatbot_3c.gif',
                    'ANSWER_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/chatbot_screen_mock.svg',
                    'ANSWER_BLOB': 'https://www.ck12.org/pages/student-tutor/images/blob_red.svg',
                    'UNDERSTAND_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/inlineQs.gif',
                    'UNDERSTAND_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/InlineQs-Screen-Mock.svg',
                    'UNDERSTAND_BLOB': 'https://www.ck12.org/pages/student-tutor/images/blob_blue.svg',
                    'ASSIGNMENTS_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/adaptive_tutor_panel.gif',
                    'ASSIGNMENT_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/Adaptive-Tutor-Window-Mck_v1a.svg',
                    'ASSIGNMENT_BLOB': 'https://www.ck12.org/pages/student-tutor/images/blob_yellow.svg',
                    'GUIDES_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/smart_notifications.gif',
                    'GUIDES_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/learningjourney_screen_moc2k.svg',
                    'GUIDES_BLOB': 'https://www.ck12.org/pages/student-tutor/images/blob_green.svg',
                    'SELF_REF_SIMPLIX': 'https://www.ck12.org/pages/student-tutor/images/practicereport2.gif',
                    'SELF_GRAPHIC_WRAP': 'https://www.ck12.org/pages/student-tutor/images/report_screen_mock2.svg',
                    'SELF_BLOB': 'https://www.ck12.org/pages/student-tutor/images/blob_orange.svg',
                    'REMOTE_BANNER': 'https://www.ck12.org/pages/student-tutor/images/educator_banner_graphic.svg',
                    'TESTIMONIAL_USER1': 'https://www.ck12.org/pages/student-tutor/images/testimonial_avatar.svg',
                    'TESTIMONIAL_USER2': 'https://www.ck12.org/pages/student-tutor/images/testimonial_avatar.svg'
                    }
    # Locators for the page

    # Banner present in the header
    BANNER = (
        By.XPATH, "//div[@class='system-notification-dismiss-container']/a")
    # Subjects Locators
    SUBJECTS_LOCATORS = [
        (By.XPATH, "//a[@data-dx-desc='footer-subjects-science-tab']"),
        (By.XPATH, "//a[@id='w-tabs-1-data-w-tab-1']")

    ]
    # Subject Topic locators
    SUB_TOPIC_LOCATORS = [
        (By.XPATH,
         "//div[@class='subjects-items-wrapper footer']//div[@class='subject-name']"),
        (By.XPATH,
         "//div[@class='subjects-items-wrapper']//div[@class='subject-name']")

    ]
    # Subjects Locators in Modal
    MODAL_SUB_LOCATORS = [
        (By.XPATH, "//a[@data-dx-desc='modal-subjects-science-tab']"),
        (By.XPATH, "//a[@data-dx-desc='modal-subjects-math-tab']")

    ]
    # Subject Topic locators in modal
    MODAL_SUB_TOPIC_LOCATORS = [
        (By.XPATH, "//div[@data-w-tab='Tab 1']//div[@class='subjects-items-wrapper modal']//div[@class='subject-name']"),
        (By.XPATH, "//div[@data-w-tab='Tab 2']//div[@class='subjects-items-wrapper modal']//div[@class='subject-name']")
    ]

    # Subjects inside Start learning with Flex modal
    MODAL_SUBJECTS = (
        By.XPATH, "//div[@class='feature-1-container subjects modal w-container']//div[@class='tabs-menu-2 w-tab-menu']//a//div")

    # Subjects locators(Both top and Bottom)
    SUBJECT_TABS = (
        By.XPATH, "//div[@class='feature-1-container subjects footer w-container']//div[@class='tabs-menu-2 w-tab-menu']//div")
    # Science subjects in Start Learning withFlexi to get Text
    SCIENCE_SUBJECTS = (
        By.XPATH, "//div[@class='subjects-items-wrapper footer']//div[@class='subject-name']")
    # Maths Subjects in Start Learning withFlexi to get text
    MATH_SUBJECTS = (
        By.XPATH, "//div[@class='subjects-items-wrapper']//div[@class='subject-name']")
    # Locators for checking the links

    # Locators of the links of signUp, teacher Tutor, browse all Flexibooks, Take a tour.
    LINK_PAGE_TITLES = [
        (By.XPATH, "//a[@data-dx-desc='footer-sign-up-cta']"),
        (By.XPATH,
         "//a[@data-dx-desc='footer-subjects-browse-all-fbs']"),
        (By.XPATH, "//a[@data-dx-desc='footer-educator']"),
        (By.XPATH,
         "//a[@class='cta-main-with-icon-wrapper dxtrack-user-action w-inline-block']")
    ]

    # Tag name
    LINK_IMAGE_TAGS = {
        "img": "src"
    }
    # Locator of browse all Flexibooks in the footer.
    LINK_FOOTER_BROWSE = (
        By.XPATH, "//a[@data-dx-desc='footer-subjects-browse-all-fbs']")
    # Locator of Take a tour in the header
    LINK_TAKE_A_TOUR_BUTTON = (
        By.XPATH, "//a[@class='cta-main-with-icon-wrapper dxtrack-user-action w-inline-block']")
    # Locator os Choose your subject in Header
    LINK_CHOOSE_YOUR = (
        By.XPATH, "//div[@class='secondary-cta-text']")

    # MODAL WINDOW BROWSE ALL FLEXBOOKS
    LINK_BROWSE_ALL_FLEXBOOKS_MODAL_WINDOW_TEXT = (
        By.XPATH, "//a[@data-dx-desc='modal-subjects-browse-all-fbs']")
    # MODAL WINDOW CLOSE BUTTON
    LINK_CLOSE_BUTTON = (
        By.XPATH, "//div[@class='modal-close-link dxtrack-user-action']")
    # CAROUSEL LOCATORES
    CAROUSEL_CONTAINER = (By.XPATH, "//div[@class='testimonials-wrapper']")
    LINK_TESTIMONIALS = [(
        By.XPATH, "//div[@class='slide-nav w-slider-nav w-round']/div[2]"),
        (
        By.XPATH, "//div[@class='slide-nav w-slider-nav w-round']/div[1]")]
    # Locator of Subject container in the footer
    LINK_SUB_CONTAINER_FOOTER = (
        By.CSS_SELECTOR, "div[class='feature-1-container subjects footer w-container']")
    # Text Locators
    # Locators of All headings
    TEXT_HEADERS = [
        (By.XPATH, "(//h1/strong)[1]"),
        (By.XPATH, "(//h1/strong)[2]"),
        (By.XPATH, "(//h1/strong)[3]"),
        (By.XPATH, "(//h1/strong)[4]"),
        (By.XPATH, "(//h1/strong)[5]"),
        (By.XPATH, "(//h1/strong)[6]"),
        (By.XPATH, "(//h1/strong)[7]"),
        (By.XPATH, "(//div[contains(@class,'h3')])[2]"),
        (By.XPATH, "(//div[contains(@class,'h3')])[3]"),
        (By.XPATH, "(//div[contains(@class,'h3')])[4]"),
        (By.XPATH, "// h1[@class = 'remote-banner-title']"),
        (By.XPATH, "//div[@class='cta-copy']")
    ]

    # Social Proof Cards
    TEXT_SOCIAL_PROOF_CARDS = (
        By.XPATH, "//div[@class='social-proof-container']//p")
    TEXT_MILLIONS_OF_STUD = (
        By.XPATH, "//div[@class='social-proof-container']")

    # CROUSEL Text
    TEXT_TESTIMONIALS = [(
        By.XPATH, "//div[@aria-label='2 of 2']//div[@class='testimonial-item-wrap']/div"),
        (
        By.XPATH, "//div[@aria-label='1 of 2']//div[@class='testimonial-item-wrap']/div")
    ]

    TEXT_LOCATORS = [
        (By.XPATH, "//div[@class='cta-main-text']"),
        (By.XPATH, "//div[@class='secondary-cta-text']"),
        (By.TAG_NAME, "p"), (By.TAG_NAME, "li"),
        (By.XPATH, "//div[@class='paragraph about']"),
        (By.XPATH,
         "(//div[@class='h3']/following-sibling::div[@class='paragraph'])[2]"),
        (By.XPATH,
         "//a[@data-dx-desc='footer-subjects-browse-all-fbs']"),
        (By.XPATH, "//a[@data-dx-desc='footer-educator']"),
        (By.XPATH, "//a[@data-dx-desc='footer-sign-up-cta']")]
    # Locators of text present in the modal
    TEXT_IN_MODAL = [(By.XPATH, "(//div[contains(@class,'h3')])[1]"),
                     (By.XPATH,
                      "(//div[@class='h3']/following-sibling::div[@class='paragraph'])[1]"),
                     (By.XPATH,
                      "//a[@data-dx-desc='modal-subjects-browse-all-fbs']"),
                     (By.XPATH, "//div[@class='modal-close-link dxtrack-user-action']")]
    # Locators of all the images
    IMAGE_LINKS = {
        "HEADER_LOGO": (By.XPATH, "//img[@class='logo']"),
        "TOUR_MOUSE": (By.XPATH, "//img[@src='images/noun_Mouse_Scroll.svg']"),
        "CHOOSE_ARROW": (By.XPATH, "//img[@class='right-arrow-white']"),
        "HERO_SUBHEAD": (By.XPATH, "//img[@class='hero-image']"),
        "GENIE": (By.XPATH, "//img[@class='genie']"),
        "ASSIST_SIMPLIX": (By.XPATH, "//img[@class='sim plix']"),
        "ASSIST_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim plix']/following-sibling::img"),
        "ASSIST_BLOB": (By.XPATH, "(//img[@class='blob right'])[1]"),
        "ANSWER_SIMPLIX": (By.XPATH, "//img[@class='sim chatbot']"),
        "ANSWER_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim chatbot']/following-sibling::img"),
        "ANSWER_BLOB": (By.XPATH, "(//img[@class='blob left'])[1]"),
        "UNDERSTAND_SIMPLIX": (By.XPATH, "//img[@class='sim inline']"),
        "UNDERSTAND_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim inline']/following-sibling::img"),
        "UNDERSTAND_BLOB": (By.XPATH, "(//img[@class='blob right'])[2]"),
        "ASSIGNMENTS_SIMPLIX": (By.XPATH, "//img[@class='sim unstuck']"),
        "ASSIGNMENT_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim unstuck']/following-sibling::img"),
        "ASSIGNMENT_BLOB": (By.XPATH, "(//img[@class='blob left'])[2]"),
        "GUIDES_SIMPLIX": (By.XPATH, "//img[@class='sim journey']"),
        "GUIDES_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim journey']/following-sibling::img"),
        "GUIDES_BLOB": (By.XPATH, "(//img[@class='blob right'])[3]"),
        "SELF_REF_SIMPLIX": (By.XPATH, "//img[@class='sim improve']"),
        "SELF_GRAPHIC_WRAP": (By.XPATH, "//img[@class='sim improve']/following-sibling::img"),
        "SELF_BLOB": (By.XPATH, "(//img[@class='blob left'])[3]"),
        "REMOTE_BANNER": (By.CLASS_NAME, "image-6")
    }
    # Locators of image in Testimonial
    TESTIMONIAL_IMAGE = {
        "TESTIMONIAL_USER1": (By.XPATH, "(//img[@class='image-5'])[2]"),
        "TESTIMONIAL_USER2": (By.XPATH, "(//img[@class='image-5'])[1]")
    }
    # Locators of image of the subject topics in footer
    SUB_IMAGE_LINKS = {
        "SCIENCE_TOPIC_IMG": (By.XPATH, "//div[@class='subjects-items-wrapper footer']//img"),

        "MATH_TOPIC_IMG": (By.XPATH, "//div[@class='subjects-items-wrapper']//img")
    }
    # Locators of image of the subject topics in modal
    MODAL_SUB_IMAGE_LINKS = {
        "MODAL_SCIENCE_TOPIC_IMG":
        (By.XPATH, "(//div[@class='subjects-items-wrapper modal'])[1]//img"),
        "MODAL_MATH_TOPIC_IMG": (By.XPATH, "(//div[@class='subjects-items-wrapper modal'])[2]//img")
    }
    # Locators of the subject present in the modal To get the source
    LINK_MODAL_SUBS = [
        (By.XPATH, "(//div[@class='subjects-items-wrapper modal'])[1]/a"),
        (By.XPATH, "(//div[@class='subjects-items-wrapper modal'])[2]/a")
    ]
    # Locators of the subject present in the footer To get the source
    LINK_FOOTER_SUBS = [
        (By.XPATH, "//div[@class='subjects-items-wrapper footer']/a"),
        (By.XPATH, "//div[@class='subjects-items-wrapper']/a")
    ]
    # Locators of the links of signUp, teacher Tutor, browse all Flexibooks, Take a tour. To get the source
    LINK_FOOTER_REST = [
        (By.XPATH, "//a[@data-dx-desc='footer-sign-up-cta']"),
        (By.XPATH, "//a[@data-dx-desc='footer-subjects-browse-all-fbs']"),
        (By.XPATH, "//a[@data-dx-desc='footer-educator']")
    ]
